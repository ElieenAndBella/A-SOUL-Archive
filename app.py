#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:04:48 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Wed May 25 2022
# Modified By: ZhanG
###
import asyncio

from loguru import logger
from typing import Union

from source import ScrapeType
from fastapi import FastAPI, Request

from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = FastAPI()


@app.on_event("startup")
async def sched():
    # Set maximum concurrency
    app.state.sema = asyncio.Semaphore(6)
    try:
        scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')

        # scheduler.add_job(ScrapeType["scrape_videos"], trigger="interval", seconds=30)
        scheduler.add_job(ScrapeType["scrape_videos"], args=[app.state.sema],
                          trigger="cron", hour=12, minute=30)

        scheduler.start()
        logger.info("scheduler started")
    except Exception as e:
        logger.error(f"exception={e}")


@app.get("/invoke")
async def scrape(request: Request, type: str, key: Union[str, None] = None):
    if key is None or key != "e10adc3949ba59abbe56e057f20f883e":
        return {
            "status": "Something may be wrong"
        }
    try:
        await ScrapeType[type](request.app.state.sema)
    except KeyError:
        return {
            "status": "Type is wrong"
        }
    return {
        "status": "I'm Scraping"
    }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='0.0.0.0', port=9008)
