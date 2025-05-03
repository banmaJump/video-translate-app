# import os
# from google.cloud import translate_v2 as translate
# from dotenv import load_dotenv

# load_dotenv()

# def translate_text(text, target_language="ja"):
    
#     #Translation APIクライアントのインスタンスを作成。
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result["translatedText"]

# def translate_files_in_directory(input_dir, output_dir):

#     #出力ディレクトリが存在しない場合、作成。
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)

#     for filename in os.listdir(input_dir):
#         if filename.endswith(".txt"):
#             input_filepath = os.path.join(input_dir, filename) #os.path.join() は、ファイルパスを安全に結合するための関数です。 => C:\Users\hase\Desktop\text\input\file1.txt
#             output_filename = "X-" + filename  # ファイル名の冒頭に"X-"を追加
#             output_filepath = os.path.join(output_dir, output_filename)

#             try:
#                 with open(input_filepath, "r", encoding="utf-8") as infile:
#                     text = infile.read()
                
#                 translated_text = translate_text(text)
                
#                 with open(output_filepath, "w", encoding="utf-8") as outfile:
#                     outfile.write(translated_text)
#                 print(f"翻訳完了: {filename}")
            
#             except Exception as e:
#                 print(f"ファイル処理中にエラーが発生しました: {filename}, {e}")


# if __name__ == "__main__":
#     input_directory = os.path.join(os.path.expanduser("~"), "Desktop", "github", "video_translate", "input")
#     output_directory = os.path.join(os.path.expanduser("~"), "Desktop", "github", "video_translate", "output")
    
#     translate_files_in_directory(input_directory, output_directory)