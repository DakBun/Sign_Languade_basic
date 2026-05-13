import cv2
from ..core.logging import logger
from ..core.config import settings

# Import đúng các Class từ ai_modules theo nội dung .pyc
from ai_modules import HandDetector, FeatureExtractor, DataPreprocessor, SignClassifier

class DetectionService:
    def __init__(self):
        # Khởi tạo các instance từ Class
        self.detector = HandDetector(max_hands=1, detection_con=0.7)
        self.extractor = FeatureExtractor()
        self.preprocessor = DataPreprocessor(window_size=5)
        self.classifier = SignClassifier(model_path=settings.MODEL_PATH)
        
        logger.info("Bộ não nhận diện đã được đồng bộ hóa với AI Modules!")

    def process_frame(self, frame):
        # 1. Tìm tay
        # Lưu ý: Theo .pyc, find_hands trả về img đã vẽ landmarks
        frame = self.detector.find_hands(frame)
        lm_list = self.detector.find_position(frame) # Lấy danh sách tọa độ
        
        label = "Unknown"
        confidence = 0.0

        if lm_list:
            try:
                # 2. Trích xuất (Dùng instance extractor)
                # Chuyển đổi lm_list sang định dạng mà extractor yêu cầu nếu cần
                features = self.extractor.extract_features(self.detector.results.multi_hand_landmarks[0].landmark)
                
                # 3. Tiền xử lý (Dùng instance preprocessor)
                normalized_data = self.preprocessor.normalize(features)
                
                # 4. Dự đoán
                label, confidence = self.classifier.predict(normalized_data)
                
                # Lọc nhiễu kết quả
                label = self.preprocessor.smooth_prediction(label)

            except Exception as e:
                logger.error(f"Lỗi logic AI: {str(e)}")

        return frame, label, confidence

# Khởi tạo instance duy nhất cho toàn hệ thống
detection_service = DetectionService()