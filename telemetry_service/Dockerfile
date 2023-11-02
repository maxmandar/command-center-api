FROM python:3.11

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    python3-dev


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["daphne", "telemetry_service.asgi:application", "-b", "0.0.0.0", "-p", "9443"]


  