import cv2

cap = cv2.VideoCapture(2, cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


while True:
    _, frame = cap.read()

    cv2.imshow('test',frame)

    if cv2.waitKey(16) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
