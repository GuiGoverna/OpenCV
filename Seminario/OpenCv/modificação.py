import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image_path = 'imgs/exemplo.jpeg'
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Verificar se a imagem foi carregada corretamente
if image is None:
    raise Exception("Não foi possível carregar a imagem. Verifique o caminho do arquivo.")

# Aplicar filtro de desfoque (blur) na imagem
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Converter a imagem original e a imagem desfocada para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blurred_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# Detectar bordas usando o algoritmo Canny
edges = cv2.Canny(gray_blurred_image, 50, 150)

# Exibir as imagens usando matplotlib
plt.figure(figsize=(10, 8))

plt.subplot(1, 3, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Imagem Desfocada')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Detecção de Bordas')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()
