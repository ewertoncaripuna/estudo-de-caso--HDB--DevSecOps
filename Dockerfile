# Imagem base com Python
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Expõe a porta do Flask
EXPOSE 8080

# Variável de ambiente para o Flask
ENV FLASK_APP=todo_project/run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Comando para iniciar
CMD ["flask", "run"]
