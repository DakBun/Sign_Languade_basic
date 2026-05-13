from sqlalchemy.orm import Session
from ..models.prediction import PredictionRecord
from ..schemas.prediction import PredictionCreate
from ..core.logging import logger

def create_prediction_history(db: Session, prediction: PredictionCreate):
    """
    Lưu một kết quả dự đoán mới vào cơ sở dữ liệu.
    """
    try:
        db_prediction = PredictionRecord(
            label=prediction.label,
            confidence=prediction.confidence,
            # Các thông tin bổ sung nếu cần (ví dụ: timestamp tự động tạo)
        )
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        return db_prediction
    except Exception as e:
        db.rollback()
        logger.error(f"Lỗi khi lưu lịch sử dự đoán: {str(e)}")
        return None

def get_prediction_history(db: Session, skip: int = 0, limit: int = 100):
    """
    Lấy danh sách lịch sử các lần dự đoán.
    """
    return db.query(PredictionRecord).offset(skip).limit(limit).all()

def delete_old_history(db: Session):
    """
    Xóa toàn bộ lịch sử để dọn dẹp dữ liệu cũ.
    (Uhahahaha! Dọn dẹp những thứ lỗi thời thôi thưa Ngài!)
    """
    try:
        db.query(PredictionRecord).delete()
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        logger.error(f"Lỗi khi xóa lịch sử: {str(e)}")
        return False