import argparse
import cv2
import imutils
# Download the image used for this tutorial from here.
# http://goo.gl/jsYXl8

# Read the image
ap = argparse.ArgumentParser();
ap.add_argument("--input", required=False,
	help="path to input image",default="C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\elon_musk_tesla_3036.jpg")
args = vars(ap.parse_args());

# Read the image
image = cv2.imread(args["input"])

# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()