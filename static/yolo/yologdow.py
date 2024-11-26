import gdown

# URL do link público do Google Drive
url = "https://drive.google.com/file/d/1wx3_TFZsvfB4jKUw6CA3yt2HuGiktSKn"
output = "yolov4_custom_3000.weights"  # Nome do arquivo local

# Baixar o arquivo
gdown.download(url, output, quiet=False)
print("Download concluído!")