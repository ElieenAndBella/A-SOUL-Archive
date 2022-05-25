#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:12:45 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Wed May 25 2022
# Modified By: ZhanG
###
import asyncio

from loguru import logger
from source.client import client
from util.const import AvA, Bella, Carol, Diana, Elieen, Acao
from util.timeit import async_timeit
from util.mongo import VideoInfoUpdate

once = False
asoul = [AvA, Bella, Carol, Diana, Elieen, Acao]


async def Scrape(sema):
    tasks = []
    for sid in asoul:
        tasks.append(asyncio.create_task(_scrape_video(sid, 0, sema)))
    await asyncio.wait(tasks)


@async_timeit
async def _scrape_video(sec_uid, cursor, sema):
    resp = await client.get(
        f"https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid={sec_uid}&count=50&max_cursor={cursor}")
    try:
        awemes = resp.json()
    except:
        return
    aweme_list = awemes["aweme_list"]
    tasks = []
    for aweme in aweme_list:
        tasks.append(asyncio.create_task(
            _scrap_video_info(aweme["aweme_id"], sema)))
    await asyncio.wait(tasks)
    has_more = awemes["has_more"]
    if has_more is False:
        return
    else:
        await _scrape_video(sec_uid, awemes["max_cursor"], sema)


async def _scrap_video_info(aweme_id, sema):
    async with sema:
        try:
            resp = await client.get(f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={aweme_id}")
            item_list = resp.json()["item_list"]
            [await VideoInfoUpdate(item["aweme_id"], item) for item in item_list]
        except Exception as e:
            logger.error(
                f"There is something wrong. skip. aweme_id={aweme_id} exception={e}")
