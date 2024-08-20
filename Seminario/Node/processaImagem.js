const sharp = require('sharp');
const path = require('path');

// Caminho da imagem
const imagePath = path.join(__dirname, 'imgs/exemplo.jpg');

// Função principal
(async () => {
  try {
    const image = sharp(imagePath);
    // Aplicar filtro de desfoque
    const blurredImage = image.blur(10);
    
    // Salvar a imagem desfocada
    await blurredImage.toFile('imagem_desfocada.jpg');
    
    console.log('Imagem desfocada salva com sucesso.');
  } catch (error) {
    console.error('Erro ao processar a imagem:', error);
  }
})();
