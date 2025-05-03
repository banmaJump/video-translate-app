from flask import request, jsonify, render_template
from flaskr import app 
# from process_video import download_youtube_audio, transcribe_audio 
import os

@app.route('/')
def index():
    return render_template('todos.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL がありません'}), 400

    output_filename = "index.mp3"
    new_mp3_file, base_mp3_file = download_youtube_audio(url, output_filename)

    if new_mp3_file and base_mp3_file:
        transcript_data = transcribe_audio(new_mp3_file, model_size="base")
        os.remove(new_mp3_file)
        full_text = transcript_data["text"]

        base_txt = f"{base_mp3_file}.txt"
        try:
            with open(base_txt, "w", encoding="utf-8") as f:
                f.write(full_text)

            text_content = ""
            if os.path.exists(base_txt):
                with open(base_txt, "r", encoding="utf-8") as f:
                    text_content = f.read()
                os.remove(base_txt)
            else:
                print(f"エラー: テキストファイル {base_txt} が見つかりませんでした。")

            return jsonify({'text': text_content})
        except Exception as e:
            print(f"エラー: テキストファイルの書き込みまたは読み込み中にエラーが発生しました: {e}")
            return jsonify({'error': 'テキスト処理中にエラーが発生しました'}), 500
    else:
        return jsonify({'error': f'{url} の処理に失敗しました'}), 500

if __name__ == "__main__":
    # 簡単なテスト
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # 例
    output_file, base_name = download_youtube_audio(url, "test_audio.mp3")
    if output_file:
        print(f"音声ファイルが保存されました: {output_file}, ベース名: {base_name}")
        transcript = transcribe_audio(output_file)
        print("文字起こし結果:")
        print(transcript["text"])
        os.remove(output_file) # テスト後にファイルを削除
    else:
        print("音声ファイルのダウンロードに失敗しました。")