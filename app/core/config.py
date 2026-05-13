import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # --- Cấu hình chung ---
    PROJECT_NAME: str = "Sign Language Detection"
    API_V1_STR: str = "/api/v1"
    
    # --- Cấu hình AI Modules ---
    # Đường dẫn đến model đã train trong models_store/
    MODEL_PATH: str = os.path.join("models_store", "model.p")
    LABEL_MAP_PATH: str = os.path.join("models_store", "label_map.json")
    
    # Ngưỡng độ tự tin tối thiểu để chấp nhận kết quả dự đoán
    MIN_CONFIDENCE_THRESHOLD: float = 0.7
    
    # --- Cấu hình Camera ---
    # Mặc định là 0 cho webcam tích hợp
    CAMERA_DEVICE_INDEX: int = 0
    FRAME_WIDTH: int = 640
    FRAME_HEIGHT: int = 480
    
    # --- Cấu hình Database (Nếu dùng) ---
    DATABASE_URL: str = "sqlite:///./sign_language.db"

    class Config:
        case_sensitive = True

# Khởi tạo đối tượng settings để sử dụng toàn dự án
settings = Settings()