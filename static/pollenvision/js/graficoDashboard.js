const ctx = document.getElementById('grafico-dashboard');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['21/11', '22/11', '23/11', '24/11', '25/11', '26/11'],  // Rótulos das barras
    datasets: [{
      label: 'Porcentagem de Viabilidade',
      data: [98, 79, 60, 80, 87, 90],  // Valores das barras
      backgroundColor: '#20A345',  // Cor das barras
      borderColor: '#20A345',  // Cor das bordas
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,  // Torna o gráfico responsivo
    plugins: {
      title: {
        display: true,
        text: 'Visão geral da viabilidade do pólen',  // Título do gráfico
        font: {
          size: 18,
          weight: 'bold'
        },
        color: '#000'
      },
      tooltip: {
        backgroundColor: '#fff',
        titleColor: '#000',
        bodyColor: '#000',
        borderColor: '#ddd',
        borderWidth: 1
      }
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Data',  // Título do eixo X
          color: '#000'
        }
      },
      y: {
        beginAtZero: true,
        max: 100,
        title: {
          display: true,
          text: 'Porcentagem de Viabilidade',  // Título do eixo Y
          color: '#000'
        }
      }
    }
  }
});
