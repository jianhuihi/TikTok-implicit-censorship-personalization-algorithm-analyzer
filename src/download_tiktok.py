def download_tiktok_from_url(url, api, output_fp=None):
    video = api.get_video_by_download_url(url)
    if output_fp:
        f = open(output_fp, "wb")
        f.write(video)
        f.close()
    else:
        return video
