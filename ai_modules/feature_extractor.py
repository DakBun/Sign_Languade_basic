import numpy as np

class FeatureExtractor:
    def __init__(self):
        # Mỗi bàn tay có 21 landmarks, mỗi landmark có tọa độ (x, y)
        # Tổng cộng chúng ta sẽ có 42 đặc trưng (features)
        self.num_landmarks = 21

    def extract_features(self, landmarks):
        """
        Chuyển đổi danh sách landmarks từ Mediapipe thành một vector phẳng.
        Input: landmarks (đối tượng hand_lms.landmark từ Mediapipe)
        Output: list các tọa độ [x1, y1, x2, y2, ..., x21, y21]
        """
        data_aux = []
        x_values = []
        y_values = []

        # Bước 1: Thu thập tất cả tọa độ x, y
        for i in range(len(landmarks)):
            x = landmarks[i].x
            y = landmarks[i].y
            x_values.append(x)
            y_values.append(y)

        # Bước 2: Chuẩn hóa (Normalization) 
        # Lấy tọa độ tương đối so với điểm nhỏ nhất để mô hình không bị 
        # ảnh hưởng bởi vị trí bàn tay trong khung hình (trái/phải/trên/dưới)
        min_x = min(x_values)
        min_y = min(y_values)

        for i in range(len(landmarks)):
            data_aux.append(landmarks[i].x - min_x)
            data_aux.append(landmarks[i].y - min_y)

        return data_aux

    def get_42_landmarks(self, hand_lms):
        """
        Hàm tiện ích để lấy nhanh 42 tọa độ đã được xử lý
        """
        return self.extract_features(hand_lms.landmark)


# Khởi tạo instance và tạo hàm helper
feature_extractor = FeatureExtractor()

def extract_features(landmarks):
    """
    Hàm helper để trích xuất đặc trưng từ landmarks.
    """
    return feature_extractor.extract_features(landmarks)