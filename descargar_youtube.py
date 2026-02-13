import sys
import subprocess
import os

# Preferir pasar la URL como argumento: python3 descargar_youtube.py <URL>
video_url = ""
if len(sys.argv) > 1:
    video_url = sys.argv[1].strip()
else:
    video_url = input("Introduce la URL del video de YouTube: ").strip()

if not video_url:
    print("No se proporcionó ninguna URL. Uso: python3 descargar_youtube.py <URL>")
    sys.exit(1)

# Ruta de salida
out_path = '/home/radukai/Música/youtube'  # cambia si quieres otra ruta

# Crear carpeta si no existe
os.makedirs(out_path, exist_ok=True)

try:
    # Usar yt-dlp para descargar solo audio en mp3
    command = [
        'yt-dlp',
        '-x',
        '--audio-format', 'mp3',
        '--audio-quality', '192',
        '-o', os.path.join(out_path, '%(title)s.%(ext)s'),
        video_url
    ]
    
    print(f"Descargando audio de: {video_url}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✓ Audio descargado correctamente en: {out_path}")
    else:
        print("Error al descargar:")
        print(result.stderr)
except FileNotFoundError:
    print("Error: yt-dlp no está instalado.")
    print("Instálalo con: pip install yt-dlp")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)