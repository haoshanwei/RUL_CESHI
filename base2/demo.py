import requests



class RunMain:
    def send_get(self, url, data, header):
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data, header):
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None, header=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res

