from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def topicos(request):
	return render(request, 'topicos.html')

def videos(request):
	return render(request, 'videos.html')

def contato(request):
	return render(request, 'contato.html')