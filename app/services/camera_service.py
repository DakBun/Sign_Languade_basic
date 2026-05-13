import cv2
import threading
from ..core.config import settings
from ..core.logging import logger

class CameraManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(CameraManager, cls).__new__(cls)
                cls._instance.camera = None
                cls._instance.is_running = False
                cls._instance.device_index = settings.CAMERA_DEVICE_INDEX
        return cls._instance

    def start(self):
        """Khởi tạo webcam."""
        if not self.is_running:
            self.camera = cv2.VideoCapture(self.device_index)
            if not self.camera.isOpened():
                logger.error(f"Không thể mở camera tại index {self.device_index}")
                return False
            
            # Cấu hình độ phân giải từ file config
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, settings.FRAME_WIDTH)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, settings.FRAME_HEIGHT)
            
            self.is_running = True
            logger.info(f"Camera đã được kích hoạt thành công (Index: {self.device_index})")
            return True
        return True

    def stop(self):
        """Giải phóng webcam."""
        if self.is_running:
            self.is_running = False
            if self.camera:
                self.camera.release()
            logger.info("Camera đã được tắt và giải phóng tài nguyên.")

    def generate_frames(self):
        """Generator trả về từng frame dưới dạng bytes để stream qua API."""
        while self.is_running:
            success, frame = self.camera.read()
            if not success:
                logger.warning("Không thể đọc frame từ camera.")
                break
            else:
                # Tại đây Ngài có thể chèn thêm logic xử lý AI trước khi stream
                # Ví dụ: vẽ landmarks lên frame
                
                ret, buffer = cv2.imencode('.jpg', frame)
                frame_bytes = buffer.tobytes()
                
                # Trả về dữ liệu theo định dạng multipart cho StreamingResponse
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Khởi tạo instance duy nhất
camera_manager = CameraManager()