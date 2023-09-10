import cv2 as cv
cap = cv.VideoCapture('E:\Projects\Pruthvi Tata IQ\Dataset\CV\S2.avi')

fourcc = cv.VideoWriter_fourcc(*'PIM1')
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv.CAP_PROP_FPS))
Writer = cv.VideoWriter('S2_HSV.avi', fourcc, fps, (width, height))

for i in range(int(cap.get(cv.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    HSV = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
    Writer.write(HSV)

    if(cv.waitKey(1) & 0xFF == ord('q')):
        break

print('Output Done')
cap.release()
Writer.release()
cv.destroyAllWindows()

