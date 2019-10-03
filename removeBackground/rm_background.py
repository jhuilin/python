from removebg import RemoveBg
import os
import cv2

path = os.getcwd()
rmbg = RemoveBg("m9wEPPT5bA2oaYh85jyFTMhS","error.log")
result = rmbg.remove_background_from_img_file("%s/%s"%(path,"me.jpg"))
