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
# source: [(10, 1854), (326, 1956), (852, 2065), (1602, 2127), (2244, 2105), (2999, 1999), (3531, 1855),
#          (3831, 1740), (1905, 1456), (1897, 1039), (396, 881), (1887, 765), (3399, 779), (868, 546),
#          (1876, 457), (2906, 483), (1135, 393), (1881, 331), (2632, 345)]
# target: [(154, 428), (153, 546), (153, 674), (153, 802), (150, 898), (150, 1028), (153, 1155),
#          (153, 1267), (316, 851), (528, 856), (740, 144), (742, 857), (742, 1557), (1334, 144),
#          (1332, 848), (1334, 1559), (1920, 145), (1924, 854), (1924, 1559)]