import cv2
import matplotlib.pyplot as plt
def adjust_video_fps():
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    point_ = []
    count = 0
    while(cap.isOpened() and count <1) :
        ret, frame = cap.read()
        frame_count += 1
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if(frame_count % int(fps) == 0):
            print("Reading per second %d"%(frame_count))
            frame = cv2.resize(frame, (256,256))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # print(frame.shape)
            # break
            # # plt.imshow(frame, cmap="gray")
            # plt.show()
    return frame

frames = adjust_video_fps()
# print(frames)


