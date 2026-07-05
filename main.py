"""FastAPI Hello Python Application."""

import time

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


app = FastAPI(
    title="Hello Python API",
    description="Sadə FastAPI tətbiqi - Docker ilə hazır",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Prometheus metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP request count",
    ["method", "endpoint"],
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"],
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    """Hər request üçün metrics topla."""
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start
    path = request.url.path or "unknown"
    REQUEST_COUNT.labels(method=request.method, endpoint=path).inc()
    REQUEST_LATENCY.labels(method=request.method, endpoint=path).observe(duration)
    return response


@app.get("/")
async def root():
    """Əsas səhifə."""
    return {"message": "Hello Python!", "status": "working"}


@app.get("/health")
async def health():
    """Sağlamlıq yoxlaması - Docker/Kubernetes üçün."""
    return {"status": "healthy"}


@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None = None):
    """Nümunə endpoint - item məlumatı."""
    return {"item_id": item_id, "q": q}


@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    """Prometheus metrics endpoint."""
    return PlainTextResponse(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
