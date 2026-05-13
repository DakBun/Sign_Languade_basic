from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
# Import camera_manager từ layer services để điều khiển phần cứng
from ..services.camera_service import camera_manager

router = APIRouter()

@router.get("/start")
async def start_camera():
    """Khởi tạo và mở kết nối với Camera."""
    # Gọi service để chiếm quyền điều khiển webcam
    success = camera_manager.start()
    if not success:
        raise HTTPException(status_code=500, detail="Không thể khởi động Camera. Vui lòng kiểm tra kết nối phần cứng.")
    return {"status": "success", "message": "Camera đã được kích hoạt."}

@router.get("/stop")
async def stop_camera():
    """Giải phóng tài nguyên Camera."""
    # Giải phóng webcam để các ứng dụng khác có thể sử dụng
    camera_manager.stop()
    return {"status": "success", "message": "Camera đã được tắt an toàn."}

@router.get("/stream")
async def video_feed():
    """
    Endpoint trả về luồng video trực tiếp (MJPEG).
    Sử dụng StreamingResponse để truyền frame liên tục từ camera_service.
    """
    if not camera_manager.is_running:
        raise HTTPException(status_code=400, detail="Camera chưa được khởi động. Hãy gọi /start trước.")
    
    return StreamingResponse(
        camera_manager.generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

@router.get("/status")
async def get_status():
    """Kiểm tra trạng thái hiện tại của thiết bị camera."""
    return {
        "active": camera_manager.is_running,
        "info": "Đang hoạt động" if camera_manager.is_running else "Đang tắt"
    }