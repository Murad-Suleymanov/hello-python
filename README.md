# Hello Python - FastAPI

Sadə FastAPI tətbiqi, Docker ilə hazır.

## API Endpointləri

| Endpoint       | Metod | Təsvir           |
|----------------|-------|------------------|
| `/`            | GET   | Əsas səhifə      |
| `/health`      | GET   | Sağlamlıq yoxlaması |
| `/metrics`     | GET   | Prometheus metrics |
| `/items/{id}`  | GET   | Item məlumatı    |
| `/docs`        | GET   | Swagger UI       |
| `/redoc`       | GET   | ReDoc            |

## Docker ilə işə salma

```bash
# Image qurma
docker build -t hello-python .

# Konteyneri işə salma
docker run -p 8000:8000 hello-python
```

Sonra brauzerdə açın: http://localhost:8000/docs
