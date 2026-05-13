from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import settings

# 1. Lấy URL database từ file config mà chúng ta đã tạo
# Mặc định là sqlite:///./sign_language.db
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# 2. Khởi tạo Engine
# 'check_same_thread': False chỉ cần thiết cho SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Tạo SessionLocal - mỗi instance sẽ là một phiên làm việc với DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class để các Models (như PredictionRecord) kế thừa
Base = declarative_base()

def get_db():
    """
    Dependency function để tạo session cho mỗi request.
    Sau khi dùng xong sẽ tự động đóng kết nối.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()