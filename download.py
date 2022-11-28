import sys
from pytube import YouTube,Playlist
from tqdm import tqdm
import getpass

class video:
    def __init__(self,link):
        self.link = link
        self.youtube = None
        try:
            self.youtube = YouTube(link)
        except Exception:
            print("[ON CLASS video] --> Erro ao tentar acessar o link")
            return None
    
    def resolutions(self):
        if self.youtube:
            formatos = self.youtube.streaming_data['formats']
            qualidades = []
            for format in formatos:
                resolution = format['qualityLabel']
                if resolution not in qualidades:
                    qualidades.append(resolution)

            return qualidades
    
    def baixar(self,qualidade):
        try:
            self.youtube.streams.get_by_resolution(qualidade).download(fr"C:\Users\{getpass.getuser()}\Videos")
            return True,1
        except Exception:
            print(f"\nO Vídeo: {self.youtube.title} não foi baixado")
            print("[ON FUNCTION baixar] --> Erro ao tentar efetuar o download do link (Pode ser que a resolução não seja suportada no download do vídeo)")
            return False,1

class playlist:
    def __init__(self,link):
        self.links = Playlist(link)
        self.videos = [video(adress) for adress in self.links]
    
    def resolutions(self):
        resolucoes = [vid.resolutions() for vid in self.videos]
        resoluts = set()
        opcoes = []
        saida = []
        for resolut in resolucoes:
            for resol in resolut:
                resoluts.add(resol)
                opcoes.append(resol)
        for resol in resoluts:
            if opcoes.count(resol) == len(self.links):
                saida.append(resol)
        return saida
    
    def baixar(self,qualidade):
        valores = []
        for video in tqdm(self.videos):
            valores.append(video.baixar(qualidade)[0])
        return valores.count(True),len(self.links)