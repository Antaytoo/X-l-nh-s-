import cv2
import numpy as np

# Bước 1: Nạp ảnh
image = cv2.imread('bird.png')  # Thay bằng đường dẫn ảnh thật

# Bước 2: Chuyển sang HSV và chuyển kiểu float để tính toán chính xác
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)

# Bước 3: Thay đổi các kênh
# H_new = (H + 60) % 180
hsv_image[:, :, 0] = (hsv_image[:, :, 0] + 60) % 180

# S_new = S * 1.2, giới hạn tối đa 255
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * 1.2, 0, 255)

# V_new = V * 0.8
hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * 0.8, 0, 255)

# Bước 4: Chuyển lại về uint8 và BGR để lưu
hsv_image = hsv_image.astype(np.uint8)
result_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Bước 5: Lưu ảnh mới
cv2.imwrite('bird.jpg', result_image)

print("Đã xử lý và lưu ảnh với H+60, S*1.2, V*0.8")
