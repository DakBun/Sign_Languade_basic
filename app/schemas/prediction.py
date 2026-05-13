from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class LandmarkPoint(BaseModel):
    """Định nghĩa một điểm landmark (x, y, z)."""
    x: float
    y: float
    z: float = 0.0

class PredictionInput(BaseModel):
    """Dữ liệu đầu vào: Danh sách 21 điểm landmarks từ bàn tay."""
    landmarks: List[LandmarkPoint]

class PredictionResponse(BaseModel):
    """Kết quả trả về sau khi mô hình Random Forest dự đoán[cite: 46]."""
    label: str
    confidence: float
    timestamp: datetime = datetime.now()
    message: Optional[str] = "Dự đoán thành công"

class PredictionInDB(PredictionResponse):
    """Schema mở rộng dùng khi lấy dữ liệu từ cơ sở dữ liệu[cite: 23]."""
    id: int

    class Config:
        from_attributes = True