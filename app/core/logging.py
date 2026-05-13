import logging
import sys
from pathlib import Path

# Tạo thư mục logs nếu chưa tồn tại
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Cấu hình định dạng log
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logging():
    """Thiết lập hệ thống logging cho toàn dự án."""
    
    # Tạo logger chính
    logger = logging.getLogger("sign_language_app")
    logger.setLevel(logging.INFO)

    # 1. Ghi log ra Console (Để theo dõi khi dev)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(console_handler)

    # 2. Ghi log ra File (Để truy vết lỗi sau này)
    file_handler = logging.FileHandler(LOG_DIR / "app.log", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(file_handler)

    return logger

# Khởi tạo logger dùng chung cho toàn dự án
logger = setup_logging()