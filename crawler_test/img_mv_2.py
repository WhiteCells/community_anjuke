# pip install opencv-python-headless
import time

import cv2
import numpy as np


def image_gray(image, img_name="white_part.jpg"):
    # 读取图像
    # image = cv2.imread('your_image.jpg')
    # 将图像转换为灰度（可选，但推荐，因为白色在灰度图中也很明显）
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 设置白色阈值（这里假设白色区域的灰度值大于200，可以根据实际情况调整）
    _, white_mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)

    # 使用掩码提取白色区域（这里使用cv2.bitwise_and，但因为我们只需要白色部分，所以直接应用掩码也可以）
    # 注意：cv2.bitwise_and的第三个参数是掩码，但我们需要确保图像和掩码的通道数匹配。
    # 由于gray_image是单通道，我们需要将white_mask也转换为单通道（实际上它已经是了），或者将image转换为灰度图后再应用。
    # 但由于我们已经有了gray_image，所以直接使用它即可。
    white_part = cv2.bitwise_and(gray_image, gray_image, mask=white_mask)

    # 如果想要保留原始图像的彩色信息，可以在BGR空间中操作，但需要先转换回BGR空间再保存
    # 不过，由于我们已经转换为灰度图，并且只关心白色区域，所以直接保存灰度图即可。

    # 存储提取出的白色区域（作为灰度图）
    cv2.imwrite(img_name, white_part)
    return white_part


def white_mask_img(image, img_name='white_part_.jpg'):
    # 读取图像
    # image = cv2.imread('bg1.jpg')

    # 转换颜色空间从BGR到HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义白色的HSV范围（注意：白色通常具有高V值和低S值，H值可以变化）
    # 这里我们设置了一个相对宽松的范围来捕捉白色
    lower_white = np.array([0, 0, 200])  # 最低亮度可以调整，以捕捉更暗的白色
    upper_white = np.array([180, 50, 255])  # 饱和度上限可以调整，以排除接近灰色的像素

    # 生成白色区域的掩码
    white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

    # 实际上，我们应该这样做来保留彩色信息（但只显示白色区域）：
    white_part_color = cv2.bitwise_and(image, image, mask=white_mask)

    # 如果要保存提取的白色区域，可以这样做：
    cv2.imwrite(img_name, white_part_color)
    return white_part_color


# 定义一个函数用于在图像上绘制矩形框，并显示结果
def cv_save_target(img, x1, y1, x2, y2):
    # 在图像上绘制矩形框，颜色为绿色，线条宽度为2
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # 显示处理后的图像
    # cv_show(img, title="res")
    cv2.imwrite(f"output_{x1, y1, x2, y2}_{int(time.time())}.jpg", img)


# 定义一个函数用于显示图像
def cv_show(img, title="img"):
    # 显示图像
    cv2.imshow(title, img)
    # 等待用户按键继续
    cv2.waitKey(0)
    # 关闭所有显示的窗口
    cv2.destroyAllWindows()


bg_path = 'bg3.jpg'
target_path = 'ta3.png'

# 加载背景图像
bg = cv2.imread(bg_path)
# 检查图像是否成功加载
if bg is None:
    print("Error: bg.png 加载失败")
# else:
    # cv_show(bg, "bg")  # 显示背景图像

# 加载目标图像
target = cv2.imread(target_path)
# 检查图像是否成功加载
if target is None:
    print("Error: target.png 加载失败")
# else:
#     cv_show(target, "target")  # 显示目标图像

# bg = image_gray(bg)
# target = image_gray(target, img_name="target_.jpg")
bg = white_mask_img(bg)
target = white_mask_img(target, img_name="target_white_.jpg")
# 对背景图像和目标图像进行边缘检测
bg_canny = cv2.Canny(bg, 70, 200)
target_canny = cv2.Canny(target, 70, 200)
# 显示边缘检测结果
# cv_show(bg_canny, "bg_canny")
# cv_show(target_canny, "target_canny")

# 在背景图像中查找与目标图像匹配的区域
res = cv2.matchTemplate(bg_canny, target_canny, cv2.TM_CCOEFF_NORMED)
# 获取匹配结果的最小值、最大值及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 打印匹配度，最大值越接近1表示匹配度越高
print(f"匹配度: {max_val}")

# 获取目标图像的尺寸（高度和宽度）
height, width = target.shape[:2]

# 计算矩形框的左上角和右下角坐标
x1, y1 = max_loc[0], max_loc[1]
x2, y2 = x1 + width, y1 + height

print("坐标:", x1, y1, x2, y2)
# 在背景图像上绘制匹配区域的矩形框，并显示最终结果
cv_save_target(bg, x1, y1, x2, y2)

