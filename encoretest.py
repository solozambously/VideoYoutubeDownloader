# Prérequis 
# Python 3 avec pip d'installez
# Installe pytube (pip install pytube) ou si erreur (pip3 install pytube)
#
#By SoloZambously
#Python3

from pytube import YouTube
print("__   __         _____      _            __  __ ____  _  _")                          
print("\ \ / /__  _   |_   _|   _| |__   ___  |  \/  |  _ \| || |")                         
print(" \ V / _ \| | | || || | | | '_ \ / _ \ | |\/| | |_) | || |_")                        
print("  | | (_) | |_| || || |_| | |_) |  __/_| |  | |  __/|__   _|")                       
print("  |_|\___/ \__,_||_| \__,_|_.__/ \___(_)_|  |_|_|      |_|")                         

print("______   __  ____        _      _____               _                     _")       
print("| __ ) \ / / / ___|  ___ | | ___|__  /__ _ _ __ ___ | |__   ___  _   _ ___| |_   _") 
print("|  _ \\\ V /  \___ \ / _ \| |/ _ \ / // _` | '_ ` _ \| '_ \ / _ \| | | / __| | | | |")
print("| |_) || |    ___) | (_) | | (_) / /| (_| | | | | | | |_) | (_) | |_| \__ \ | |_| |")
print("|____/ |_|   |____/ \___/|_|\___/____\__,_|_| |_| |_|_.__/ \___/ \__,_|___/_|\__, |")
print("                                                                              |___/") 

print('Bienvenue')
print('Téléchargez gratuitement une vidéo YouTube avec seulement un lien !')
print('Create By SoloZambously')

url_input = input('Entrez l\'url de votre vidéo : ')
url = YouTube(url_input)
# url.register_on_progress_callback(on_download_progress)
print("Vous téléchargez : ", url.title)
# print(url.streams)
stream = url.streams.first()
stream.download()
print("Votre fichier à bien été téléchargez !")



# [<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="25fps" vcodec="avc1.640020" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400b" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
