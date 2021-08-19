
ABOUT THIS FOLDER

The feature_orb_main.py is the main file which we have to run for the output.

feature_orb.py is the supporting file which contain a fuction for detecting the template image in the test_image.
This fuction return the coordinate point of portion of the test_image which matches with the template image along with a 
boolean value for representing that the template image is present in the test_image

image folder contain the images used in the files. All the names of the images are given in the file itself so no need to pass any argument while compiling

template_image.png is the template image and test_image.png is the test_image


HOW TO COMPILE

RUN python feature_orb_main.py

OUTPUT

output of the image is present in the output folder with the name resulted_image.png


WHY USED THIS TECHNIQUE

This orb detector has been used because it is fast and also flann matcher is used as in this level the all the image is of same type as there is no tiltes of other
object are present in the test_image therefor the computation time as well as the accuracy will increase when using flann matcher with orb detector rather than any other detector.


















