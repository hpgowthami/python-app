from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.qr_code_service import QRCodeService

router = APIRouter()
qr_code_service = QRCodeService()

class QRCodeRequest(BaseModel):
    data: str
    expiration: int  # Expiration time in seconds

class QRCodeResponse(BaseModel):
    qr_code_url: str
    metadata_id: int

@router.post("/generate", response_model=QRCodeResponse)
async def generate_qr_code(request: QRCodeRequest):
    try:
        qr_code_url, metadata_id = qr_code_service.generate_qr_code(request.data, request.expiration)
        return QRCodeResponse(qr_code_url=qr_code_url, metadata_id=metadata_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/retrieve/{metadata_id}", response_model=QRCodeResponse)
async def retrieve_qr_code(metadata_id: int):
    try:
        qr_code_url = qr_code_service.get_qr_code(metadata_id)
        if qr_code_url is None:
            raise HTTPException(status_code=404, detail="QR code not found")
        return QRCodeResponse(qr_code_url=qr_code_url, metadata_id=metadata_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))