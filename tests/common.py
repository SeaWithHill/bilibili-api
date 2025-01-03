
from bilibili_api import Credential, login
import os

from bilibili_api import Credential


def get_credential():
    BILI_SESSDATA = os.getenv("BILI_SESSDATA")
    BILI_CSRF = os.getenv("BILI_CSRF")
    BILI_BUVID3 = os.getenv("BILI_BUVID3")
    BILI_DEDEUSERID = os.getenv("BILI_DEDEUSERID")

    BILI_SESSDATA = "30093723%2C1749870009%2C63417%2Ac1CjAPtgnv0ZJPvuJb39dyCoUBcp_MBSjGDvHmyrPJ2X9w36Bad5L3XvITt-5ZJWkHTiMSVkFJelZlSjR4eU8ydDg4anZHa2Q0UXpPcHlLOHFyaWM1YmVnNHJOaVdFM09OdjRCQWZlb2ptUTRYcGVfSzBPalRKUFFQNTFiQ3d4Y2NBcElPbVBjbVp3IIEC"
    BILI_CSRF = "025567f76536d7d777d9c34f5c4124eb"
    BILI_BUVID3 = ""
    BILI_DEDEUSERID = ""
    os.environ["BILI_SESSDATA"] = BILI_SESSDATA
    os.environ["BILI_CSRF"] = BILI_CSRF

    # if not BILI_SESSDATA or not BILI_CSRF or not BILI_BUVID3 or not BILI_DEDEUSERID:
    #     print(Exception("缺少环境变量"))
    #     cred = login.login_with_qrcode_term()
    #     os.environ["BILI_SESSDATA"] = cred.sessdata
    #     os.environ["BILI_CSRF"] = cred.bili_jct
    #     os.environ["BILI_BUVID3"] = cred.buvid3
    #     os.environ["BILI_DEDEUSERID"] = cred.dedeuserid
    #     BILI_SESSDATA = os.getenv("BILI_SESSDATA")
    #     BILI_CSRF = os.getenv("BILI_CSRF")
    #     BILI_BUVID3 = os.getenv("BILI_BUVID3")
    #     BILI_DEDEUSERID = os.getenv("BILI_DEDEUSERID")

    return Credential(BILI_SESSDATA, BILI_CSRF, BILI_BUVID3, BILI_DEDEUSERID)
