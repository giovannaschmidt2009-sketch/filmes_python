import yt_dlp
import os


def baixar(url, tipo):
    # Cria a pasta 'Downloads' se não existir
    if not os.path.exists('Downloads'):
        os.makedirs('Downloads')

    # Configuração base
    opcoes = {
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
    }

    if tipo == '1':
        # Configuração para VÍDEO (MP4)
        opcoes['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        print("\n🎬 Modo selecionado: VÍDEO (MP4)")
    else:
        # Configuração para ÁUDIO (MP3)
        opcoes['format'] = 'bestaudio/best'
        opcoes['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        print("\n🎵 Modo selecionado: ÁUDIO (MP3)")

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print(f"\n✅ Concluído! Verifique a pasta 'Downloads'.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    print("=== baixador para youtube (MP4/MP3) ===")
    url = input("Cole o link do YouTube: ").strip()

    print("\nComo deseja baixar?")
    print("1 - Vídeo (MP4)")
    print("2 - Áudio (MP3)")
    escolha = input("Digite 1 ou 2: ")

    if url and escolha in ['1', '2']:
        baixar(url, escolha)
    else:
        print("Opção ou URL inválida.")
