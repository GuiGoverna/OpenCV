import cv2
import numpy as np

# Função para desenhar a imagem com os quadrados ocultos
def draw_hidden_squares(image, squares):
    hidden_image = image.copy()
    for x, y, w, h in squares:
        cv2.rectangle(hidden_image, (x, y), (x + w, y + h), (0, 0, 0), -1)
    return hidden_image

# Carregar a imagem
image = cv2.imread('imgs/Cris.jpg')
image_height, image_width, _ = image.shape

# Configurar os quadrados ocultos
grid_size = 3  # Dividir a imagem em uma grade 3x3
square_width = image_width // grid_size
square_height = image_height // grid_size

# Criar uma lista de quadrados
squares = [(x * square_width, y * square_height, square_width, square_height)
           for y in range(grid_size) for x in range(grid_size)]

# Embaralhar os quadrados para que sejam removidos em ordem aleatória
np.random.shuffle(squares)

# Exibir a imagem inicial com todos os quadrados ocultos
hidden_image = draw_hidden_squares(image, squares)
cv2.imshow('Flagle', hidden_image)

# Loop principal para detectar teclas e revelar partes da imagem
index = 0
while True:
    key = cv2.waitKey(0)  # Espera até uma tecla ser pressionada

    # Se a tecla for 'q', sair do loop
    if key == ord('q'):
        break

    # Revelar o próximo quadrado
    if index < len(squares):
        index += 1
        hidden_image = draw_hidden_squares(image, squares[:len(squares) - index])
        cv2.imshow('Flagle', hidden_image)
    else:
        cv2.imshow('Flagle', image)

# Fechar todas as janelas ao finalizar
cv2.destroyAllWindows()
