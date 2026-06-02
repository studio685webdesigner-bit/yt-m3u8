import subprocess

YOUTUBE_URL = "https://youtube.com/watch?v=JC7f3EUDaqw"

try:
    # Formato universal nativo para directos en YouTube sin restricciones rígidas
    comando = ["yt-dlp", "-g", YOUTUBE_URL]
    url_m3u8 = subprocess.check_output(comando).decode("utf-8").strip()
    
    if "http" in url_m3u8:
        # Generamos la lista M3U8 clásica
        contenido_m3u = f"#EXTM3U\n#EXTINF:-1, Cronica TV En Vivo\n{url_m3u8}\n"
        with open("live.m3u8", "w", encoding="utf-8") as f:
            f.write(contenido_m3u)
        print("Archivo live.m3u8 creado con éxito.")
    else:
        print("Error: No se obtuvo un flujo HLS válido.")

except Exception as e:
    print(f"Error en la extracción: {e}")
