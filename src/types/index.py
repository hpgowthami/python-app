from pydantic import BaseModel
from typing import Optional

class QRCodeMetadata(BaseModel):
    id: int
    data: str
    created_at: str
    expires_at: str

class QRCodeResponse(BaseModel):
    id: int
    data: str
    url: str
    created_at: str
    expires_at: str