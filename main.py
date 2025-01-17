from gtts import gTTS
import os
from pydub import AudioSegment
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip, ImageClip, VideoFileClip, concatenate_videoclips
from moviepy.config import change_settings
from PIL import Image, ImageDraw, ImageFont

change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

def text_to_audio(text, lang, filename):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(os.path.join("Audio", filename))
        print(f"Audio saved to: {os.path.join('Audio', filename)}")
    except Exception as e:
        errors.append(f"Error in text_to_audio with {filename}: {e}")

def combine_audio_files(audio_files, output_filename):
    try:
        combined = AudioSegment.empty()
        for file in audio_files:
            audio = AudioSegment.from_mp3(os.path.join("Audio", file))
            combined += audio
            print(f"Added {file} to the combined audio")
        combined.export(os.path.join("Audio", output_filename), format="mp3")
        print(f"Combined audio saved to: {os.path.join('Audio', output_filename)}")
    except Exception as e:
        errors.append(f"Error in combine_audio_files with {output_filename}: {e}")

errors = []
japan_dataset = [{"Body_Parts": [
    { "Japanese": "あたま", "Romaji": "atama", "English": "Head" },
    { "Japanese": "ひたい", "Romaji": "hitai", "English": "Forehead" },
    { "Japanese": "め", "Romaji": "me", "English": "Eye" },
    { "Japanese": "みみ", "Romaji": "mimi", "English": "Ear" },
    { "Japanese": "はな", "Romaji": "hana", "English": "Nose" },
    { "Japanese": "くち", "Romaji": "kuchi", "English": "Mouth" },
    { "Japanese": "あご", "Romaji": "ago", "English": "Chin" },
    { "Japanese": "かた", "Romaji": "kata", "English": "Shoulder" },
    { "Japanese": "うで", "Romaji": "ude", "English": "Arm" },
    { "Japanese": "ほね", "Romaji": "hone", "English": "Bone" },
    { "Japanese": "て", "Romaji": "te", "English": "Hand" },
    { "Japanese": "ゆび", "Romaji": "yubi", "English": "Fingers" },
    { "Japanese": "てくび", "Romaji": "tekubi", "English": "Wrist" },
    { "Japanese": "まゆ", "Romaji": "mayu", "English": "Eyebrow" },
    { "Japanese": "まつげ", "Romaji": "matsuge", "English": "Eyelashes" },
    { "Japanese": "からだ", "Romaji": "karada", "English": "Body" },
    { "Japanese": "あし", "Romaji": "ashi", "English": "Leg" },
    { "Japanese": "あしくび", "Romaji": "ashikubi", "English": "Ankle" },
    { "Japanese": "こし", "Romaji": "koshi", "English": "Waist" },
    { "Japanese": "はだ", "Romaji": "hada", "English": "Skin" },
    { "Japanese": "つめ", "Romaji": "tsume", "English": "Nail" },
    { "Japanese": "ほほ", "Romaji": "hoho", "English": "Cheek" },
    { "Japanese": "くび", "Romaji": "kubi", "English": "Neck" },
    { "Japanese": "むね", "Romaji": "mune", "English": "Chest" },
    { "Japanese": "おなか", "Romaji": "onaka", "English": "Stomach" },
    { "Japanese": "は", "Romaji": "ha", "English": "Teeth" },
    { "Japanese": "くちびる", "Romaji": "kuchibiru", "English": "Lips" },
    { "Japanese": "かみ", "Romaji": "kami", "English": "Hair" }
  ],
  "Daily_Phrases": [
    { "Japanese": "ごちゅうもんは", "Romaji": "gochuumon wa", "English": "Placing an order" },
    { "Japanese": "かしこまりました", "Romaji": "kashikomarimashita", "English": "Confirming an order" },
    { "Japanese": "いただきます", "Romaji": "itadakimasu", "English": "Thank you for the food (Before eating)" },
    { "Japanese": "ごちそうさまでした", "Romaji": "gochisousama deshita", "English": "Thank you for the food (After eating)" },
    { "Japanese": "ただいま", "Romaji": "tadaima", "English": "I am home/I’m back" },
    { "Japanese": "おかえりなさい", "Romaji": "okaerinasai", "English": "Welcome back" },
    { "Japanese": "いってきます", "Romaji": "ittekimasu", "English": "I will go and come" },
    { "Japanese": "いってらっしゃい", "Romaji": "itterasshai", "English": "Yes, you go and come" },
    { "Japanese": "いらっしゃい", "Romaji": "irasshai", "English": "Welcome" },
    { "Japanese": "いらっしゃいませ", "Romaji": "irasshaimase", "English": "Welcome (To customers in a shop, store, etc.)" },
    { "Japanese": "ごめんください", "Romaji": "gomenkudasai", "English": "May I come in?" },
    { "Japanese": "どうぞ おあがりください", "Romaji": "douzo oagari kudasai", "English": "Yes, you may come in" },
    { "Japanese": "いっしょに いかがですか", "Romaji": "issho ni ikaga desu ka", "English": "Won’t you join us?" },
    { "Japanese": "いいえ、ちょっと", "Romaji": "iie, chotto", "English": "It’s a bit difficult" },
    { "Japanese": "だめですか", "Romaji": "dame desu ka", "English": "So, you can’t come?" },
    { "Japanese": "また こんど おねがいします", "Romaji": "mata kondo onegaishimasu", "English": "Please ask me some other time" },
    { "Japanese": "もういっぱい いかがですか", "Romaji": "mou ippai ikaga desu ka", "English": "Would you like to have one more cup?" },
    { "Japanese": "いいえ、けっこう です", "Romaji": "iie, kekkou desu", "English": "Polite way of refusing" },
    { "Japanese": "もういちど おねがいします", "Romaji": "mou ichido onegaishimasu", "English": "Can you repeat one more time?" },
    { "Japanese": "そろそろ しつれいします", "Romaji": "sorosoro shitsurei shimasu", "English": "I’m leaving before you" },
    { "Japanese": "おげんきですか", "Romaji": "ogenki desu ka", "English": "How are you?" },
    { "Japanese": "いいでんきですね", "Romaji": "ii denki desu ne", "English": "Nice weather" }
  ]}]
