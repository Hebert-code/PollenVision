  // Seleciona os elementos
  const carrosselLista = document.querySelector('.carrossel-lista');
  const prevButton = document.querySelector('.prev');
  const nextButton = document.querySelector('.next');
  let currentIndex = 0;

  // Função para mudar o slide
  function moveToSlide(index) {
    const totalSlides = document.querySelectorAll('.carrossel-item').length;
    if (index >= totalSlides - 2) {  
      currentIndex = 0;
    } else if (index < 0) {
      currentIndex = totalSlides - 3;  
    } else {
      currentIndex = index;
    }
    carrosselLista.style.transform = `translateX(-${currentIndex * 33.33}%)`; 
  }

  // Eventos dos botões de navegação
  nextButton.addEventListener('click', () => moveToSlide(currentIndex + 1));
  prevButton.addEventListener('click', () => moveToSlide(currentIndex - 1));

  // Inicializa o carrossel na primeira posição
  moveToSlide(currentIndex);