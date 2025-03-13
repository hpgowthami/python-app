from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.qr_code import router as qr_code_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(qr_code_router, prefix="/qr", tags=["qr"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the QR Code Generator API"}