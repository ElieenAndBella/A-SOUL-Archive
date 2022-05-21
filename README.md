# **|** **Douyin API**
### User Information Interface
> URL: https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid=xxx
    >>- Method: GET
    >>- Params
        >>>- sec_uid
### Video List Interface
> URL: https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=xxx&count=xxx&max_cursor=xxx&_signature=xxx
    >>+ Method: GET
    >>+ Params:
        >>>- sec_uid
        >>>- count: refer to the number of video
        >>>- max_cursor: means next page
        >>>- _signature: may be abandoned
### Video Information Interface
> URL: https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=xxx&_signature=xxx
    >>+ Method: GET
    >>+ Params:
        >>>- item_ids: video's ID
        >>>- _signature: may be abandoned
