import argparse
import os
import time
import cv2
import numpy as np
from imutils.video import VideoStream
from imutils.video import FPS

# Argument for --name
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--name', help='Put the name of the person.', default="Visitor")
args = arg_parser.parse_args()
person_name = args.name

# Create directory for saving face images
Face_Folder = person_name
if not os.path.exists(Face_Folder):
    os.makedirs(Face_Folder)

# Load the serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('deploy.prototxt.txt', 'face.caffemodel')

# Initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Start the FPS counter
fps = FPS().start()

# Loop over the frames from the video stream
while True:
    # Grab the frame from the threaded video stream and resize it to 320x320
    frame = vs.read()
    frame = cv2.resize(frame, (320, 320))

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (320, 320)), 1.0, (320, 320), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence < 0.8:
            continue
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # Crop the face from the frame
        cropped_face = frame[startY:endY, startX:endX]

        # Save the cropped face image
        current_time = time.strftime("%Y-%m-%d %H-%M-%S")
        image_name = f"{current_time} {person_name}.jpg"
        image_path = os.path.join(Face_Folder, image_name)
        cv2.imwrite(image_path, cropped_face)
        print("Image captured and saved!")

        # Draw the bounding box and confidence on the frame
        text = f"{confidence * 100:.2f}%"
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)

    # Update the FPS counter
    fps.update()

    # Calculate and display the FPS
    fps.stop()
    fps_text = f"FPS: {fps.fps():.2f}"
    cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("VisioAccelerAI Face Crop", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# Stop the FPS counter and display info
fps.stop()
cv2.destroyAllWindows()
vs.stop()
