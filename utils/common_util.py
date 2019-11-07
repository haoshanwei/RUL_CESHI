class CommonUtil(object):
    def is_contains(self, expect, reality):
        flag = None
        print(type(expect))
        print(reality)
        if expect == reality["code"]:
            flag = True
        else:
            flag = False
        return flag