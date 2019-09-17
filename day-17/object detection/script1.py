import cv2
import time
from datetime import datetime
import pandas
first_frame=None
satatus_list=[None, None]
times=[]
df=pandas.DataFrame(columns=['Start_time','End_time'])
video=cv2.VideoCapture(0)

while True:

    check, frame=video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_delta, None, iterations=2)
    (cnts,_) =cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for countour in cnts:
        if cv2.contourArea(countour)<10000:
            continue
        status=1

        (x, y, w,h)=cv2.boundingRect(countour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    satatus_list.append(status)
    if satatus_list[-1]==1 and satatus_list[-2]==0:
        times.append(datetime.now())
    cv2.imshow("colour frame", frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print(satatus_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("timing.csv")
video.release()
cv2.destroyAllWindows
