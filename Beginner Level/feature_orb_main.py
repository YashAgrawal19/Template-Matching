import cv2
import numpy as np
from feature_orb import get_corrected_img
import time


if __name__ == "__main__":

	parle = cv2.imread("images/template_image.png",0)
    #image_guitar = cv2.resize(image_guitar,(640,480))

	target = cv2.imread("images/test_image1.png")
	frame = target.copy()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	start_time = time.time()
	orb = cv2.ORB_create(nfeatures=20000)
	kp1, des1 = orb.detectAndCompute(parle, None)

	default = True
	while default:
		coord, default = get_corrected_img(parle,orb,kp1,des1, frame)
		if default == False:
			break
		#print(coord)

		frame = cv2.fillPoly(frame,coord,color=(0,0,0))
		target = cv2.polylines(target,coord,True,(0,255,0),1, cv2.LINE_AA)
		
		if cv2.waitKey(1) == ord('q'):
            		break
	
	cv2.imshow("target",target)
	
	cv2.waitKey(0)

