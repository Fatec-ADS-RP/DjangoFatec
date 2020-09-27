from django.shortcuts import render

from .forms import Contact

def index(request):
	return render(request, 'index.html')

def videos(request):
	return render(request, 'videos.html')

def contact(request):
    context = {}
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = Contact()
    else:
        form = Contact()

    context['form'] = form

    template_name = 'contato.html'
    return render(request, template_name, context)