import cv2
import mediapipe as mp
import numpy as np
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

@csrf_exempt
def process_frame(request):
    if request.method == "POST":
        try:
            data = request.json()
            image_data = data["image"].split(",")[1]  # Extract base64 data
            image_bytes = base64.b64decode(image_data)

            # Convert to OpenCV format
            np_arr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Process with Mediapipe
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(img_rgb)

            # Detect hand presence
            hand_detected = bool(results.multi_hand_landmarks)

            return JsonResponse({"hand_detected": hand_detected})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return JsonResponse({"message": "Send a POST request."})
