#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:04:48 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sat May 21 2022
# Modified By: ZhanG
###
from source import ScrapeType
from fastapi import FastAPI

app = FastAPI()

@app.get("/invoke")
async def scrape(type: str, key: str):
    if key != "e10adc3949ba59abbe56e057f20f883e":
        return {
            "status": "Something may be wrong"
        }
    await ScrapeType[type]()
    return {
        "status": "I'm Scraping"
    }

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('app:app', host='0.0.0.0', port=9008)
