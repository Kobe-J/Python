import requests


"""
姚希龙
2020.7.2 
视频爬虫
"""
hd = {
    'Connection': 'keep-alive',
    'Host': 'upos-hz-mirrorkodo.acgvideo.com:443',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

print("开始下载")
url=""
r = requests.get(url, headers=hd, stream=True)
with open('test.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)
print("下载结束")


