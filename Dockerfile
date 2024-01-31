# FROM tiangolo/uvicorn-gunicorn:python3.11

# WORKDIR /app
# COPY . .

# RUN pip install --no-cache-dir -r requirements.txt

# WORKDIR /app/API

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . .

EXPOSE 8000

WORKDIR /app/API
