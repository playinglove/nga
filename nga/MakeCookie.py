# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = open("cookie.txt", "r").read()
    # cookie = "UM_distinctid=1635d9d13c777b-03b66611879fa-3961430f-144000-1635d9d13c86fe; taihe=bf3d77f557cb44a550bee5d21e74ef34; bbsmisccookies=%7B%7D; CNZZDATA1256638851=674147559-1529645399-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529645399; CNZZDATA1256638828=1589233661-1526543616-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648393; CNZZDATA1256638919=1525469300-1529648646-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648646; CNZZDATA1256638924=312763242-1529646682-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529653575; CNZZDATA1264400273=1988147916-1529650361-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529650361; CNZZDATA1256638887=559896610-1529648818-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529648818; CNZZDATA30043604=cnzz_eid%3D147715379-1526279102-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1529979443; CNZZDATA30039253=cnzz_eid%3D1037247114-1526283838-http%253A%252F%252Fbbs.ngacn.cc%252F%26ntime%3D1529977786; CNZZDATA1256638820=1787913993-1526280324-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529976113; guestJs=1529980732; PHPSESSID=2u02d1bip6oguslklb5bhv0vt4; ngacn0comUserInfo=spring%25B0%25A1%25B0%25A1%25B0%25A1%09spring%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%0939%0939%09%0910%091200%094%090%090%0961_12; ngacn0comUserInfoCheck=3325213a7ec86ffb6cee44228238fd99; ngacn0comInfoCheckTime=1529981284; ngaPassportUid=40755489; ngaPassportUrlencodedUname=spring%25B0%25A1%25B0%25A1%25B0%25A1; ngaPassportCid=Xkc2bbakvmldcuj8u5bdali9p4pbk0h2ns4upk7q; lastvisit=1529981482; lastpath=/read.php?tid=12247684; Hm_lvt_5adc78329e14807f050ce131992ae69b=1529647469,1529909758,1529980014,1529981483; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1529981483; CNZZDATA1256638858=1208637985-1526546744-http%253A%252F%252Fbbs.ngacn.cc%252F%7C1529978881"
    trans = transCookie(cookie)
    print(trans.stringToDict())
