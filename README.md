Django YouTube Video Downloader
A simple and clean web application built with Django and Python to download YouTube videos directly from a URL. The application uses the pytubefix library to fetch video data and streams the file directly to the user's browser without saving it on the server.

Features
Simple Interface: A clean, modern, and responsive user interface for a seamless experience.

Direct Download: Enter a YouTube video URL and get an instant download link.

Serverless Streaming: Videos are streamed directly to the user's browser, saving server disk space and bandwidth.

Error Handling: Provides user-friendly feedback for invalid links or other download errors.

Lightweight: Built with minimal dependencies, making it fast and easy to deploy.

Tech Stack
Backend: Python, Django

YouTube API: pytubefix

Frontend: HTML, CSS

Python Version: 3.8+

Setup and Installation
Follow these steps to get the project running on your local machine.

1. Prerequisites
Python 3.8 or higher

pip (Python package installer)

2. Clone the Repository
Clone this repository to your local machine using Git:

git clone [https://github.com/Samriddha9619/Youtube_downloader.git](https://github.com/Samriddha9619/Youtube_downloader.git)
cd your-repository-name

3. Create and Activate a Virtual Environment
It's a best practice to create a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

4. Install Dependencies
Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

pip freeze > requirements.txt

5. Run Django Migrations
Although this simple project doesn't use a database, it's good practice to run initial migrations.

python manage.py migrate

6. Start the Development Server
You're all set! Start the Django development server.

python manage.py runserver

The application will be running at http://127.0.0.1:8000/.

Usage
Open your web browser and navigate to http://127.0.0.1:8000/.

Copy the URL of the YouTube video you want to download.

Paste the URL into the input field on the page.

Click the "Submit" button.

Your browser will prompt you to save the video file (.mp4).

Project Structure
Here is a brief overview of the key files in the downloader app:

views.py: Contains the main logic for handling the form submission, fetching the video using pytubefix, and streaming the response.

templates/downloader/youtube.html: The HTML template that renders the user interface.

static/downloader/style.css: The CSS file that styles the HTML page.

urls.py: Defines the URL routes for the application.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
