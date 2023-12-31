from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__)

# Function to load your model
def load_your_model():
    model = tf.keras.models.load_model('StandardOCR-ResNet50V2-2.h5')
    return model

# Function to preprocess the uploaded image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (120, 120))
    img = img.astype('float32')
    img /= 255.0
    img = np.expand_dims(img, axis=0)
    return img

# Function to perform prediction
def perform_prediction(filepath):
    loaded_model = load_your_model()  # Load the model
    processed_img = preprocess_image(filepath)  # Preprocess the image
    predictions = loaded_model.predict(processed_img)  # Get predictions
    predicted_class_index = np.argmax(predictions, axis=1)[0]  # Get the predicted class index
    return predicted_class_index  # Return the predicted class index

# Define the directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def upload_file():
    # Check if a file was posted
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if not file:
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Perform prediction on the uploaded image
            predicted_class_index = perform_prediction(filepath)
            
            # Define the class names corresponding to the indices
            class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            
            # Convert the predicted class index to class name
            predicted_class_name = class_names[predicted_class_index]

            # Return the predicted class name
            return jsonify({'prediction': predicted_class_name})

        except Exception as e:
            # If there's an error during prediction, return the error message
            return jsonify({'error': str(e)})

    return jsonify({'error': 'File not allowed or unsupported format'})

@app.route('/<path:filename>')
def serve_js(filename):
    return send_from_directory('static', filename)
    
if __name__ == '__main__':
    app.run(debug=True)