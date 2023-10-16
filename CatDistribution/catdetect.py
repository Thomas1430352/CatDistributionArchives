import pixellib
from pixellib.instance import instance_segmentation
import cv2

segmentation_model = instance_segmentation()
segmentation_model.load_model('C:\Users\thoma\Documents\CatDistribution')
segmask, output = segmentation_model.segmentImage('C:\Users\thoma\Documents\CatDistribution\cat iamges\cat1.jpg', extract_segmented_objects=True, save_extracted_objects= True, show_bboxes= True, output_image_name="C:\Users\thoma\Documents\CatDistribution\cat iamges\cat1.jpg")

cv2.imshow('img' , output)
cv2.waitKey(0)