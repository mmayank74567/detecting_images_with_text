from detecting_text.detecting_text_in_images import DetectingText
from imutils import paths
import argparse
import shutil
import cv2

apo = argparse.ArgumentParser()
apo.add_argument("--model", required = True, help = "Path to the model")
apo.add_argument("--imagepath", required = True, help = "Path to the folder of images")
apo.add_argument("--output", required = True, help = "Path to the output folder of images with text")
args = vars(apo.parse_args())

object1 = DetectingText(args["model"])
counter = 0
path_list = list(paths.list_images(args["imagepath"]))
for i in path_list:
    image = cv2.imread(i)

    box = object1.east_detection(image)
    if box>0:
        try: 
            shutil.copy(i, args["output"])
            counter = counter + 1 
            print("[INFORMATION] Found text in the image {}. Copying to the output folder.".format(i))
        except:
            print("Error processing")
print("[INFORMATION] Done. Total images found with text: {}".format(counter))
        
    