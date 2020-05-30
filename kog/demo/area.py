import cv2 as cv
import numpy as np

# canny边缘检测
def canny_demo(image):
    t = 140
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    cv.imwrite("../img/canny_output.png", canny_output)
    return canny_output

# 读取图像
src1 = cv.imread("../img/screen.png")
src2 = cv.imread("../img/img_mask.png")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src1)

# 调用
binary = canny_demo(src2)


# 轮廓发现
contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    # 面积
    area = cv.contourArea(contours[c])
    # 周长
    arclen = cv.arcLength(contours[c], True)
    # 矩形
    rect = cv.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    box = np.int0(box)

    # 轮廓描绘
    cv.drawContours(src1,[box],0,(0,255,0),2)
    cv.circle(src1, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)
    cv.drawContours(src1, contours, c, (0, 0, 255), 2, 8)
    cv.putText(src1, "area:" + str(area), (50, 50), cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 1);
    cv.putText(src1, "arclen:" + str(arclen), (50, 80), cv.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 1);

# 图像显示
cv.imshow("contours_analysis", src1)
cv.imwrite("../img/contours_analysis.png", src1)
cv.waitKey(0)
cv.destroyAllWindows()