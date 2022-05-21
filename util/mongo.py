#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 7:56:24 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sat May 21 2022
# Modified By: ZhanG
###
from const import MongoUN, MongoPW, MongoHost
from motor.motor_asyncio import AsyncIOMotorClient

MongoUri = f"mongodb://{MongoUN}:{MongoPW}@{MongoHost}"
mclient = AsyncIOMotorClient(MongoUri)["ASOUL"]

async def find():
    record = mclient['member'].find({})
    print(await record.to_list(length=5))

import asyncio

asyncio.run(find())