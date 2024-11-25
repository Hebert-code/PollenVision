import cv2
import numpy as np
import os

# Caminho para os arquivos do modelo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YOLO_DIR = os.path.join(BASE_DIR, "static", "yolo")  # Definir o diretório de modelos YOLO

CFG_PATH = os.path.join(YOLO_DIR, "yolov4_custom.cfg")
WEIGHTS_PATH = os.path.join(YOLO_DIR, "yolov4_custom_3000.weights")
NAMES_PATH = os.path.join(YOLO_DIR, "obj.names")

# Verifique se os arquivos existem antes de carregar
if not os.path.exists(CFG_PATH):
    raise FileNotFoundError(f"Arquivo de configuração não encontrado: {CFG_PATH}")
if not os.path.exists(WEIGHTS_PATH):
    raise FileNotFoundError(f"Arquivo de pesos não encontrado: {WEIGHTS_PATH}")
if not os.path.exists(NAMES_PATH):
    raise FileNotFoundError(f"Arquivo de nomes de classes não encontrado: {NAMES_PATH}")

# Carrega o modelo YOLO
net = cv2.dnn.readNet(WEIGHTS_PATH, CFG_PATH)

# Carrega os nomes das classes
classes = []
with open(NAMES_PATH, "r") as f:
    classes = [line.strip() for line in f.readlines()]

def yolo_infer(image_path):
    # Carrega a imagem
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Prepara a entrada para YOLO
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Obtem as camadas de saída
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


    # Executa a inferência
    detections = net.forward(output_layers)

    results = []  # Inicializa a lista de resultados
    total_confidence = 0  # Variável para acumular a soma das confianças
    valid_detections = 0  # Contador para o número de detecções válidas

    for output in detections:
        for detection in output:
            scores = detection[5:]  # Obtém as pontuações para as classes
            class_id = np.argmax(scores)  # Identifica a classe com maior pontuação
            confidence = scores[class_id]  # Confiança da classe identificada
            
            if confidence > 0.3:  # Limite de confiança reduzido para 0.3
                # Calcula as coordenadas da caixa delimitadora
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                # Armazena os resultados detectados
                results.append({
                    "class": classes[class_id],
                    "confidence": float(confidence),
                    "box": [x, y, w, h]
                })

                # Acumula a confiança e incrementa o contador de detecções válidas
                total_confidence += confidence
                valid_detections += 1
                
                # Exibe detalhes sobre a detecção
                print(f"Class: {classes[class_id]}, Confidence: {confidence:.2f}, Box: {x, y, w, h}")

    # Calcula a média de confiança se houver detecções válidas
    if valid_detections > 0:
        average_confidence = total_confidence / valid_detections
        print(f"Average Confidence: {average_confidence:.2f}")
    else:
        average_confidence = 0
        print("No valid detections found.")

    # Determina a viabilidade do pólen com base na média de confiança
    if average_confidence > 0.5:  # Exemplo de limite para a viabilidade
        viability = "Viable"
    else:
        viability = "Not Viable"

    print(f"Pollen Viability: {viability}")

    # Retorna os resultados
    return results

