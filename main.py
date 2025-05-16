from drive_utils import authenticate_drive, get_latest_txt_file, get_folder_id
from text_to_audio import text_to_speech
from send_whatsapp import send_whatsapp_message
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("🔐 Authenticating with Google Drive...")
    drive = authenticate_drive()
    folder_name = os.getenv("folder_name")
    audio_folder = os.getenv("audio_folder")

    print("📂 Fetching latest newsletter text file...")
    file_data_list = get_latest_txt_file(drive, folder_name)
    if not file_data_list or None in file_data_list:
        print("❌ No new newsletter found in Drive.")
        return

    for (text, file) in file_data_list:
        print(f"✅ Found newsletter: {file['title']}")

        print("🎤 Converting text to audio...")
        mp3_path = text_to_speech(text, file['title'].replace('.txt', ''))
        print(f"🎧 Audio file created: {mp3_path}")

        print("🚀 Uploading audio to Drive...")
        audio_folder_id = get_folder_id(drive, audio_folder)
        audio_file = drive.CreateFile({
            'title': file['title'].replace('.txt', '.mp3'),
            'parents': [{'id': audio_folder_id}]
        })
        audio_file.SetContentFile(mp3_path)
        audio_file.Upload()

        public_link = audio_file['alternateLink']
        print(f"✅ Uploaded audio. Link: {public_link}")

        print("📲 Sending WhatsApp message with audio link...")
        send_whatsapp_message("hello")
        print("✅ WhatsApp message sent!")

        print("🧹 Cleaning up audio file and text file from Drive...")
        os.remove(mp3_path)
        file.Delete()
        print("🗑️ Text file deleted.")

    print("✅ Done! System design audio pipeline ran successfully.")


if __name__ == "__main__":
    main()
