import requests

from amonitor.RenderTemplate import export_ups_list_md
from bilibili_api.dynamic import Dynamic
import asyncio
from bilibili_api import dynamic,Credential
import asyncio
from bilibili_api import dynamic,video, Credential
from loguru import logger

SESSDATA = "30093723%2C1749870009%2C63417%2Ac1CjAPtgnv0ZJPvuJb39dyCoUBcp_MBSjGDvHmyrPJ2X9w36Bad5L3XvITt-5ZJWkHTiMSVkFJelZlSjR4eU8ydDg4anZHa2Q0UXpPcHlLOHFyaWM1YmVnNHJOaVdFM09OdjRCQWZlb2ptUTRYcGVfSzBPalRKUFFQNTFiQ3d4Y2NBcElPbVBjbVp3IIEC"
BILI_JCT = "025567f76536d7d777d9c34f5c4124eb"
BUVID3 = "7DFC1389-BD13-BE5B-A327-3BF74019EAA772367infoc"

async def blibliDynamic():
    # 实例化 Credential 类
    credential = Credential(sessdata=SESSDATA, bili_jct=BILI_JCT, buvid3="")
    # 实例化 Dynamic 类
    list = await dynamic.get_dynamic_page_info(credential=credential)
    for e in list:
        print(e.get_dynamic_id())
    dict = await dynamic.get_dynamic_page_UPs_info(credential=credential)
    upList = dict.get("up_list")
    for f in upList:
        logger.info('up主 {upName}, 是否已经更新 {isUpdate}'.format(upName = f.get("uname"), isUpdate = f.get("has_update")))
    return upList

if __name__ == '__main__':
    logger.add("../log/blibli.log", rotation="1 MB", compression="zip")
    # 1.生成更新列表信息
    upsList =  asyncio.get_event_loop().run_until_complete(blibliDynamic())
    # 2.生成每日阅读列表
    export_ups_list_md('D:\\Users\\mabf\\PycharmProjects\\bilibili-api\\templates\\',upsList,'D:\\obsidian\\vue_expert\\howtobeavueexport\\D-Diary日记\\2025\\')

