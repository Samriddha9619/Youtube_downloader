# 🎥 Django YouTube Video Downloader

A simple and clean web application built with **Django** and **Python** to download YouTube videos directly from a URL.  
The application uses the **pytubefix** library to fetch video data and streams the file directly to the user's browser without saving it on the server.

---

## ✨ Features
- **Simple Interface**: Clean, modern, and responsive UI for a seamless experience.  
- **Direct Download**: Enter a YouTube video URL and get an instant download link.  
- **Serverless Streaming**: Videos are streamed directly to the user's browser (no server storage).  
- **Error Handling**: User-friendly messages for invalid links or errors.  
- **Lightweight**: Minimal dependencies → fast & easy to deploy.  

---

## 🛠 Tech Stack
- **Backend**: Python, Django  
- **YouTube API**: pytubefix  
- **Frontend**: HTML, CSS  
- **Python Version**: 3.8+  

---

## 🚀 Setup and Installation

Follow these steps to run the project locally:

### 1. Prerequisites
- Python 3.8 or higher  
- pip (Python package installer)  

### 2. Clone the Repository
```bash
git clone https://github.com/Samriddha9619/Youtube_downloader.git
cd Youtube_downloader
```

### 3. Create and Activate a Virtual Environment  
**For Windows**  
```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

> 💡 If you don’t have a `requirements.txt`, create one after installing manually:  
```bash
pip install django pytubefix
pip freeze > requirements.txt
```

### 5. Run Django Migrations
```bash
python manage.py migrate
```

### 6. Start the Development Server
```bash
python manage.py runserver
```

Your app will be live at:  
👉 http://127.0.0.1:8000/

---

## 📌 Usage
1. Open the app in your browser.  
2. Copy the YouTube video URL.  
3. Paste it into the input field and click **Submit**.  
4. Your browser will prompt you to save the video file (`.mp4`).  

---

## 📂 Project Structure
```
Youtube_downloader/
│── downloader/
│   ├── views.py              # Handles form, fetches video, streams response
│   ├── templates/downloader/youtube.html  # Main HTML UI
│   ├── static/downloader/style.css        # CSS styling
│   └── urls.py               # URL routes
│
├── manage.py
└── requirements.txt
```

---

## 📄 License
This project is licensed under the **MIT License**.  
See the LICENSE file for details.
