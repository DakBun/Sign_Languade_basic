from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Import các logic AI từ module bạn đã code xong
from ai_modules.classifier import sign_classifier
from ai_modules.feature_extractor import extract_features
from ai_modules.preprocessor import normalize_data

router = APIRouter()

# Định nghĩa cấu trúc dữ liệu đầu vào (ví dụ: danh sách 21 landmarks từ frontend)
class PredictionInput(BaseModel):
    landmarks: List[dict] # Danh sách các điểm {'x':..., 'y':..., 'z':...}

# Định nghĩa cấu trúc kết quả trả về
class PredictionResponse(BaseModel):
    label: str
    confidence: float
    message: Optional[str] = None

@router.post("/", response_model=PredictionResponse)
async def predict_sign(data: PredictionInput):
    """
    Endpoint nhận diện ký hiệu ngôn ngữ từ dữ liệu landmarks.
    Luồng xử lý: Input -> Extract Features -> Normalize -> Predict
    """
    try:
        # 1. Trích xuất đặc trưng (21 landmarks * 2 = 42 features)
        features = extract_features(data.landmarks)
        
        # 2. Tiền xử lý / Chuẩn hóa dữ liệu
        normalized_features = normalize_data(features)
        
        # 3. Dự đoán bằng model Random Forest (.p)
        # Giả định sign_classifier.predict trả về (nhãn, độ tự tin)
        label, confidence = sign_classifier.predict(normalized_features)
        
        return PredictionResponse(
            label=label,
            confidence=round(float(confidence), 2),
            message="Nhận diện thành công"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi trong quá trình nhận diện: {str(e)}")

@router.get("/labels")
async def get_labels():
    """Trả về danh sách các ký hiệu mà mô hình có thể nhận diện."""
    return {"supported_labels": sign_classifier.get_label_list()}