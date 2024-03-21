import os
from pytube import YouTube
from moviepy.editor import *


class YouTubeDownloader:
    def __init__(self, url, qualidade='highest'):
        self.url = url
        self.qualidade = qualidade
        self.youtube = YouTube(url)
        self.video = None
        self.caminho_video = None

    def baixar_video(self):
        print("Iniciando o download do vídeo...")
        # Criar o diretório 'mp4/' se não existir
        if not os.path.exists('mp4/'):
            os.makedirs('mp4/')
        if self.qualidade == 'highest':
            self.video = self.youtube.streams.get_highest_resolution()
        elif self.qualidade == 'lowest':
            self.video = self.youtube.streams.get_lowest_resolution()
        elif self.qualidade == 'medium':
            streams = self.youtube.streams.filter(
                progressive=True, file_extension='mp4')
            streams = sorted(streams, key=lambda s: s.resolution)
            mid_index = len(streams) // 2
            self.video = streams[mid_index]
        else:
            print("Qualidade não reconhecida. Baixando na maior qualidade disponível.")
            self.video = self.youtube.streams.get_highest_resolution()
        self.caminho_video = f'mp4/{self.youtube.title}.mp4'
        self.video.download(filename=self.caminho_video)
        print("Download do vídeo concluído!")

    def converter_video_para_mp3(self):
        print("Iniciando a conversão para mp3...")
        # Criar o diretório 'mp3/' se não existir
        if not os.path.exists('mp3/'):
            os.makedirs('mp3/')
        # Converter o vídeo para mp3
        clip = VideoFileClip(self.caminho_video)
        caminho_audio = f'mp3/{self.youtube.title}.mp3'
        clip.audio.write_audiofile(caminho_audio)
        print("Conversão para mp3 concluída!")
        return caminho_audio

    def excluir_video(self):
        print("Excluindo o arquivo de vídeo...")
        # Excluir o arquivo de vídeo
        os.remove(self.caminho_video)
        print("Arquivo de vídeo excluído!")


# parametro qualidade choices = ['highest', 'lowest', 'medium']


# Baixar em .mp3
downloader = YouTubeDownloader(
    'https://www.youtube.com/watch?v=1wVGCLkT4CM&t=314s')
downloader.baixar_video()
caminho_audio = downloader.converter_video_para_mp3()
downloader.excluir_video()

# # Baixar em .mp4
# downloader = YouTubeDownloader(
#     'https://www.youtube.com/watch?v=kGlSQR_0bwQ')
# downloader.baixar_video()
