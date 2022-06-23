# A-SOUL Archive

**_Just for A-SOUL ♡_**

## **|** **Project Detail**

Language: Python, Javascript  
Farmework: Fastapi, Vue2  
Database: MongoDB

**Crawlers are written based on HTTPX, all written asynchronously.**

## **|** **Project Tree**

```
├── LICENSE
├── README.md
├── __pycache__
│   ├── app.cpython-38.pyc
│   └── main.cpython-38.pyc
├── app.py
├── router
│   ├── __init__.py
│   ├── __pycache__
│   └── v1.py
├── source
│   ├── __init__.py
│   ├── __pycache__
│   ├── client.py
│   ├── scrape_member_info.py
│   └── scrape_videos.py
├── util
│   ├── __init__.py
│   ├── __pycache__
│   ├── const.py
│   ├── mongo.py
│   └── timeit.py
├── venv
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
└── website
    ├── babel.config.js
    ├── dist
    ├── node_modules
    ├── package-lock.json
    ├── package.json
    ├── public
    ├── src
    └── vue.config.js
```

## **|** **Douyin API**

### User Information Interface

> URL: https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid=xxx
>
> - Method: GET
>   > - Params
>   >   > - sec_uid

### Video List Interface

> URL: https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=xxx&count=xxx&max_cursor=xxx&_signature=xxx
>
> - Method: GET
>   > - Params:
>   >   > - sec_uid
>   >   > - count: refer to the number of video
>   >   > - max_cursor: means next page
>   >   > - \_signature: may be abandoned

### Video Information Interface

> URL: https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=xxx&_signature=xxx
>
> - Method: GET
>   > - Params:
>   >   > - item_ids: video's ID
>   >   > - \_signature: may be abandoned

# **License**

MIT

# **Thanks**

https://github.com/asoul-sig/asoul-video 修改了并使用了前端代码
