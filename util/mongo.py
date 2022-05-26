#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 7:56:24 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Thu May 26 2022
# Modified By: ZhanG
###
import json
from .const import MongoUN, MongoPW, MongoHost
from motor.motor_asyncio import AsyncIOMotorClient

MongoUri = f"mongodb://{MongoUN}:{MongoPW}@{MongoHost}"
mclient = AsyncIOMotorClient(MongoUri)
mdb = mclient["ASOUL"]


async def MemberUpdate(sec_uid: str, new: json):
    mdb['member'].update_one({'user_info.sec_uid': sec_uid}, {
                             '$set': new}, upsert=True)


async def VideoInfoUpdate(aweme_id: str, new: json):
    mdb['video'].update_one({'aweme_id': aweme_id}, {'$set': new}, upsert=True)


async def GetMemberInfo():
    pipeline = [
        {
            "$project": {"user_info.nickname": 1, "user_info.signature": 1, "user_info.sec_uid": 1, "user_info.uid": 1, "user_info.avatar_larger.url_list": 1}
        },
        # if not "_id":0, it would be unsuccess
        {
            "$project": {"nickname": "$user_info.nickname", "signature": "$user_info.signature", "sec_uid": "$user_info.sec_uid", "uid": "$user_info.uid", "avatar_url": {"$arrayElemAt": ["$user_info.avatar_larger.url_list", 0]}, "_id":0}
        }
    ]
    gets = mdb['member'].aggregate(pipeline)
    return [get async for get in gets]


async def GetVideo(page, uids):
    pipeline = []
    pipeline.extend([
        {
            "$project": {"id": "$aweme_id", "vid": "$video.vid", "author_user_id": 1,
                         "author.name": "$author.nickname", "author.unique_id": 1, "author.short_id": "$author_user_id", "author.signature": 1,
                         "author.avatar_url": {"$arrayElemAt": ["$author.avatar_larger.url_list", 0]},
                         "statistic.digg": "$statistics.digg_count", "statistic.play": "$statistics.play_count", "statistic.share": "$statistics.share_count", "statistic.comment": "$statistics.comment_count",
                         "description":"$desc",
                         "text_extra":{"$map": {"input": "$text_extra", "as": "out", "in": "$$out.hashtag_name"}},
                         "origin_cover_urls": "$video.origin_cover.url_list", "dynamic_cover_urls": "$video.dynamic_cover.url_list", "_id": 0,
                         "video_height": "$video.height", "video_width": "$video.width", "video_duration": "$video.duration", "video_ratio": "$video.ratio",
                         "created_at": "$create_time"}
        },
        {
            "$sort": {"created_at": -1}
        },
    ])
    if uids:
        pipeline.append({"$match": {"$or": [{"author.short_id": int(uid)} for uid in uids]}})
    pipeline.extend([
        {
            "$skip": 26 * (page - 1)
        },
        {
            "$limit": 26
        },
    ])
    gets = mdb['video'].aggregate(pipeline)
    return [get async for get in gets]
