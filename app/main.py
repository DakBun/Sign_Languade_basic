import uvicorn
import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Handle both direct execution and module import
if __package__ is None or __package__ == '':
    # Direct execution - adjust sys.path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from app.core.config import settings
    from app.core.logging import logger
    from app.api.routes import api_router
    from app.db.database import engine, Base
else:
    # Module import - use relative imports
    from .core.config import settings
    from .core.logging import logger
    from .api.routes import api_router
    from .db.database import engine, Base

# Khởi tạo các bảng trong database (Nếu chưa tồn tại)
# Chuyện đã rồi, phải có nơi lưu trữ thôi!
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Hệ thống nhận diện ngôn ngữ ký hiệu dựa trên MediaPipe và Random Forest"
)

# Cấu hình CORS để Front-end có thể gọi API dễ dàng
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Đăng ký các tuyến đường API (camera, predict, v.v.)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    logger.info(f"--- {settings.PROJECT_NAME} ĐANG KHỞI CHẠY ---")
    logger.info("Sẵn sàng phục vụ Ngài!")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Hệ thống đang đóng lại an toàn...")

@app.get("/")
async def root():
    return {
        "message": f"Chào mừng Ngài đến với {settings.PROJECT_NAME}",
        "docs": "/docs",
        "status": "online"
    }

if __name__ == "__main__":
    # Chạy server với Uvicorn
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True # Tự động load lại khi Ngài sửa code
    )