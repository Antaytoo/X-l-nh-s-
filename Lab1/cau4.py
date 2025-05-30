import cv2
import numpy as np

# Bước 1: Nạp ảnh
image = cv2.imread('bird.png')  # Thay 'ten_anh.jpg' bằng tên file ảnh của bạn

# Bước 2: Chuyển sang HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)

# Bước 3: Thay đổi kênh H và V
hsv_image[:, :, 0] = (1/3) * hsv_image[:, :, 0]
hsv_image[:, :, 2] = (3/4) * hsv_image[:, :, 2]

# Giới hạn giá trị H: [0,179] và S, V: [0,255]
hsv_image[:, :, 0] = np.clip(hsv_image[:, :, 0], 0, 179)
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1], 0, 255)
hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2], 0, 255)

# Chuyển về kiểu uint8
hsv_image = hsv_image.astype(np.uint8)

# Bước 4: Chuyển lại sang BGR để lưu ảnh
result_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('bird.png', result_image)

print("Đã lưu ảnh mới với H = 1/3 H_old và V = 3/4 V_old.")
