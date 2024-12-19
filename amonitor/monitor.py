from bilibili_api import homepage, sync
#
# if __name__ == '__main__':
#     print(sync(homepage.get_videos()))
#
#
# # SESSDATA
# # 30093723%2C1749870009%2C63417%2Ac1CjAPtgnv0ZJPvuJb39dyCoUBcp_MBSjGDvHmyrPJ2X9w36Bad5L3XvITt-5ZJWkHTiMSVkFJelZlSjR4eU8ydDg4anZHa2Q0UXpPcHlLOHFyaWM1YmVnNHJOaVdFM09OdjRCQWZlb2ptUTRYcGVfSzBPalRKUFFQNTFiQ3d4Y2NBcElPbVBjbVp3IIEC
# # bili_jct
# # 025567f76536d7d777d9c34f5c4124eb


import asyncio
from bilibili_api import video


async def main() -> None:
    # 实例化 Video 类
    v = video.Video(bvid="BV1uv411q7Mv")
    # 获取信息
    info = await v.get_info()
    # 打印信息
    print(info)


import asyncio
from bilibili_api import video, Credential

async def main() -> None:
    # 实例化 Credential 类
    SESSDATA = "30093723%2C1749870009%2C63417%2Ac1CjAPtgnv0ZJPvuJb39dyCoUBcp_MBSjGDvHmyrPJ2X9w36Bad5L3XvITt-5ZJWkHTiMSVkFJelZlSjR4eU8ydDg4anZHa2Q0UXpPcHlLOHFyaWM1YmVnNHJOaVdFM09OdjRCQWZlb2ptUTRYcGVfSzBPalRKUFFQNTFiQ3d4Y2NBcElPbVBjbVp3IIEC"
    bili_jct = "025567f76536d7d777d9c34f5c4124eb"
    credential = Credential(sessdata=SESSDATA, bili_jct=bili_jct)
    # 实例化 Video 类
    v = video.Video(bvid="BV1BgSqYvEDU", credential=credential)
    info = await v.get_info()
    print(info)
    # 给视频点赞
    await v.like(True)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


