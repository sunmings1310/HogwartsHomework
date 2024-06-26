from api_object.apis.base_api import BaseApi


class WeworkApi(BaseApi):
    def __init__(self):
        self.token = None

    def get_token(self, corpid, corpsecret):
        # return: access_token的值

        # corpid = "ww75abb8519b57cec6"
        # corpsecret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        # url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # param = {
        #     "corpid": corpid,
        #     "corpsecret": corpsecret
        # }
        # 发起get请求
        # res = requests.get(url=url, params=param)
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        res = self.send_api(req)
        self.token = res.json()["access_token"]

if __name__ == '__main__':
    wa = WeworkApi()
    wa.get_token('a','b')