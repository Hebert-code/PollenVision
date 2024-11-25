from django.shortcuts import render
from .models import AnalysisResult, Profile, Image, Plant
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .yolo_utils import yolo_infer
import os
from django.conf import settings

def index(request):
    return render(request, 'pollenvision/base.html')

def dashboard(request):
    
    resultados = AnalysisResult.objects.all()

    total_viabilidade = sum([resultado.viability for resultado in resultados])
    media_viabilidade = total_viabilidade / len(resultados) if resultados else 0

    total_erro = sum([resultado.error for resultado in resultados])
    media_erro = total_erro / len(resultados) if resultados else 0

    historico_analise = len(resultados)

    # Preparar as datas e as viabilidades para o gráfico
    datas = [resultado.analysis_date.strftime('%Y-%m-%d') for resultado in resultados]
    viabilidades = [resultado.viability for resultado in resultados]
    
    return render(request, 'pollenvision/dashboard.html', {
        'media_viabilidade': media_viabilidade,
        'historico_analise': historico_analise,
        'media_erro': media_erro,
        'resultados': resultados,
        'datas': datas,
        'viabilidades': viabilidades,
    })

def upload(request):
    if request.method == 'POST' and 'image_path' in request.FILES and 'plant_name' in request.POST:

        plant_name = request.POST['plant_name']
        image_file = request.FILES['image_path']

        user = Profile.objects.first()
        plant = Plant.objects.create(user=user, plant_name=plant_name)

        # Salva a imagem no banco e no sistema de arquivos
        image_instance = Image.objects.create(plant=plant, user=user, image_path=image_file)

        # Caminho absoluto da imagem salva
        image_path = os.path.join(settings.MEDIA_ROOT, str(image_instance.image_path))

        # Realiza a análise com YOLO
        yolo_results = yolo_infer(image_path)

        # Variáveis para calcular a viabilidade baseada na média de confiança
        total_confidence = 0
        valid_detections = 0
        good_count = 0

        for result in yolo_results:
            confidence = result['confidence']
            total_confidence += confidence
            valid_detections += 1
            if result['class'] == 'Good':
                good_count += 1

        # Calcula a média de confiança se houver detecções válidas
        if valid_detections > 0:
            average_confidence = total_confidence / valid_detections
            # Aqui, você pode definir um critério para a viabilidade baseado na confiança média
            viability = (average_confidence * 100)  # Exemplo de viabilidade com base na média de confiança
        else:
            average_confidence = 0
            viability = 0  # Nenhuma detecção válida

        # Se preferir usar o número de "Good" para viabilidade, substitua:
        # viability = (good_count / grain_count) * 100

        error = 100 - viability  # Simples diferença

        # Salva os resultados no banco
        AnalysisResult.objects.create(
            image=image_instance,
            plant=plant,
            viability=viability,
            grain_count=valid_detections,
            error=error
        )
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
        plant = result.plant  # Acessa o objeto Plant relacionado
        print(plant.plant_name)  # Exemplo de como acessar o nome da planta

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
