import os
import subprocess

# REEMPLAZA ESTE ENLACE POR TU CANAL DE YOUTUBE O VIDEO EN VIVO
YOUTUBE_URL = "https://www.youtube.com/watch?v=JC7f3EUDaqw"

try:
    # Ejecuta yt-dlp para obtener la URL del manifiesto m3u8
    comando = ["yt-dlp", "-g", YOUTUBE_URL]
    url_m3u8 = subprocess.check_output(comando).decode("utf-8").strip()
    
    # Genera el contenido del archivo M3U8 formateado correctamente
    contenido_m3u = f"#EXTM3U\n#EXT-X-VERSION:3\n#EXTINF:-1, Mi Transmision en Vivo\n{url_m3u8}\n"
    
    # Guarda el archivo en el repositorio
    with open("live.m3u8", "w", encoding="utf-8") as f:
        f.write(contenido_m3u)
    print("Archivo live.m3u8 generado con exito.")

except Exception as e:
    print(f"Error al extraer el directo: {e}")
