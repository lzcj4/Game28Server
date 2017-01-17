import requests


class WebCrawler:
    cookies = None

    def __init__(self):
        pass

    def get(self, url, header=None):
        try:
            r = requests.get(url, cookies=WebCrawler.cookies, proxies=requests.utils.getproxies(), headers=header)
            WebCrawler.cookies = r.cookies
            return r
        except:
            print("发起HTTP请求时出错，被Catch住")
            pass

    def post(self, url, data, header=None):
        try:
            r = requests.post(url, data, cookies=WebCrawler.cookies, proxies=requests.utils.getproxies(), headers=header)
            WebCrawler.cookies = r.cookies
            return r
        except:
                print("发起HTTP请求时出错，被Catch住")
                pass
