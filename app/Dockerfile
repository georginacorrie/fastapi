FROM python3.7

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt



EXPOSE $PORT

WORKDIR /api
CMD ["uvicorn", "main:app"]