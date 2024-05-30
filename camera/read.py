# %% Read stream

# Works with 'capture_stream.py' example from picamera2 repo.
# Note: capture_stream.py needs to be started before this script.

# %% Import cv2

import cv2
import matplotlib.pyplot as plt

# %%

def capture_h265_stream():
    image_filename = 'test_file'
    camera_username = 'test_user'
    camera_password = 'test_pw'
    camera_ip = '192.168.0.50'
    
    # cap = cv2.VideoCapture(f'rtsp://{camera_username}:{camera_password}@{camera_ip}/streamX')
    cap = cv2.VideoCapture(f'http://raspberrypi.local:10001')

    idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is not None:
            # cv2.imwrite(f"{image_filename}_{idx}.png", frame)
            print(f'Successfully wrote a file')
            idx += 1

            if idx > 10:
                break


    cap.release()
    return frame


# %%

frame = capture_h265_stream()


# %%

# Revert RGB
frame=frame[:,:,::-1]

plt.figure('frame')
plt.clf()
plt.imshow(frame)
plt.show()
# %%
