import sys
from pytube import YouTube
from tqdm import tqdm
import os

# Pedir al usuario que ingrese el enlace del video
link = input("Ingresa el enlace del video: ")

# Pedir al usuario que elija la calidad del video
print("Elige la calidad del video (360, 480, 720, 1080): ")
quality = input()

# Mapeo de la calidad a las opciones de pytube
quality_map = {
    "360": "360p",
    "480": "480p",
    "720": "720p",
    "1080": "1080p"
}

# Obtener la URL del video de YouTube
yt = YouTube(link)

# Obtener el objeto stream del video en la calidad especificada
stream = yt.streams.filter(res=quality_map[quality]).first()

# Obtener el nombre del archivo de salida
output_file = f"{yt.title}.mp4"

# Descargar el video
stream.download(output_path='/mnt/c/Users/juand/Videos/Descargas', filename=output_file)
print("Descarga completada.")
