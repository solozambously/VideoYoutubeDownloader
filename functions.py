from pytubefix import YouTube, Search
from pytubefix.cli import on_progress
from pydub import AudioSegment
import re

def download_audio_m4a(url, tag):
    yt = YouTube(url, on_progress_callback=on_progress)
    print('Téléchargement en cours de : ', yt.title)

    ys = yt.streams.get_by_itag(tag)
    ys.download(output_path="./audio/m4a", filename=f"{clean_filename(yt.title)}.m4a")
    
def convert_m4a_to_mp3(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    title = clean_filename(yt.title)
    
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

def search_video(search):
    """
    Cherche des vidéos sur YouTube en fonction d'un terme de recherche.
    """
    results = Search(str(search))

    videos_data = []
    for video in results.videos:
        video_info = {
            'title': video.title,
            'url': video.watch_url,
            'duration': video.length
        }
        videos_data.append(video_info)
    
    return videos_data

def clean_filename(filename):
    """
    Clean les noms des fichiers pour que ce soit compatible avec les systèmes d'exploitations
    """

    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    
    cleaned_filename = re.sub(invalid_chars, '_', filename)
    cleaned_filename = re.sub(r'\s+', '_', cleaned_filename)
    
    return cleaned_filename