import cv2
import numpy as np

# Đọc ảnh gốc
image = cv2.imread('bird.png')

# Kiểm tra ảnh có đọc được không
if image is None:
    print("Không thể đọc ảnh.")
    exit()

# Chuyển ảnh sang hệ HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Tách các kênh H, S, V
H, S, V = cv2.split(hsv_image)

# Tạo ảnh chỉ có kênh Hue (H)
hue_image = cv2.merge([H, np.zeros_like(S), np.zeros_like(V)])
hue_image_bgr = cv2.cvtColor(hue_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('bird.png', hue_image_bgr)

# Tạo ảnh chỉ có kênh Saturation (S)
sat_image = cv2.merge([np.zeros_like(H), S, np.zeros_like(V)])
sat_image_bgr = cv2.cvtColor(sat_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('bird.png', sat_image_bgr)

# Tạo ảnh chỉ có kênh Value (V)
val_image = cv2.merge([np.zeros_like(H), np.zeros_like(S), V])
val_image_bgr = cv2.cvtColor(val_image, cv2.COLOR_HSV2BGR)
cv2.imwrite('bird.png', val_image_bgr)

print("Đã lưu 3 ảnh HSV với 3 màu khác nhau.")
