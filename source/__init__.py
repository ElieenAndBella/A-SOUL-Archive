#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Saturday, May 21st 2022, 5:15:06 pm
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Sat May 21 2022
# Modified By: ZhanG
###
from .scrape_video import Scrape as sv
from .scrape_member_info import Scrape as smi

ScrapeType = {
    "scrape_video": sv,
    "scrape_member_info": smi
}
