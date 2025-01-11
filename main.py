from googletrans import Translator
from gtts import gTTS
import os
from pydub import AudioSegment

def english_to_japanese_audio(english_text, filename="japanese_audio.mp3"):
    try:
        # Translate English to Japanese
        translator = Translator()
        japanese_text = translator.translate(english_text, dest='ja').text

        # Convert Japanese text to speech
        tts = gTTS(text=japanese_text, lang='ja')

        # Save the audio to a file
        tts.save(filename)
        print(f"Audio saved to: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

def english_to_uk_audio(english_text, filename="uk_audio.mp3"):
    try:
        # Convert English text to speech with UK accent
        tts = gTTS(text=english_text, lang='en', tld='co.uk')

        # Save the audio to a file
        tts.save(filename)
        print(f"Audio saved to: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

def combine_audio_files(audio_files, output_filename):
    combined = AudioSegment.empty()
    for file in audio_files:
        audio = AudioSegment.from_mp3(file)
        combined += audio
    combined.export(output_filename, format="mp3")
    print(f"Combined audio saved to: {output_filename}")

# Example usage
english_sentences_dataset = [{"title":"Months","phrases":["Month before last","Last month","This month","Next month","Month after next"]},{"title":"Weeks","phrases":["Week before last","Last week","This week","Next week","Week after next"]},{"title":"Numbers","phrases":["1","2","3","4","5","6","7","8","9","10","100","1000","10000","100000"]},{"title":"Time","phrases":["1 o'clock","2 o'clock","3 o'clock","4 o'clock","5 o'clock","6 o'clock","7 o'clock","8 o'clock","9 o'clock","10 o'clock","What is the time now?"]},{"title":"Colors","phrases":["Red","Blue","White","Black","Brown","Green","Purple","Yellow","Gold","Silver","Grey","Navy blue","Pink","Orange"]},{"title":"Family","phrases":["Grandfather","Grandmother","Father","Mother","Elder brother","Elder sister","Younger brother","Younger sister","Son","Daughter","Husband","Wife","Parents","Children","Friend","Relative","Grandchild","Baby"]},{"title":"Body Parts","phrases":["Head","Forehead","Eye","Ear","Nose","Mouth","Chin","Shoulder","Arm","Bone","Hand","Fingers","Wrist","Eyebrow","Eyelashes","Body","Leg","Ankle","Waist","Skin","Nail","Cheek","Neck","Chest","Stomach","Teeth","Lips","Hair"]},{"title":"Daily Phrases","phrases":["Placing an order","Confirming an order","Thank you for the food (Before eating)","Thank you for the food (After eating)","I am home/I’m back","Welcome back, you are home","I will go and come","Yes, you go and come","Welcome (Guest to your home)","Welcome (To customers in a shop)"]},{"title":"Greetings","phrases":["Good morning","Good afternoon / Hello / Hi","Good night","Sorry / Excuse me / Thank you","Sorry","Everyone","Thank you","You are welcome","See you again","Goodbye","Good evening","Please (while asking favor)","Please (while offering something)","Please","Congratulations","It’s ok / Alright","Birthday"]},{"title":"Classroom Instructions","phrases":["To start","To understand","To take a break / rest","To finish"]},{"title":"Question Types","phrases":["Shall we start?","Shall we take a break?","Shall we finish?","Do you understand?"]},{"title":"Plural Types","phrases":["Let’s start","Let’s take a break","Let’s finish"]},{"title":"Days of the Week","phrases":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","What day?","What is the day today?"]},{"title":"Days","phrases":["Day before yesterday","Yesterday","Today","Tomorrow","Day after tomorrow"]},{"title":"Years","phrases":["Year before last","Last year","This year","Next year","Year after next"]}]

audio_files = []

for category in english_sentences_dataset:
    # Generate the audio for the title
    title_filename = f"{category['title']}_title.mp3"
    english_to_uk_audio(category["title"], title_filename)
    audio_files.append(title_filename)
    
    for i, sentence in enumerate(category["phrases"]):
        english_filename = f"{category['title']}_english_{i}.mp3"
        japanese_filename = f"{category['title']}_japanese_{i}.mp3"
        
        # Generate the audio for the English sentence
        english_to_uk_audio(sentence, english_filename)
        audio_files.append(english_filename)
        
        # Generate the audio for the Japanese translation
        english_to_japanese_audio(sentence, japanese_filename)
        
        # Repeat the Japanese translation 5 times
        for _ in range(5):
            audio_files.append(japanese_filename)

# Combine all the audio files into a single file
combine_audio_files(audio_files, "combined_audio.mp3")

# Clean up individual audio files
for file in set(audio_files):  # Use set to avoid deleting the same file multiple times
    os.remove(file)
