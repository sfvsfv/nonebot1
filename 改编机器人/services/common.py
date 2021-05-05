import httpx
from httpx import AsyncClient, HTTPError

from services.log import logger

UserAgent = "box-s-ville.Saiki"


class ServiceException(Exception):
    'Base of exceptions thrown by the services side'

    def __init__(self, message: str) -> None:
        super().__init__(message)

    @property
    def message(self) -> str:
        return self.args[0]


async def fetch_text(uri: str) -> str:
    async with AsyncClient(headers={'User-Agent': UserAgent}
                           ) as client:
        try:
            res = await client.get(uri)
            res.raise_for_status()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('API 服务目前不可用')
        return res.json()


async def fetch_wall_url(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            result = resp.json()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取图片地址失败')
        return result['images'][0]['url']


async def get_wall_content(url: str):
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            content_url = await fetch_wall_url(url)
            resp = await client.get("https://www.bing.com" + content_url)
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取图片失败')
        return resp.content


async def fetch_wikipedia(url: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url)
            resp.raise_for_status()
            result = resp.json()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取百科失败')
        return result['data']


async def get_wikipedia_text(url: str):
    try:
        data = await fetch_wikipedia(url)
        res = []
        if data['content'] == '':
            msg = '==未找到该词条=='
            res.append(msg)
        else:
            msg = data['content']
            img = data['ImgUrl']
            res.append(msg)
            res.append(img)

    except HTTPError as e:
        logger.exception(e)
        raise ServiceException('获取整合百科失败')
    return res


async def fetch_set_data(url: str) -> str:
    async with httpx.AsyncClient(headers={
        "r18": "2",
        "size1200": "true",
        "user-agent": UserAgent
    }, proxies={"http": "https://www.pixiv.net"}) as client:
        try:
            resp = await client.get(url)
            result = resp.json()
            data = result['data'][0]
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('获取setu失败')
        return data


async def get_setu_data(url: str):
    async with httpx.AsyncClient(headers={
        "r18": "2",
        "size1200": "true",
        "user-agent": UserAgent
    }, proxies={"http": "https://www.pixiv.net"}) as client:
        try:
            data = await fetch_set_data(url)
            msg = "pid:" + str(data['pid']) + "\n" + "title:" + data['title'] + "\n" \
                  + "author:" + data['author'] + "\n" + "url:" + data['url'] + "\n" + \
                  "tags:" + str(data['tags'])
            imgUrl = data['url']
            result = []
            result.append(msg)
            result.append(imgUrl)
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('setu——msg整合失败')
        return result


async def get_joke_data(url: str) -> str:
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            result = data['data']['content']
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('jokeAPI暂不可用')
        return result


async def get_zhTop_data(url: str) -> str:
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            result = data['list']
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('知乎热搜API暂不可用')
        return result


async def get_garbageSort_data(url: str) -> str:
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            result = data['data']
            msg = result['Name'] + '属于' + result['Type'] + '\n' + result['Description']['Concept'] + '\n' + result[
                'Type'] + '包含：' + result['Description']['Including'] + '\n' + '处理方法：' + result['Description'][
                      'Release_requirement']
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('知乎热搜API暂不可用')
        return msg


async def translate(keyword: str) -> str:
    async with httpx.AsyncClient(headers={'User-Agent': UserAgent}) as client:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        key = {
            'type': "AUTO",
            'i': keyword,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON",
            "typoResult": "true"
        }
        try:
            resp = await client.post(url, data=key)
            data = resp.json()
        except HTTPError as e:
            logger.exception(e)
            raise ServiceException('知乎热搜API暂不可用')
        return data['translateResult'][0][0]['tgt']


async def get_music_id(song: str) -> int:
    url = 'http://47.112.23.238/Music/getMusicList'
    headers = {'User-Agent': UserAgent}
    data = {
        "musicName": song,
        "type": "netease",
        "number": "5"
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, headers=headers, data=data)
        id = resp.json()['data'][0]['id']
        return id


async def get_yiyan_data(url: str) -> str:
    headers = {'User-Agent': UserAgent}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        data = resp.json()['data']
        msg = data['constant'] + ' --' + data['source']
        return msg


async def get_caihong_data(url: str) -> str:
    headers = {'User-Agent': UserAgent}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        data = resp.json()['data']
        msg = data['comment']
        return msg
