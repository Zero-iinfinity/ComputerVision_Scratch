import cv2 as cv
import numpy as np
import tensorflow as tf
import time

IMG_SIZE = 244  # Changed from 224 to 244 to match your model
class_names = ['without mask', 'with mask']

# Load your trained model
model = tf.keras.models.load_model("mask_detector.h5")

cam = cv.VideoCapture(0)


prev_time = time.time()
fps = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Start timing for FPS calculation
    start_time = time.time()

    # Convert to grayscale and resize
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    resized = cv.resize(gray, (IMG_SIZE, IMG_SIZE))

    # Preprocess for model: scale and add batch/channel dims
    img_input = resized.astype(np.float32) / 255.0
    img_input = np.expand_dims(img_input, axis=(0, -1))  # Shape: (1, 244, 244, 1)

    # Get predictions
    pred_class_logits, pred_bbox = model.predict(img_input, verbose=0)
    pred_class = np.argmax(pred_class_logits[0])
    pred_label = class_names[pred_class]

    # Scale bounding box coordinates back to original frame size
    frame_height, frame_width = frame.shape[:2]
    pred_box = pred_bbox[0]

    # Convert normalized coordinates (0-1) to pixel coordinates
    x = int(pred_box[0] * frame_width)
    y = int(pred_box[1] * frame_height)
    w = int(pred_box[2] * frame_width)
    h = int(pred_box[3] * frame_height)

    # Draw predicted bounding box and label on original frame
    x2, y2 = x + w, y + h
    color = (0, 255, 0) if pred_label == 'with mask' else (0, 0, 255)  # Green for mask, Red for no mask
    cv.rectangle(frame, (x, y), (x2, y2), color, 2)

    # Add confidence score if available
    confidence = np.max(tf.nn.softmax(pred_class_logits[0]).numpy())
    label_text = f"{pred_label}: {confidence:.2f}"
    cv.putText(frame, label_text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Calculate FPS
    end_time = time.time()
    fps = 1 / (end_time - start_time + 1e-7)
    fps_text = f"FPS: {fps:.1f}"
    cv.putText(frame, fps_text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv.imshow("Face Mask Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()