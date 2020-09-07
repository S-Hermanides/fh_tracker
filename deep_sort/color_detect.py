import cv2
import numpy as np

def find_color(roi, colors, threshold=0.0):
  """
  Generates a percentage of each jersey color in the roi. If at least one is
  above threshold, returns the color with the highest percentage, otherwise
  returns None.

  roi: image or region of interest within image
  colors: list of colors as strings in order [Team1, Team2, ref or other]
  threshold: minimum fraction of image containing either of the colors necessary to be detected
  """

  color_dict = {'white': [[80, 0, 100], [180, 100, 255]],
                'red': [[170, 50, 50], [180, 255, 255], [0, 50, 50], [10, 255, 255]],
                'yellow': [[20, 50, 50], [30, 255, 255]],
                'green': [[50, 50, 50], [80, 255, 255]],
                'blue': [[81, 50, 50], [125, 255, 255]],
                'light blue': [[90, 100, 50], [125, 255, 180]],
                'dark blue': [[106, 50, 50], [125, 255, 255]],
                'purple': [[126, 50, 50], [140, 255, 255]],
                'pink': [[141, 50, 50], [169, 255, 255]],
                'orange': [[8, 50, 50], [40, 255, 255]],
                'black': [[0, 0, 0], [180, 40, 20]],
                'grey': [[0, 0, 21], [180, 25, 160]]}

  roi_hsv = cv2.cvtColor(roi, cv2.COLOR_RGB2HSV)
  total_pixels = roi.shape[0] * roi.shape[1]
  highest_color = None
  highest_perc = 0
  for color in colors:
    if color in color_dict.keys():
      # red is on the edge of HSV range, so needs a combination of two masks
      if color == 'red':
        lower1 = np.array(color_dict[color][0])
        upper1 = np.array(color_dict[color][1])
        lower2 = np.array(color_dict[color][2])
        upper2 = np.array(color_dict[color][3])
        mask = cv2.inRange(roi_hsv, lower1, upper1) + cv2.inRange(roi_hsv, lower2, upper2)
      else:
        lower = np.array(color_dict[color][0])
        upper = np.array(color_dict[color][1])
        mask = cv2.inRange(roi_hsv, lower, upper)
      color_perc = cv2.countNonZero(mask) / total_pixels
      if color_perc > highest_perc and color_perc > threshold:
        highest_perc = color_perc
        highest_color = color
    else:
      print(f'{color} not in color dictionary')
      break
  return highest_color