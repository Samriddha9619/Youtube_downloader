
from http.client import HTTPResponse
from django.shortcuts import render, redirect 
from pytube import YouTube




def youtube(request): 

	if request.method == 'POST': 
		

		link = request.POST['link'] 
		try:
			video = YouTube(link) 
			stream = video.streams.get_lowest_resolution() 
			stream.download() 
		except Exception as e:
			return HTTPResponse(f"Error: {str(e)}")

	
		return render(request, 'downloader/youtube.html') 
	return render(request, 'downloader/youtube.html')
