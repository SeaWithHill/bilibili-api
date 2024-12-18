"""
bilibili_api.homepage

主页相关操作。
"""

from typing import Union

from .utils.utils import get_api
from .utils.credential import Credential
from .utils.network import Api

API = get_api("homepage")


async def get_top_photo() -> dict:
    """
    获取主页最上方的图像。
    例如：b 站的风叶穿行，通过这个 API 获取的图片就是风叶穿行的图片。

    Returns:
        调用 API 返回的结果。
    """
    api = API["info"]["top_photo"]
    params = {"resource_id": 142}
    return await Api(**api).update_params(**params).result


async def get_links(credential: Union[Credential, None] = None):
    """
    获取主页左面的链接。
    可能和个人喜好有关。

    Args:
        credential (Credential | None): 凭据类

    Returns:
        调用 API 返回的结果
    """
    api = API["info"]["links"]
    params = {"pf": 0, "ids": 4694}
    return await Api(**api, credential=credential).update_params(**params).result


async def get_popularize(credential: Union[Credential, None] = None):
    """
    获取推广的项目。
    (有视频有广告)

    Args:
        credential(Credential | None): 凭据类

    Returns:
        调用 API 返回的结果
    """
    api = API["info"]["popularize"]
    params = {"pf": 0, "ids": 34}
    return await Api(**api, credential=credential).update_params(**params).result


async def get_videos(credential: Union[Credential, None] = None):
    """
    获取首页推荐的视频。

    Args:
        credential (Credential | None): 凭据类

    Returns:
        调用 API 返回的结果
    """
    api = API["info"]["videos"]
    SESSDATA = "30093723%2C1749870009%2C63417%2Ac1CjAPtgnv0ZJPvuJb39dyCoUBcp_MBSjGDvHmyrPJ2X9w36Bad5L3XvITt-5ZJWkHTiMSVkFJelZlSjR4eU8ydDg4anZHa2Q0UXpPcHlLOHFyaWM1YmVnNHJOaVdFM09OdjRCQWZlb2ptUTRYcGVfSzBPalRKUFFQNTFiQ3d4Y2NBcElPbVBjbVp3IIEC"
    BILI_JCT = "025567f76536d7d777d9c34f5c4124eb"
    # 025567f76536d7d777d9c34f5c4124eb
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3="")
    return await Api(**api, credential=credential).result