audio_files = []

for category in japan_dataset:
    for title, phrases in category.items():
        try:
            title_filename = f"{title}_title.mp3"
            text_to_audio(title, 'en', title_filename)
            audio_files.append(title_filename)
            
            for i, phrase in enumerate(phrases):
                english_filename = f"{title}_english_{i}.mp3"
                japanese_filename = f"{title}_japanese_{i}.mp3"
                
                text_to_audio(phrase["English"], 'en', english_filename)
                audio_files.append(english_filename)
                
                text_to_audio(phrase["Japanese"], 'ja', japanese_filename)
                audio_files.append(japanese_filename)
                
                img = Image.new("RGB", (1920, 1080), color="black")
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("YuGothR.ttc", size=100)
                text = f'{phrase["Japanese"]}\n \n{phrase["English"].upper()}'
                bbox = draw.textbbox((0, 0), text, font=font)
                text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
                position = ((1920 - text_width) / 2, (1080 - text_height) / 2)
                draw.multiline_text(position, text, font=font, fill="white")
                img.save("text_image.png")
                audio_clip = AudioFileClip(os.path.join("Audio", japanese_filename))
                clip = ImageClip("text_image.png").set_duration(audio_clip.duration)
                clip = clip.set_audio(audio_clip)
                output_video_japanese = os.path.join("Audio", f"{title}_japanese_{i}.mp4")
                clip.write_videofile(output_video_japanese, fps=24)
        except Exception as e:
            errors.append(f"Error processing {title}: {e}")

for category in japan_dataset:
    for title, phrases in category.items():
        try:
            set_audio_files = [f"{title}_title.mp3"]
            set_video_files = []
            for i in range(len(phrases)):
                set_audio_files.append(f"{title}_english_{i}.mp3")
                set_audio_files.extend([f"{title}_japanese_{i}.mp3"] * 5)
                set_video_files.extend([f"{title}_japanese_{i}.mp4"] * 5)
            
            combine_audio_files(set_audio_files, f"{title}_combined.mp3")
            
            video_clips = [VideoFileClip(os.path.join("Audio", video_file)) for video_file in set_video_files]
            final_video = concatenate_videoclips(video_clips)
            final_video.write_videofile(os.path.join("Audio", f"{title}_combined.mp4"), fps=24)
        except Exception as e:
            errors.append(f"Error combining files for {title}: {e}")

try:
    set_combined_files = [f"{title}_combined.mp3" for category in japan_dataset for title in category.keys()]
    combine_audio_files(set_combined_files, "final_combined_audio.mp3")
except Exception as e:
    errors.append(f"Error combining final audio files: {e}")

# try:
#     set_combined_video_files = [f"{title}_combined.mp4" for category in japan_dataset for title in category.keys()]
#     final_video_clips = [VideoFileClip(os.path.join("Audio", video_file)) for video_file in set_combined_video_files]
#     final_combined_video = concatenate_videoclips(final_video_clips)
#     final_combined_video.write_videofile(os.path.join("Audio", "final_combined_video.mp4"), fps=24)
# except Exception as e:
#     errors.append(f"Error combining final video files: {e}")

for file in set(audio_files):  # Use set to avoid deleting the same file multiple times
    try:
        print(f'{file} deleted')    
        os.remove(os.path.join("Audio", file))
    except Exception as e:
        errors.append(f"Error deleting file {file}: {e}")

for category in japan_dataset:
    for title, phrases in category.items():
        for i in range(len(phrases)):
            try:
                print(f"{title}_japanese_{i}.mp4")    
                os.remove(os.path.join("Audio", f"{title}_japanese_{i}.mp4"))
            except Exception as e:
                errors.append(f"Error deleting file {title}_japanese_{i}.mp4: {e}")

if errors:
    print("\nErrors encountered:")
    for error in errors:
        print(error)
