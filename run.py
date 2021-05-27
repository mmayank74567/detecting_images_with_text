from detecting_text.detecting_text_in_images import DetectingText
import cv2
import argparse

apo = argparse.ArgumentParser()
apo.add_argument("--image", required = True, help = "Path to the image")
apo.add_argument("--model", required = True, help = "Path to the model")
args = vars(apo.parse_args())

image = cv2.imread(args["image"])
object1 = DetectingText(args["model"])
box = object1.east_detection(image)

