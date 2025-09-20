import os
import numpy as np
import cv2
from datetime import datetime
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from tensorflow.keras.models import load_model  # type: ignore
from .models import *

base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, 'models', '20_Epoch_85%Training_80%Testing.h5')
model = load_model(model_path)
print("Model loaded successfully.")

# Class mappings
CLASS_MAPPING = {
    0: 'No_Dr (Normal Eye with no Diabetic Retinopathy)',
    1: 'Mild Diabetic Retinopathy',
    2: 'Moderate Diabetic Retinopathy',
    3: 'Severe Diabetic Retinopathy',
    4: 'Proliferative Diabetic Retinopathy'
}

def predict(img_path):
    try:
        # Read and preprocess the image
        img = cv2.imread(img_path)
        img = cv2.resize(img, (224, 224))  # Resize to match the input size
        img = img / 255.0  # Normalize to match the training pipeline
        img = np.expand_dims(img, axis=0)  # Add batch dimension

        # Predict using the loaded model
        predictions = model.predict(img)
        predicted_class = np.argmax(predictions)
        
        # Get the result from class mapping
        return CLASS_MAPPING[predicted_class]
    except Exception as e:
        print(f"Error in prediction: {e}")
        return "Error in prediction"

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        left = request.FILES.get('left')
        right = request.FILES.get('right')

        try:
            # Save the uploaded files temporarily
            fs = FileSystemStorage()
            left_path = fs.save(left.name, left)
            right_path = fs.save(right.name, right)
            left_full_path = fs.path(left_path)
            right_full_path = fs.path(right_path)

            # Predict using the model
            res1 = predict(left_full_path)
            res2 = predict(right_full_path)

            # Save contact information (if applicable in your models)
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                img1=left.name,
                img2=right.name,
                res1=res1,
                res2=res2,
                date=datetime.today()
            )
            contact.save()

            # Prepare the data for the template
            data = {
                'name': name,
                'email': email,
                'phone': phone,
                'desc': desc,
                'img1': fs.url(left_path),
                'img2': fs.url(right_path),
                'res1': res1,
                'res2': res2,
            }
            return render(request, 'result.html', data)
        except Exception as e:
            print(f"Error in handling the request: {e}")
            return HttpResponse(f"Error in handling the request: {e}")

    return render(request, 'contact.html')
