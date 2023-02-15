FROM python:3.10.8
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501"]

# docker build -t spacecraft-app .
# docker run -p 8501:8501 spacecraft-app