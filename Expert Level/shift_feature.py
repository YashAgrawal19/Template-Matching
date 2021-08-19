import sys # For debugging only
import numpy as np
import cv2
#from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 25


def get_corrected(img11,sift,kp1,des1,frame):

	kp2, des2 = sift.detectAndCompute(frame,None)

	FLANN_INDEX_KDTREE = 1
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 100)

	flann = cv2.FlannBasedMatcher(index_params, search_params)

	matches = flann.knnMatch(des1,des2,k=2)




	good_matches = []
	matches = [match for match in matches if len(match) == 2]
	for m, n in matches:
		if m.distance < 0.8 * n.distance:   #75
			good_matches.append(m)

	default = False
	coordinate = []

	if len(good_matches) > MIN_MATCH_COUNT:
		src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
		dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
		matchesMask = mask.ravel().tolist()
		h,w = img11.shape
		pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
		dst = cv2.perspectiveTransform(pts,M)
		coordinate = np.int32(dst)
		default = True
	else:
		print( "Not enough matches are found - {}/{}".format(len(good_matches), MIN_MATCH_COUNT) )
		matchesMask = None
	draw_params = dict(matchColor = (0,255,0), # draw matches in green color
		            singlePointColor = None,
		            matchesMask = matchesMask, # draw only inliers
		            flags = 2)
	img_feature = cv2.drawMatches(img11,kp1,frame,kp2,good_matches,None,**draw_params)
	#cv2.imshow("img_feature",img_feature)

	return [coordinate], default
