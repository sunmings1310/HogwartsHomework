import requests


class BaseApi:

    def send_api(self, req, tools="requests"):
        if tools == "requests":
            return requests.request(**req)