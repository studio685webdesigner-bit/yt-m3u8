import os
import subprocess

# Enlace de Crónica TV en vivo que agregaste
YOUTUBE_URL = "https://youtube.com"

try:
    # Comando optimizado para extraer el formato HLS nativo de YouTube
    comando = ["yt-dlp", "-f", "b", "-g", YOUTUBE_URL]
    url_m3u8 = subprocess.check_output(comando).decode("utf-8").strip()
    
    # Validamos que se haya extraído algo para evitar archivos vacíos
    if "http" in url_m3u8:
        contenido_m3u = f"#EXTM3U\n#EXT-X-VERSION:3\n#EXTINF:-1, Cronica TV en Vivo\n{url_m3u8}\n"
        with open("live.m3u8", "w", encoding="utf-8") as f:
            f.write(contenido_m3u)
        print("Archivo live.m3u8 generado con exito.")
    else:
        print("Error: No se pudo obtener una URL valida.")

except Exception as e:
    print(f"Error en la extraccion: {e}")
