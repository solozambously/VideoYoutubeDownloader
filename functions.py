from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment

def download_audio_m4a(url, tag):
    yt = YouTube(url, on_progress_callback=on_progress)
    print('Téléchargement en cours de : ', yt.title)

    ys = yt.streams.get_by_itag(tag)
    ys.download(output_path="./audio/m4a")
    
def convert_m4a_to_mp3(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    title = yt.title
    
    audio = AudioSegment.from_file(f'./audio/m4a/{title}.m4a', format="m4a")
    audio.export(f'./audio/{title}.mp3', format="mp3")
    
def determinate_best_audio_stream(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    streams = yt.streams
    
    audio_streams = []
    
    for stream in streams:
        if stream.mime_type == "audio/mp4":
            audio_streams.append(stream)

    best_audio_stream = max(audio_streams, key=lambda a: int(a.abr.replace('kbps', '').strip()))
    best_audio_tag = best_audio_stream.itag
    return best_audio_tag