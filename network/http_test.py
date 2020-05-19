import requests,bs4,time
from requests.exceptions import ReadTimeout,ConnectTimeout,HTTPError,ConnectionError


def send_http_packet(url):
    requests.packages.urllib3.disable_warnings()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    headers = {'User-Agent': user_agent}
    url = "http://" + url
    response_html= ""
    file = open("http_logs.txt","a")
    try:
        response = requests.get(url, headers)
        response_html = response.content.decode("UTF-8")
        return response_html
    except ReadTimeout:
        print('Read Timeout')
        file.write(time.asctime(time.localtime(time.time())) + " Read Timeout \n")
        file.close()
        return False
    except ConnectTimeout:
        print('Connect Timeout')
        file.write(time.asctime(time.localtime(time.time())) + " Connect Timeout \n")
        file.close()
        return False
    except HTTPError:
        print('HTTP Error')
        file.write(time.asctime(time.localtime(time.time())) + " HTTP Error \n")
        file.close()
        return False
    except ConnectionError:
        print('Connection Error')
        file.write(time.asctime(time.localtime(time.time())) + " Connection Error \n")
        file.close()
        return False

def check_http(url,title):
    html = send_http_packet(url)
    file = open("http_logs.txt","a")
    if html != False  and title != False :
        soup = bs4.BeautifulSoup(html, 'lxml')
        html_title = ""
        html_title = soup.title.text
        if title in html_title:
            return True
        else:
            return False
    else:
        print('html or title is None')
        file.write(time.asctime(time.localtime(time.time())) + " html or title is None \n")
        file.close()
        return False