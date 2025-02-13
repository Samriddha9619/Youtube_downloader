from django.shortcuts import render
import yt_dlp
def youtube_downloader(request):
    if request.method == "POST":
        video_url = request.POST.get("video_url")
        try:
            # yt-dlp options
            ydl_opts = {
                'format': 'best',  # Get best available quality
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)  # Get video info without downloading
                download_url = info.get("url")  # Get direct video URL
                video_title = info.get("title", "Unknown Title")

            return render(request, "downloader/youtube.html", {"download_url": download_url, "video_title": video_title})
        
        except Exception as e:
            return render(request, "downloader/youtube.html", {"error": "Invalid URL or video cannot be downloaded."})

    return render(request, "downloader/youtube.html")