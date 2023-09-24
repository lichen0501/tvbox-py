from functools import cache
import requests
from fastapi import FastAPI, Response
from urllib.parse import urlsplit

app = FastAPI()
url = 'https://alist.lichen.run/d/应用/android/tv/tvbox.txt'
api_url = ''

# 获取tvbox接口
@app.get("/")
async def root():
    return Response(content=get_api(), media_type="text/html")

# 更新api缓存
@app.get("/update")
async def root():
    get_api.cache_clear()
    get_api()
    return 'api_url:' + api_url

@cache
def get_api():
    global api_url
    api_url = get_api_url()
    resp = requests.get(api_url)
    content = resp.text
    domain = urlsplit(api_url).hostname
    scheme = urlsplit(api_url).scheme
    new_url = scheme + '://' + domain + '/'
    content = content.replace('./', new_url)
    return content

# 从远程地址或者api地址
def get_api_url():
    resp = requests.get(url)
    content = resp.text
    print(content)
    return content
    
