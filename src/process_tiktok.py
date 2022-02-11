import os
import speech_recognition as sr

def _download_tiktok_from_url(url, api, output_fp):
    tiktok = api.get_tiktok_by_url(url)
    video_url = tiktok['itemInfo']['itemStruct']['video']['downloadAddr']
    video = api.get_video_by_download_url(video_url)
    
    f = open(output_fp, "wb")
    f.write(video)
    f.close()
    return tiktok


def generate_subtitles(url, api):
    tiktok = _download_tiktok_from_url(url, api, "temp.mp4")

    os.system(f'ffmpeg -i temp.mp4 -q:a 0 -map a temp.wav')
    os.system(f'ffmpeg -i temp.wav -ac 1 mono.wav')
    # Sample rate: 44100 Hz, Sample width: s16
    r = sr.Recognizer()
    with sr.AudioFile("mono.wav") as source:
        audio = r.record(source)
    result = r.recognize_sphinx(audio)

    os.system(f'rm temp.mp4 temp.wav mono.wav')

    return result, tiktok
    
    

    

