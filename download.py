import os
import youtube_dl

from conf import ydl_opts


def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=False)
        return result['url']
