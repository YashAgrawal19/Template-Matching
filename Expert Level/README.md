
ABOUT THE FOLDER

The sift.py and sift_expert.py are 2 main files with 2 techniques here the technique is same just change the 1 parameter for different results

sift_feature.py is the supporting file which contain a fuction for detecting the template image in the test_image. This fuction return the coordinate point of portion of the test_image which matches with the template image along with a boolean value for representing that the template image is present in the test_image

image folder contain the images used in the files. All the names of the images are given in the file itself so no need to pass any argument while compiling

As we have multiple template images therefor I have used os library to read all the images present in the images/templates/ folder 




HOW TO COMPILE


RUN python sift.py

here we need to change MIN_MATCH_COUNT  parameter to 20 which is present on the top of the file sift_feature.py

RUN python sift_expert.py

Here the MIN_MATCH_COUNT parameter value is kept at 25 





OUTPUT

While runnig the sift.py file the output will be sift_result.png in the output folder

While runnig the sift_expert.py file the output will be sift_expert_result.png in the output folder



WHY USED THIS TECHNIQUE

This sift detector has been used with flann matcher as in this level the image is not straight as well as not of the same size as well as there are many other objects are present.






