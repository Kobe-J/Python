import requests
import json

# 下载图片
url = "http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E5%A3%81%E7%BA%B8&tag=%E6%B8%B8%E6%88%8F&start=0&len=15&width=1366&height=768"
url1 = ""
r = requests.get(url)
data = json.loads(r.text)
print(data)
img_url = []
for i in data["all_items"]:
    img_url.append(i["pic_url"])

for a in range(len(img_url)):
    with open("/SourceTree/img/%s" % img_url[a][-10:] + ".jpg", "wb") as f:
        r2 = requests.get(img_url[a])
        f.write(r2.content)
        print("下载完毕：", img_url[a])
