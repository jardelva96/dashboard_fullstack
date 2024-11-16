FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos do diretório "backend" para o contêiner
COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

# Instale as dependências
RUN pip install -r /app/requirements.txt

# Defina o caminho do PYTHONPATH para incluir a pasta "app"
ENV PYTHONPATH=/app

# Comando para rodar o FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
