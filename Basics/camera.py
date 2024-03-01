import cv2

# You can add device index or mp4 path
cap = cv2.VideoCapture(0) #using device index either 0 or -1 usually try with 0 if not then -1
fourcc = cv2.VideoWriter_fourcc(*'XVID',)


#Saving the output of video recording 
out = cv2.VideoWriter("Rec.avi",fourcc,20.0,(640,480))


while(cap.isOpened()):
    #while true capture the video frames
    ret,frame=cap.read()

    if(ret):
        #Height and Width will be shown
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #convert it to grayscale color
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Frame1",grayscale)

        #saving the file
        out.write(frame)

        # 0 value capture 1 frame while 1 makes it capture 1fps 
        if (cv2.waitKey(1) & 0xFF==ord("q")):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()