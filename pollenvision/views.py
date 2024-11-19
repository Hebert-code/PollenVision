from django.shortcuts import render
from .models import AnalysisResult, Profile, Image, Plant
from django.http import HttpResponse
from reportlab.pdfgen import canvas

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
    if request.method == 'POST' and 'image_path' in request.FILES and 'plant_name' in request.POST:

        plant_name = request.POST['plant_name']
        image_file = request.FILES['image_path']

        user = Profile.objects.first()
        plant = Plant.objects.create(user=user, plant_name=plant_name)

        Image.objects.create(plant=plant, user=user, image_path=image_file)

        return resultado(request)

    return render(request, 'pollenvision/upload.html')

def resultado(request):
    #Basicamente vamos pegar a analise mais recente
    #A yolo salva no banco e a gente pega a mais recente 
    analysis_result = AnalysisResult.objects.latest('analysis_date')

    return render(request, 'pollenvision/resultado.html', {'analysis_result': analysis_result})

def historico(request):
    if request.method == "GET":
        analysis_results = AnalysisResult.objects.all()
        analysis_results = analysis_results.order_by('-analysis_date')[:3]

        return render(request, 'pollenvision/historico.html', {'analysis_results': analysis_results})

    if request.method == "POST":
        analysis_results = AnalysisResult.objects.all()
        
        # Pega os dados do formulário
        plant_id1 = request.POST.get('id_plant')
        start_date = request.POST.get('datainicial')
        end_date = request.POST.get('datafinal')

        print(f"ID da Planta: {plant_id1}")
        print(f"Data Inicial: {start_date}")
        print(f"Data Final: {end_date}")

        # Filtro pelo ID da planta
        if plant_id1:
            analysis_results = analysis_results.filter(plant__plant_id = plant_id1)
    
    for result in analysis_results:
        plant = result.plant  
        print(plant.plant_name) 

    analysis_results = analysis_results.order_by('-analysis_date')[:3]
    
    return render(request, 'pollenvision/historico.html', {'analysis_results': analysis_results})
    

def suporte(request):
    return render(request, 'pollenvision/suporte.html')

def relatorios(request):
    if request.method == "POST":
        nome_planta = request.POST.get("id_planta")
        data_inicial = request.POST.get("data_inicial")
        data_final = request.POST.get("data_final")

        analises = AnalysisResult.objects.all()

        if nome_planta:
            analises = analises.filter(plant__plant_name=nome_planta)
        if data_inicial:
            analises = analises.filter(analysis_date__gte=data_inicial)
        if data_final:
            analises = analises.filter(analysis_date__lte=data_final)

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="relatorio.pdf"'

        p = canvas.Canvas(response)
        p.drawString(100, 800, "Relatório de Análises")
        p.drawString(100, 780, f"Período: {data_inicial} a {data_final}")

        y = 750
        for analise in analises:
            p.drawString(
                100,
                y,
                f"Planta: {analise.plant.plant_name} | Data: {analise.analysis_date} | Resultado: {analise.viability}",
            )
            y -= 20
            if y < 100: 
                p.showPage()
                y = 800

        p.showPage()
        p.save()
        return response

    return render(request, "pollenvision/relatorios.html")
