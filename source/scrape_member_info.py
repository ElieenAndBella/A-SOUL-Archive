#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:11:56 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sat May 21 2022
# Modified By: ZhanG
###
from loguru import logger
from source.client import client
from util.const import AvA, Bella, Carol, Diana, Elieen, Acao

async def Scrape():
    asoul = [AvA, Bella, Carol, Diana, Elieen, Acao]
    for sid in asoul:
        try:
            resp = await client.get(f"https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={sid}")
            logger.info(resp.json())
            if resp.status_code // 100 != 2:
                raise 
        except:
            logger.error("There is something wrong. skip.")
            continue
