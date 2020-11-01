from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import Contact

@login_required(login_url='accounts:login')
def index(request):
	return render(request, 'index.html')

@login_required(login_url='accounts:login')
def videos(request):
	return render(request, 'videos.html')

@login_required(login_url='accounts:login')
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