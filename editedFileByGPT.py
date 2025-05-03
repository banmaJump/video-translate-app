# import os
# import openai
# from dotenv import load_dotenv

# # 環境変数のロード
# load_dotenv()

# # OpenAI APIキーの設定
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def translate_text(text, target_language="Japanese"):
#     """テキストを指定された言語に翻訳する"""
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": f"You are a helpful assistant that translates text to {target_language}."
#                 },
#                 {
#                     "role": "user",
#                     "content": text
#                 }
#             ]
#         )
#         return response.choices[0].message['content'].strip()
    
#     except Exception as e:
#         print(f"翻訳中にエラーが発生しました: {e}")
#         return None


# def translate_files_in_directory(input_dir, output_dir):
#     """指定されたディレクトリ内のテキストファイルを翻訳し、結果を別のディレクトリに保存する"""
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for filename in os.listdir(input_dir):
#         if filename.endswith(".txt"):
#             input_filepath = os.path.join(input_dir, filename)
#             output_filepath = os.path.join(output_dir, filename)

#             try:
#                 with open(input_filepath, "r", encoding="utf-8") as infile:
#                     text = infile.read()
                
#                 translated_text = translate_text(text)
                
#                 if translated_text:
#                     with open(output_filepath, "w", encoding="utf-8") as outfile:
#                         outfile.write(translated_text)
#                     print(f"翻訳完了: {filename}")
#                 else:
#                     print(f"翻訳失敗: {filename}")
      
#             except Exception as e:
#                 print(f"ファイル処理中にエラーが発生しました: {filename}, {e}")


# if __name__ == "__main__":
#     input_directory = os.path.join(os.path.expanduser("~"), "Desktop",  "github", "video_translare", "input")
#     output_directory = os.path.join(os.path.expanduser("~"), "Desktop",  "github", "video_translate", "output")
    
#     translate_files_in_directory(input_directory, output_directory)