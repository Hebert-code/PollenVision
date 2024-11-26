# PollenVision

PollenVision é uma plataforma de análise de pólen que oferece serviços tanto para a web quanto para dispositivos móveis. Esta plataforma visa fornecer dados precisos e detalhados sobre concentrações de pólen para ajudar a identificar a viabilidade do polén.
![image](https://github.com/user-attachments/assets/18e271b0-48bd-4125-82b6-f8379c59ec76)

## Estrutura do Projeto

A estrutura atual do projeto segue o padrão básico do Django, com algumas pastas adicionais para arquivos estáticos, templates e configurações de ambiente virtual.

```plaintext
pollenvision/
├── home/
│   ├── migrations/
│   ├── __pycache__/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── pollenvision/
│   ├── __pycache__/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── setup/
│   ├── __pycache__/
│   ├── css/
│   │   └── style.css
│   ├── img/
│   │   ├── hero_logo.png
│   │   └── logo.png
├── static/
│   └── home/
│       └── css/
│           └── style.css
│       └── img/
│           ├── hero_logo.png
│           └── logo.png
├── templates/
│   └── home/
│       └── index.html
├── venv/
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
```

## Funcionalidades Planejadas

- **Análise de Pólen**: Fornecer dados detalhados sobre os níveis de pólen.
- **Versão Web e Mobile**: Disponível tanto para usuários de desktop quanto para dispositivos móveis.
- **API REST**: Integração via APIs para fornecer dados de pólen a outros serviços ou aplicativos.
- **Visualizações Interativas**: Gráficos e mapas para visualizar dados de pólen em tempo real.

## Instalação

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/Hebert-code/pollenvision.git
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente. Um exemplo está disponível em `.env_example`:

   ```bash
   cp .env_example .env
   ```

5. Rode as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```
7. Rodar o Script para baixar os pesos
   ```bash
   python static/yolo/yologdow.py
   ```

8. Acesse o projeto em `http://localhost:8000`.

## Estrutura de Pastas

- **home/**: Contém as configurações principais do app, como `views`, `urls` e `models`.
- **static/**: Arquivos estáticos, como CSS e imagens.
- **templates/**: Arquivos HTML para renderização.
- **venv/**: Ambiente virtual para gerenciamento de pacotes.

## Requisitos

- Python 3.x
- Django 5.x
- [Outras dependências estão listadas em `requirements.txt`](requirements.txt).

## Contribuições

1. Fork o repositório.
2. Crie um branch com a sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para o branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


