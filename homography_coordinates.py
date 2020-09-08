import cv2


def click_and_mark(event, x, y, flags, params):
    global coordinates, counter
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        cv2.circle(img, (x, y), 15, (0, 0, 255), -1)
        cv2.putText(img, str(counter), (x+15, y-5), font, 2, (0, 0, 255), 2)
        counter += 1


img1_path = './data/game1_frame.jpg'
img2_path = './data/FHFIELD.jpg'

for path in [img1_path, img2_path]:
    coordinates = []
    counter = 1
    img = cv2.imread(path)

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', click_and_mark)
    while True:
        cv2.imshow('Image', img)
        key = cv2.waitKey(0) & 0xFF
        if key == 27 or key == ord('n'):
            print(coordinates)
            cv2.imwrite(path[:-4] + '_marked.jpg', img)
            break
    cv2.destroyAllWindows()

# For my video and field I found the following coordinates:
# source: [(9, 1854), (324, 1954), (852, 2064), (1601, 2127), (2245, 2108), (2998, 2003),
# (3530, 1853), (3829, 1739), (1908, 1456), (394, 883), (3403, 781), (870, 546), (2900, 482)]
# target: [(151, 430), (153, 549), (153, 676), (153, 803), (151, 895), (153, 1027), (153, 1156),
# (153, 1275), (316, 851), (741, 145), (740, 1559), (1333, 144), (1333, 1559)]
