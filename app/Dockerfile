FROM python:3.7

COPY . .


RUN pip install --upgrade pip

WORKDIR /app/
RUN pip install -r requirements.txt



EXPOSE 8000

WORKDIR ./api/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
