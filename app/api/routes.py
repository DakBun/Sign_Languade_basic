from fastapi import APIRouter
from . import camera, predict

api_router = APIRouter()

# Đăng ký các router từ các module con
api_router.include_router(camera.router, prefix="/camera", tags=["Camera"])
api_router.include_router(predict.router, prefix="/predict", tags=["Prediction"])

@api_router.get("/")
async def root():
    return {"message": "Sign Language Detection API is running"}