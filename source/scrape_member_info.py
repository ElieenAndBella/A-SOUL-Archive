#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:11:56 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sun May 22 2022
# Modified By: ZhanG
###
import asyncio
from loguru import logger
from source.client import client
from util.const import AvA, Bella, Carol, Diana, Elieen, Acao
from util.mongo import MemberUpdate
from util.timeit import async_timeit

asoul = [AvA, Bella, Carol, Diana, Elieen, Acao]

@async_timeit
async def Scrape():
    tasks = []
    for sid in asoul:
        tasks.append(asyncio.create_task(_scrape_member_info(sid)))
    await asyncio.wait(tasks)


async def _scrape_member_info(sec_uid: str):
    try:
        resp = await client.get(f"https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={sec_uid}")
        await MemberUpdate(sec_uid, resp.json())
        logger.info(f"Member Info sec_uid={sec_uid}")
        if resp.status_code // 100 != 2:
            raise
    except Exception as e:
        logger.error(
            f"There is something wrong. skip. sec_uid={sec_uid} exception={e}")
