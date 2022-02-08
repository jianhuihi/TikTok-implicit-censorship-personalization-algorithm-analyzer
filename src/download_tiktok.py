from TikTokApi import TikTokApi
s_v_web_id = "verify_c1470728e338f0cdea062062bad25303"
api = TikTokApi.get_instance(custom_verifyFp=s_v_web_id)

def download_tiktok_from_url(url, output_fp=None):
    video = api.get_video_by_download_url(url)
    if output_fp:
        f = open(output_fp, "wb")
        f.write(video)
        f.close()
    else:
        return video
