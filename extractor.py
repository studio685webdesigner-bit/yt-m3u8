import os
import subprocess

YOUTUBE_URL = "https://youtube.com"

try:
    # Forzamos a yt-dlp a extraer estrictamente el formato m3u8 nativo de los servidores de Google
    comando = ["yt-dlp", "-f", "22/95/94/93/b", "-g", YOUTUBE_URL]
    url_m3u8 = subprocess.check_output(comando).decode("utf-8").strip()
    
    if "http" in url_m3u8:
        # Estructura limpia que cualquier reproductor IPTV y VLC lee de inmediato
        contenido_m3u = f"#EXTM3U\n#EXTINF:-1, Cronica TV En Vivo\n{url_m3u8}\n"
        with open("live.m3u8", "w", encoding="utf-8") as f:
            f.write(contenido_m3u)
        print("Archivo live.m3u8 reescrito con exito.")
    else:
        print("Error: Formato no compatible.")

except Exception as e:
    print(f"Error en la extraccion: {e}")
