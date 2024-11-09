from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import AnalysisResult, Profile, Image, Plant

# Create your views here.

def index(request):
    return render(request, 'pollenvision/base.html')

def dashboard(request):
    
    resultados = AnalysisResult.objects.all()

    total_viabilidade = sum([resultado.viability for resultado in resultados])
    media_viabilidade = total_viabilidade / len(resultados) if resultados else 0

    total_erro = sum([resultado.error for resultado in resultados])
    media_erro = total_erro / len(resultados) if resultados else 0

    historico_analise = len(resultados)
    
    return render(request, 'pollenvision/dashboard.html', {
        'media_viabilidade': media_viabilidade,
        'historico_analise': historico_analise,
        'media_erro': media_erro,
        'resultados': resultados
    })

def upload(request):
    if request.method == 'POST' and 'image_path' in request.FILES and 'plant_id' in request.POST:

        image_file = request.FILES['image_path']
        
        plant_id = request.POST['plant_id']
        
        try:
            plant = Plant.objects.get(plant_id=plant_id)
        except Plant.DoesNotExist:
            return render(request, 'upload.html', {'error': 'Planta não encontrada!'})
        
        image = Image.objects.create(
            plant=plant,
            user=Profile.objects.first(),  # Aqui você pode adaptar para pegar o usuário correto
            image_path=image_file
        )

        # Após salvar a imagem, redireciona para a página de sucesso
        return redirect('pollenvision/resultado.html')  # Ou a URL de sua escolha

    return render(request, 'pollenvision/upload.html')

def resultado(request):
    return render(request, 'pollenvision/resultado.html')

def historico(request):
    return render(request, 'pollenvision/historico.html')

def relatorios(request):
    return render(request, 'pollenvision/relatorios.html')

def suporte(request):
    return render(request, 'pollenvision/suporte.html')