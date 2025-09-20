# AI Retina Disease Detection Web App  

This project is a **Django-based web application** for detecting eye diseases (e.g., Diabetic Retinopathy) from **retina images**.  
The system uses a **deep learning model (EfficientNetB0)** trained with data augmentation to classify retina scans into disease categories.  

Users can **sign up / log in** and then **upload retina images** through the web interface. The app processes the image with the trained model and returns predictions in real-time.  

---

## 🚀 Features  
- 🧠 Deep Learning model using **TensorFlow & EfficientNetB0**  
- 🔄 Data augmentation for robust training  
- 🌐 Web interface built with **Django**  
- 👤 User authentication (login/register)  
- 📂 Upload retina images for detection  
- 📊 Results displayed with prediction accuracy  

---

## 📂 Project Structure  

```bash
eye-disease-detection/
├── Project/             # Django project files
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── home/                # App: main web logic (views, urls, models)
│   ├── models           # Contains files for training the model, the training script, and images of training statistics
├── media/               # Uploaded retina images
├── static/              # CSS, JS, assets
├── templates/           # HTML templates
├── db.sqlite3           # Default database
├── manage.py            # Django project manager
````

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/MuhammadHasnainKayani/ai-retina-diagnosis-web
   cd ai-retina-diagnosis-web
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run server**

   ```bash
   python manage.py runserver
   ```

6. Open in browser:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🧠 Model Training

The **EfficientNetB0 model** was trained with transfer learning and fine-tuning:

* **Input size:** 224×224
* **Augmentations:** rotation, zoom, shift, flip
* **Optimizer:** Adam (lr=0.0001)
* **Loss:** categorical crossentropy
* **Epochs:** 15
* **Dataset:** Balanced diabetic retinopathy dataset

Example training code is included in the repo for reproducibility.

---

## 📦 Requirements

* Python 3.8+
* Django
* TensorFlow / Keras
* scikit-learn
* numpy
* Pillow

Install everything with:

```bash
pip install -r requirements.txt
```

---

