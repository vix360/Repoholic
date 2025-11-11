# AI Chatbot — Starter Repo (FastAPI + React)

Deskripsi
--------
Proyek ini adalah starter template untuk membangun AI Chatbot sederhana:
- Backend: FastAPI dengan endpoint /api/chat
- Frontend: React (Vite) demo sederhana
- Docker + docker-compose untuk menjalankan backend dan frontend secara cepat
- Adapter LLM stub (ganti dengan integrasi OpenAI atau model lokal)

Fitur
-----
- Endpoint REST /api/chat untuk menerima pesan dan merespons
- Struktur modular: app/api, app/models
- Contoh Dockerfile dan docker-compose.yml
- README cepat untuk memulai

Quickstart (development)
------------------------
1. Backend
   - Masuk ke folder backend (root)
   - Buat virtualenv dan install:
     ```
     python -m venv .venv
     source .venv/bin/activate  # Linux/macOS
     .venv\Scripts\activate     # Windows
     pip install -r requirements.txt
     ```
   - Jalankan:
     ```
     uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
     ```
   - Buka http://localhost:8000/docs untuk OpenAPI

2. Frontend
   - Masuk ke folder frontend
   - Install dan jalankan:
     ```
     npm install
     npm run dev
     ```
   - Buka http://localhost:5173

Docker (alternatif)
-------------------
- Jalankan:
  ```
  docker-compose up --build
  ```
- Backend akan tersedia di port 8000, frontend di port 5173

Kontribusi
---------
Silakan buat issue atau PR. Untuk integrasi LLM, ganti adapter di app/models/adapter.py

Lisensi
------
MIT
