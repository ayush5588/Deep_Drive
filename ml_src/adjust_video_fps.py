import cv2
import numpy as np
# import matplotlib.pyplot as plt
import tflite_runtime.interpreter as tflite
interpreter = tflite.Interpreter(model_path="/home/pi/Desktop/models/distracted_driver.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

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
            input_data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            input_data = (input_data / 255).astype(np.float32)
            input_data = np.expand_dims(input_data, -1)
            input_data = np.expand_dims(input_data, 0)
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            tflite_results = interpreter.get_tensor(output_details[0]['index'])
            cpred = np.argmax(tflite_results, axis=1)
            print(cpred)
            # input_data = cv2.resize(input_data, (256, 256))
            # print(frame.shape)
            # break
            # # plt.imshow(frame, cmap="gray")
            # plt.show()
    # return frame

frames = adjust_video_fps()
# print(frames)


