# %% Read stream

# Works with 'capture_stream.py' example from picamera2 repo.
# Note: capture_stream.py needs to be started before this script.

# %% Import cv2

import cv2

# %%

def capture_h265_stream():
    image_filename = 'test_file'
    camera_username = 'test_user'
    camera_password = 'test_pw'
    camera_ip = '192.168.0.50'
    
    # cap = cv2.VideoCapture(f'rtsp://{camera_username}:{camera_password}@{camera_ip}/streamX')
    cap = cv2.VideoCapture(f'http://raspberrypi.local:10001')

    while not cap.isOpened():
        ...

    while cap.isOpened():
        ret, frame = cap.read()
        if frame is not None:
            cv2.imwrite(f"{image_filename}.png", frame)
            print(f'Successfully wrote a file')
        break

    cap.release()
    return frame


# %%

frame = capture_h265_stream()


# %%
