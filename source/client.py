#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:14:41 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sun May 22 2022
# Modified By: ZhanG
###
import httpx
from util.const import UserAgent

transport = httpx.AsyncHTTPTransport(retries=2)
client = httpx.AsyncClient(transport=transport, headers={"User-Agent": UserAgent})
