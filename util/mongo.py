#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 7:56:24 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sun May 22 2022
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
