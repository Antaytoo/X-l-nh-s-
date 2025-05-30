import cv2
import numpy as np

# Đọc ảnh gốc
image = cv2.imread('bird.png')

# Kiểm tra nếu ảnh không được nạp đúng
if image is None:
    print("Không thể đọc ảnh.")
    exit()

# Tách các kênh màu B, G, R
B, G, R = cv2.split(image)

# Tạo ảnh chỉ có màu đỏ (Red)
red_image = cv2.merge([np.zeros_like(B), np.zeros_like(G), R])
cv2.imwrite('anh_do.png', red_image)

# Tạo ảnh chỉ có màu xanh lá (Green)
green_image = cv2.merge([np.zeros_like(B), G, np.zeros_like(R)])
cv2.imwrite('anh_xanh_la.png', green_image)

# Tạo ảnh chỉ có màu xanh dương (Blue)
blue_image = cv2.merge([B, np.zeros_like(G), np.zeros_like(R)])
cv2.imwrite('anh_xanh_duong.png', blue_image)

print("Đã lưu 3 ảnh với 3 màu khác nhau.")
