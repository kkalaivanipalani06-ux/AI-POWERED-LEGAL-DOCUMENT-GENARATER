from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, skills, wallet


# --------------------------------------------------
# Create FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Skill Wallet API",
    description="REST API for the Skill Wallet application",
    version="1.0.0"
)


# --------------------------------------------------
# CORS Configuration
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Register API Routers
# --------------------------------------------------

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["Users"]
)

app.include_router(
    skills.router,
    prefix="/api/skills",
    tags=["Skills"]
)

app.include_router(
    wallet.router,
    prefix="/api/wallet",
    tags=["Wallet"]
)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/", tags=["System"])
def root():
    return {
        "message": "Welcome to Skill Wallet API",
        "status": "running",
        "version": "1.0.0"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": "skill-wallet-api"
    }

API integration
After starting the server:

uvicorn app.main:app --reload

The following endpoints will be connected through main.py:

Module	Base URL
Users	/api/users
Skills	/api/skills
Wallet	/api/wallet
Health	/health

FastAPI's interactive documentation will be available at:

http://127.0.0.1:8000/docs

Test main.py
Run:

curl http://127.0.0.1:8000/

Expected:

{
  "message": "Welcome to Skill Wallet API",
  "status": "running",
  "version": "1.0.0"
}

Health check:

curl http://127.0.0.1:8000/health

Expected:

{
  "status": "healthy",
  "service": "skill-wallet-api"
}
