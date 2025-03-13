from typing import Optional
import qrcode
import io
from PIL import Image
from fastapi import HTTPException
from src.db.models import QRCodeMetadata
from src.db.session import get_db_session

class QRCodeService:
    def __init__(self):
        self.db_session = get_db_session()

    def generate_qr_code(self, data: str) -> bytes:
        """Generate a QR code image from the provided data."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        return img_byte_arr.getvalue()

    def save_metadata(self, data: str, expiration: Optional[int] = None) -> QRCodeMetadata:
        """Save QR code metadata to the database."""
        qr_code_metadata = QRCodeMetadata(data=data, expiration=expiration)
        self.db_session.add(qr_code_metadata)
        self.db_session.commit()
        return qr_code_metadata

    def get_metadata(self, qr_code_id: int) -> QRCodeMetadata:
        """Retrieve QR code metadata from the database."""
        metadata = self.db_session.query(QRCodeMetadata).filter(QRCodeMetadata.id == qr_code_id).first()
        if not metadata:
            raise HTTPException(status_code=404, detail="QR code metadata not found")
        return metadata