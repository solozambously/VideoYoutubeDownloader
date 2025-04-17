FROM python:3.9-slim
COPY app.py functions.py requirements.txt ./
RUN apt-get update && apt-get install -y ffmpeg && apt-get clean
RUN pip install -r requirements.txt
EXPOSE 5500
CMD ["python", "app.py"]