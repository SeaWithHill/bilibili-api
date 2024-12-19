from bilibili_api import hot, sync

if __name__ == '__main__':
    print(sync(hot.get_hot_videos()))

