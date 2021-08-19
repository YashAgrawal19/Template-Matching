
HOW TO COMPILE

The feature_orb_main.py is the main file which we have to run for the output.

feature_orb is the supporting file which contain a fuction for detecting the template image in the test_image.
This fuction return the coordinate point of portion of the test_image which matches with the template image along with a 
boolean value for representing that the template image is present in the test_image

OUTPUT

output of the image is present in the output folder 

WHY USED THIS TECHNIQUE

This orb detector has been used because it is fast and also flann matcher is used as in this level the all the image is of same type as there is no tiltes of other
object are present in the test_image therefor the computation time as well as the accuracy will increase when using flann matcher with orb detector rather than any other detector.


















