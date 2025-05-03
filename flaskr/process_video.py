import yt_dlp
import whisper
import os

def download_youtube_audio(url: str) -> tuple[str | None, str | None]:
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_filepath = ydl.prepare_filename(info)
            base, _ = os.path.splitext(downloaded_filepath)
            base5 = base[:5]
            audio_filepath = base + ".mp3"
            output_filepath = base5 + ".mp3"
            if os.path.exists(audio_filepath):
                os.rename(audio_filepath, output_filepath)
                return output_filepath, base5 #ゴール：完成した5文字のmp3ファイル、拡張子なしのファイル名。
            else:
                print(f"エラー: 音声ファイル {audio_filepath} が見つかりませんでした。MP3ファイルの生成に失敗した可能性があります。")
                return None, None
    except Exception as e:
        print(f"エラー: YouTubeのダウンロード中にエラーが発生しました: {e}")
        return None, None
    
def transcribe_audio(audio_filepath: str, model_size="base"):
    model = whisper.load_model(model_size)
    transcript_data = model.transcribe(audio_filepath)
    return transcript_data