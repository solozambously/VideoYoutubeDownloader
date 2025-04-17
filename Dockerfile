FROM python:3.9-slim
COPY app.py functions.py ./
RUN pip install -r requirements.txt
EXPOSE 5500
CMD ["python", "app.py"]