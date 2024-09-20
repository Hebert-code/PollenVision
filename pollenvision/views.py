from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pollenvision/base.html')

def dashboard(request):
    return render(request, 'pollenvision/dashboard.html')

def upload(request):
    return render(request, 'pollenvision/upload.html')

def resultado(request):
    return render(request, 'pollenvision/resultado.html')

def historico(request):
    return render(request, 'pollenvision/historico.html')

def relatorios(request):
    return render(request, 'pollenvision/relatorios.html')

def suporte(request):
    return render(request, 'pollenvision/suporte.html')