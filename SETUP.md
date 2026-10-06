# 🚀 fastapi-learning - Setup & Development Guide

Comprehensive instructions for setting up, running, testing, and deploying **fastapi-learning**.

---

## 📋 Prerequisites

- **Python**: `>= 3.12`
- **uv**: Fast Python package installer ([Install uv](https://docs.astral.sh/uv/getting-started/installation/))


---

## 🛠️ Local Development Setup

### 1. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Activate Virtual Environment
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
uv sync --dev
```



### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Run Django Dev Server
```bash
python manage.py runserver 8000
```

### 7. Run Celery Worker (Separate Terminal Tab)
```bash
source .venv/bin/activate
celery -A config worker -l info
```

---



---

## 🧪 Testing & Code Quality

### Run Test Suite
```bash
uv run pytest
```

### Code Formatting & Linting
```bash
uv run ruff check .
uv run ruff format .
```
