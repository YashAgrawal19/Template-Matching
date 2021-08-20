import cv2
import numpy as np

def get_corrected_img(img_parle,orb,kp1,des1, img_frame):
    
    
	img_frame_ori = img_frame.copy()
	MIN_MATCHES = 60   #50

	kp2, des2 = orb.detectAndCompute(img_frame, None)

	

	index_params= dict(algorithm = 6,
                   table_number = 12, # 12
                   key_size = 20,     # 20
                   multi_probe_level = 2) #2
	search_params = dict(checks=100)#{}
	
	'''
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks=100)   # or pass empty dictionary	
	'''

	flann = cv2.FlannBasedMatcher(index_params, search_params)
	matches = flann.knnMatch(des1, des2, k=2)

	#print(matches[0], len(matches))

	good_matches = []
	matches = [match for match in matches if len(match) == 2]
	for m, n in matches:
		if m.distance < 0.8 * n.distance:   #75
			good_matches.append(m)

	default = False
	coordinate = []

	if len(good_matches) > MIN_MATCHES:
		src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
		dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)
		M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
		matchesMask = mask.ravel().tolist()
		h,w = img_parle.shape
		pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
		dst = cv2.perspectiveTransform(pts,M)
		coordinate = np.int32(dst)
		default = True
	else:
		print( "Not enough matches are found - {}/{}".format(len(good_matches), MIN_MATCHES) )
		matchesMask = None

	draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                    singlePointColor = None,
                    matchesMask = matchesMask, # draw only inliers
                    flags = 2)
	img_feature = cv2.drawMatches(img_parle,kp1,img_frame,kp2,good_matches,None,**draw_params)
	#cv2.imshow("img_feature",img_feature)
	return [coordinate], default

