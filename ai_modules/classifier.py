import pickle
import numpy as np
import os

class SignClassifier:
    def __init__(self, model_path='models_store/model.p'):
        """
        Khởi tạo bộ phân loại.
        :param model_path: Đường dẫn tới file model đã train (Random Forest, SVM, v.v.)
        """
        self.model = None
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        """
        Nạp mô hình từ đĩa vào bộ nhớ.
        """
        if os.path.exists(self.model_path):
            try:
                model_dict = pickle.load(open(self.model_path, 'rb'))
                self.model = model_dict['model']
                print(f"--- Model loaded successfully from {self.model_path} ---")
            except Exception as e:
                print(f"--- Error loading model: {e} ---")
        else:
            print(f"--- Warning: Model file not found at {self.model_path}. Please train the model first. ---")

    def predict(self, features):
        """
        Dự đoán nhãn từ vector đặc trưng.
        :param features: List 42 tọa độ đã qua xử lý.
        :return: Nhãn dự đoán (string hoặc int) và độ tin cậy.
        """
        if self.model is None:
            return "No Model", 0.0

        # Chuyển đổi list thành mảng numpy 2D (1 mẫu, N đặc trưng)
        input_data = np.asarray(features).reshape(1, -1)
        
        # Thực hiện dự đoán
        prediction = self.model.predict(input_data)
        
        # Lấy xác suất nếu mô hình hỗ trợ (tùy chọn)
        try:
            proba = self.model.predict_proba(input_data)
            confidence = np.max(proba)
        except:
            confidence = 1.0  # Mặc định là 1 nếu không lấy được xác suất

        return prediction[0], confidence


# Khởi tạo instance duy nhất cho classifier
sign_classifier = SignClassifier()