#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Sunday, May 22nd 2022, 2:32:22 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sun May 22 2022
# Modified By: ZhanG
###
import time
import asyncio
import functools

from loguru import logger


def async_timeit(func):
    @functools.wraps(func)
    async def inner(*args, **kwargs):
        start = time.time()
        ret = await asyncio.create_task(func(*args, **kwargs))
        end = time.time() - start
        logger.info(f"this functions spend {end} seconds")
        return ret
    return inner

def sync_timeit(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time() - start
        logger.info(f"this functions spend {end} seconds")
        return ret
    return inner
