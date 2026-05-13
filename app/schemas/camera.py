from pydantic import BaseModel
from typing import Optional

class CameraStatus(BaseModel):
    """Schema trả về trạng thái hiện tại của camera."""
    is_running: bool
    device_index: int
    message: Optional[str] = None

class CameraSettings(BaseModel):
    """Schema để cập nhật cấu hình camera từ client."""
    device_index: int = 0
    frame_width: int = 640
    frame_height: int = 480