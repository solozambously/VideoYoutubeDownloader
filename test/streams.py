from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input('Entrez l\'URL de la vidéo YouTube : ')

yt = YouTube(url, on_progress_callback=on_progress)
streams = yt.streams

# Séparer les streams vidéo et audio
video_streams = []
audio_streams = []

for stream in streams:
    if stream.mime_type == "video/mp4":
        video_streams.append(stream)
    elif stream.mime_type == "audio/mp4":
        audio_streams.append(stream)

print("\n🎬 Streams vidéo disponibles :")
for v in video_streams:
    print(f"- itag={v.itag}, type={v.mime_type}, res={v.resolution}, fps={v.fps}, vcodec={v.video_codec}, progressive={v.is_progressive}")

print("\n🎧 Streams audio disponibles :")
for a in audio_streams:
    print(f"- itag={a.itag}, type={a.mime_type}, abr={a.abr}, acodec={a.audio_codec}")