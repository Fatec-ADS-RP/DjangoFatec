from django.shortcuts import render, get_object_or_404

from .models import Topics

def topicos(request):
    topicos = Topics.objects.all()
    template_name = 'topicos.html'
    context = {
        'topicos': topicos
    }
    return render(request, template_name, context)

def details(request, slug):
    topico = get_object_or_404(Topics,slug=slug)
    topicos = Topics.objects.all()
    context = {
        'topico': topico,
        'topicos': topicos
    }
    template_name = 'details.html'
    return render(request, template_name, context)



