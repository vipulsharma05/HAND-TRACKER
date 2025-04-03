from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
from .Handtracking import handDetector  # Import your module

cap = cv2.VideoCapture(0)  # Access webcam
detector = handDetector()  # Initialize the detector

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        frame = detector.findHands(frame)  # Process frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def index(request):
    return render(request, 'tracking/index.html')
