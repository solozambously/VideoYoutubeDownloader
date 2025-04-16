from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=KG6ft_YDp5k"

yt = YouTube(url, on_progress_callback=on_progress)
streams = yt.streams    
    
audio_streams = []

for stream in streams:
    if stream.mime_type == "audio/mp4":
        audio_streams.append(stream)

best_audio_stream = max(audio_streams, key=lambda a: int(a.abr.replace('kbps', '').strip()))
best_audio_tag = best_audio_stream.itag
print(f"Meilleur stream audio : {best_audio_tag}")