const relatorio = document.getElementById('grafico-relatorios');

new Chart(relatorio, {
  type: 'bar',
  data: {
    labels: ['21/11', '22/11', '23/11', '24/11', '25/11', '26/11'], // Rótulos das barras
    datasets: [{
      label: 'Número de relatórios',
      data: [1, 5, 3, 2, 1, 8], // Valores das barras
      backgroundColor: '#20A345', // Cor das barras
      borderColor: '#20A345', // Cor das bordas
      borderWidth: 1
    }]
  },
  options: {
    responsive: true, // Torna o gráfico responsivo
    plugins: {
      title: {
        display: true,
        text: 'Estatísticas do Relatório', // Título do gráfico
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
          text: 'Data', // Título do eixo X
          color: '#000'
        }
      },
      y: {
        beginAtZero: true,
        max: 10,
        title: {
          display: true,
          text: 'Número de relatórios', // Título do eixo Y
          color: '#000'
        }
      }
    }
  }
});