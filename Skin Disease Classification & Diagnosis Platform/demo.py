import cv2
import os

path = "./Dataset/HAM10000_images_part_1"


for image in os.listdir(path):
    img_path = path + "/" + image
    img = cv2.imread(img_path)

    cv2.imshow("Images", img)
    cv2.waitKey(0) 
