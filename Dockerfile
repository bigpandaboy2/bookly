FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "src", "--host", "0.0.0.0", "--port", "8000"]