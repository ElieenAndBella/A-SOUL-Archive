#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Created Date: Thursday, May 23th 2022, 8:27:55 am
# Author: ZhanG
# Github: https://github.com/ElieenAndBella
# -----
# Last Modified: Thu May 26 2022
# Modified By: ZhanG
###
from util.mongo import GetMemberInfo, GetVideo
from pydantic import BaseModel
from typing import Any, List, Union
from fastapi import APIRouter, Request

router = APIRouter()


class Response(BaseModel):
    data: Any


@router.get("/members", response_model=Response)
async def GetMembers():
    return Response(data=await GetMemberInfo())


@router.get("/videos", response_model=Response)
async def GetVideoList(request: Request, page: Union[int, None] = None, keyword: Union[str, None] = None):
    return Response(data=await GetVideo(page, request.query_params.getlist("uid")))
