from pydub import AudioSegment

audio = AudioSegment.from_file(r"/home/zob/projects/yt_downloader_api/VideoYoutubeDownloader/test/test.m4a")
audio.export(r"/home/zob/projects/yt_downloader_api/VideoYoutubeDownloader/test/test.mp3", format="mp3")