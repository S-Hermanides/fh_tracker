# Field hockey player tracker

Hello and welcome to the code for my field hockey player tracker. 
This tracker has 4 stages and the code is organized as follows:
* Detection using Yolo v4. Most of the code for yolo v4 resides in the "core" folder
* Tracking using DeepSORT. The classes for this part can be found in the "deep_sort" folder
* Color detection. I added the code for this into the deep_sort folder and adjusted the deepSORT 
classes to work with it. The main function can be found in color_detect.py
* I created the homography_coordinates.py script to do camera calibration and added it to the main folder.
The rest of the transformation happens inside the object_tracker.py script

## Running the tracker

I recommend using Google Colab to run the tracker, since it gives acces to a GPU for free.

1. To run the tracker, first clone this repository by running the following command:
```!git clone https://github.com/S-Hermanides/fh_tracker```

2. Download pre-trained yolov4.weights file [here](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT)
Copy and paste yolov4.weights from your downloads folder into the 'data' folder of this repository.

3. Create the Yolo v4 model by running the following command in the terminal:  
```!python save_model.py --model yolov4```  
This converts the weights into a tensorflow model that's ready to be used

4. Run the tracker with the following command, replacing the parts in <brackets> with your information:  
```!python object_tracker.py --video '<input_video_path> --output <output_video_path> --output_2 <output_map_view_path> --jersey_colors <list_of_colors>```  
There are a number of parameters to tune. Below is a list and an example of how I achieved my final result.

```
# These variables are most likely to be changing

# Input jersey colors to identify teams: Team1, Team2
jersey_colors = 'white','blue'

# score threshold is a hyperparameter for Yolo, the confidence score of a detection being a certain class.
score_threshold = 0.5

# Colab can't show video, so set flag to True if you are using a GPU on Google Colab
dont_show_flag = True

# iou threshold is a deepsort hyperparameter, Intersection over Union (predicted versus actual detection box overlap). High value means high chance the boxes are the same detection. 0.45 is default
iou_threshold = 0.45
# max cosine distance is used by deepsort to re-identify detections after losing them (based on the extracted 'appearance' detection vector)
max_cosine_distance = 0.4
# max age is the number of frames that can be "missed" before a unique detection ID is considered dead. Tune if the same object gets multiple IDs. Default is 60
max_age_par = 60
# Number of consecutive detections before the track is confirmed. Default is 3
n_init_par = 3

# If not None, fix samples per class to at most this number. Removes the oldest samples when the budget is reached.
nn_budget = None
# nms is a method to prevent multiple detections for the same object. threshold values often used are 0.3-0.5. Tune if multiple boxes appear
nms_max_overlap = 1.0
```