import numpy as np

class DataPreprocessor:
    def __init__(self, window_size=5):
        """
        Khởi tạo bộ tiền xử lý.
        :param window_size: Kích thước cửa sổ để lọc nhiễu (Moving Average).
        """
        self.window_size = window_size
        self.history = []

    def normalize(self, features):
        """
        Chuẩn hóa vector đặc trưng về dải [0, 1].
        """
        features = np.array(features)
        min_val = np.min(features)
        max_val = np.max(features)
        
        if max_val - min_val == 0:
            return features.tolist()
            
        normalized = (features - min_val) / (max_val - min_val)
        return normalized.tolist()

    def smooth_prediction(self, new_prediction):
        """
        Lọc nhiễu kết quả dự đoán bằng cách lấy kết quả xuất hiện nhiều nhất 
        trong các khung hình gần nhất (giúp nhãn không bị nhảy liên tục).
        """
        self.history.append(new_prediction)
        if len(self.history) > self.window_size:
            self.history.pop(0)
            
        # Trả về nhãn xuất hiện nhiều nhất trong lịch sử
        return max(set(self.history), key=self.history.count)

    def process(self, features):
        """
        Tổng hợp các bước xử lý dữ liệu.
        """
        # 1. Khử nhiễu hoặc chuẩn hóa sâu hơn nếu cần
        processed_features = self.normalize(features)
        
        return processed_features