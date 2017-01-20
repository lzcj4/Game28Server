import requests
import  logging


class WebCrawler:
    cookies = None

    def __init__(self):
        pass

    def get(self, url, header=None):
        try:
            r = requests.get(url, cookies=WebCrawler.cookies, proxies=requests.utils.getproxies(), headers=header)
            WebCrawler.cookies = r.cookies
            return r
        except ConnectionError as  err:
            logging.error("发起HTTP请求时ConnectionError:{}".format(err))
        except requests.HTTPError  as  err:
            logging.error("发起HTTP请求时HTTPError:{}".format(err))
        except requests.TooManyRedirectsError  as  err:
            logging.error("发起HTTP请求时TooManyRedirectsError:{}".format(err))
        except TimeoutError  as  err:
            logging.error("发起HTTP请求时TimeoutError:{}".format(err))
        except Exception as err:
            logging.error("发起HTTP请求时未知异常:{}".format(err))

    def post(self, url, data, header=None):
        try:
            r = requests.post(url, data, cookies=WebCrawler.cookies, proxies=requests.utils.getproxies(),
                              headers=header)
            WebCrawler.cookies = r.cookies
            return r
        except ConnectionError as  err:
            logging.error("发起HTTP请求时ConnectionError:{}".format(err))
        except requests.HTTPError  as  err:
            logging.error("发起HTTP请求时HTTPError:{}".format(err))
        except requests.TooManyRedirectsError  as  err:
            logging.error("发起HTTP请求时TooManyRedirectsError:{}".format(err))
        except TimeoutError  as  err:
            logging.error("发起HTTP请求时TimeoutError:{}".format(err))
        except Exception as err:
            logging.error("发起HTTP请求时未知异常:{}".format(err))
