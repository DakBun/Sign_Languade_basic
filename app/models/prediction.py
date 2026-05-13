from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, DateTime
from ..db.database import Base

# SQLAlchemy ORM Model (cho database)
class PredictionRecord(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    label = Column(String, index=True)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

# Pydantic Schemas (cho API validation)
# Schema để nhận dữ liệu đầu vào (nếu cần tạo thủ công)
class PredictionBase(BaseModel):
    label: str
    confidence: float

# Schema dùng khi tạo mới một bản ghi (có thể mở rộng thêm)
class PredictionCreate(PredictionBase):
    pass

# Schema dùng để trả về dữ liệu cho Client (Response)
class Prediction(PredictionBase):
    id: int
    created_at: datetime

    class Config:
        # Cho phép Pydantic đọc dữ liệu từ các đối tượng SQLAlchemy (ORM)
        from_attributes = True

# Schema trả về kết quả dự đoán nhanh kèm tin nhắn
class PredictionResult(BaseModel):
    label: str
    confidence: float
    message: Optional[str] = "Nhận diện thành công"