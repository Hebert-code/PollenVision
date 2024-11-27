import gdown

# ID do arquivo extraído da URL
file_id = "1wx3_TFZsvfB4jKUw6CA3yt2HuGiktSKn"
url = f"https://drive.google.com/uc?id={file_id}"  # URL correta para o gdown
output = "yolov4_custom_3000.weights"

# Baixar o arquivo
gdown.download(url, output, quiet=False)
print("Download concluído!")
