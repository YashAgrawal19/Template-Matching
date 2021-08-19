import sys # For debugging only
import numpy as np
import cv2
import os
from sift_feature import get_corrected
#from matplotlib import pyplot as plt


file_name = os.listdir("images/templates/")
print(file_name)

target = cv2.imread("images/test_image.png")

for name in file_name:
	img1 = cv2.imread('images/templates/'+name,0) # queryImage
	img1 = cv2.resize(img1,(200,200))
	#img2 = cv2.imread('images/test_image.png',0) # trainImage
	img2 = cv2.imread("images/test_image.png",0)
	
	# Initiate SIFT detector
	sift = cv2.SIFT_create(nfeatures = 10000)

	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(img1,None)

	i=0
	default = True
	while default:
		coord, default = get_corrected(img1,sift,kp1,des1,img2)

		if default == False:
			break
		
		target = cv2.polylines(target,coord,True,(0,255,0),2, cv2.LINE_AA)
		cv2.imshow("target",target)

		img2 = cv2.fillPoly(img2,coord,color=(0,0,0))
		
		if cv2.waitKey(1) == ord('q'):
		    		break


cv2.imwrite("sift_expert_result.png",target)
cv2.waitKey(0)

