import numpy as np
import cv2 as cv
import glob
import time

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)



cbrow = 9
cbcol = 6

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((cbrow * cbcol, 3), np.float32)
objp[:, :2] = np.mgrid[0:cbcol, 0:cbrow].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.jpg')


cap = cv.VideoCapture(0)

contador = 0
inicio = time.time()

while True:
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    cv.imshow('gray', gray)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (cbrow,cbcol), None)

    # If found, add object points, image points (after refining them)
    

    if ret == True:
        elapsedtime = time.time() - inicio
        if elapsedtime >=2:
        #if cv.waitKey(10) & 0xFF == ord('a'):
            objpoints.append(objp)
            corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
            imgpoints.append(corners)
            
            contador = contador + 1
            inicio = time.time()


        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,f'{contador}', (100,100), font, 1, (255,255,255), 2)
        cv.putText(img,f'{elapsedtime:.2f}', (200,100), font, 1, (255,255,255), 2)



        cv.drawChessboardCorners(img, (cbrow,cbcol), corners, ret)
        cv.imshow('img', img)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break
 
cv.destroyAllWindows()
cap.release()


print(f'Puntos: {len(objpoints)} - {len(imgpoints)} ')

print('Calibrando camara')
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints,imgpoints, gray.shape[::-1], None, None)

print('Camara calibrada')

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv.imshow('original',frame)
    dst = cv.undistort(frame, mtx, dist, None, None)
    cv.imshow('undistorted', dst)

    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()

