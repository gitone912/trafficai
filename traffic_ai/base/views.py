from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Intersection, TrafficData

def intersection_traffic(request, intersection_id):
    intersection = Intersection.objects.get(pk=intersection_id)
    traffic_data = TrafficData.objects.filter(intersection=intersection).order_by('-timestamp')[:10]
    context = {
        'intersection': intersection,
        'traffic_data': traffic_data,
    }
    return render(request, 'intersection_traffic.html', context)

def home(request):
    return render(request, 'homepage.html')

import cv2
import numpy as np
from django.shortcuts import render

def detect_vehicles(image):
    # Load the pre-trained vehicle detection model
    model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the image
    vehicles = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return len(vehicles)

def release_side(request):
    if request.method == 'POST':
        # Get the uploaded images from the request
        images = []
        for i in range(1, 5):
            image_file = request.FILES.get(f'image{i}')
            if image_file:
                image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
                images.append(image)

        # Perform vehicle detection for each image
        vehicle_counts = []
        for image in images:
            vehicle_count = detect_vehicles(image)
            vehicle_counts.append(vehicle_count)

        # Determine which side of the road should have a green light based on vehicle density
        max_vehicle_count = max(vehicle_counts)
        green_light_index = vehicle_counts.index(max_vehicle_count)

        # Create a list to hold the light colors for each side
        light_colors = ['red', 'red', 'red', 'red']
        light_colors[green_light_index] = 'green'

        return render(request, 'release_side.html', {'light_colors': light_colors})

    return render(request, 'release_side.html')
