# 🎧 Inbox2Audio: Turn Your Newsletters Into Screen-Free Learning

Tired of your eyes bleeding from reading endless **System Design newsletters** in your inbox? Wish you could just *listen* to them while walking, cooking, or vibing on your balcony?

**Inbox2Audio** is here to rescue your screen-fatigued soul. It automates the entire pipeline:

📥 **Extract** → 📄 **Convert** → ☁️ **Upload** → 🔊 **Narrate** → ☁️ **Reupload** → 📲 **Notify**

## 🚀 What It Does

1. **Pulls emails** from a specific Gmail label (like `SystemDesign`)  
2. **Extracts the content** and saves each email as a plain `.txt` file  
3. **Uploads those `.txt` files** to your Google Drive  
4. ** CRON fetches them back** and converts the text to audio using a text-to-speech engine  
5. **Uploads the `.mp3` files** back to Drive, and *deletes* the original `.txt` files to keep things tidy  
6. **Sends you a WhatsApp message** with a direct Drive link to the audio file  
   > So you can *listen to your newsletters like a podcast*

## 💡 Why This Exists

System design newsletters are great... but **reading them daily?** Nah.  
This project exists because we’re all about **reducing screen time** and **boosting passive learning**.

## 🛠 Tech Stack

- **Gmail API** – for fetching label-based emails
- **Google Drive API** – for storing & fetching files
- **gTTS** – for audio generation
- **WhatsApp API** – for sending those slick audio links
- **Python** – the brains of the operation

## 🔄 Workflow

```mermaid
graph TD;
    A[Gmail Label] --> B[Extract Email Body];
    B --> C[Save as .txt];
    C --> D[Upload to Drive];
    D --> E[Cron Schedule];
    E --> F[Fetch from Drive];
    F --> G[Convert to Audio];
    G --> H[Upload Audio to Drive];
    H --> I[Delete .txt File];
    I --> J[Send WhatsApp Link];
