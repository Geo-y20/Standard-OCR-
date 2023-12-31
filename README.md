<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Standard OCR Project</h1>

  <h2>Introduction</h2>
    <p>This project aims to create a highly accurate and efficient model for character recognition in images. The dataset used in this project can be found <a href="https://www.kaggle.com/datasets/preatcher/standard-ocr-dataset">here</a>. The dataset consists of two sections: Data and Data2, each having training and testing directories with 36 subdirectories representing different character classes. The training data contains 573 images per class, while the testing data includes approximately 88 images per class. Understanding the dataset's structure is crucial for proper organization and analysis.</p>

  <h2>Problem Statement</h2>
    <p>The task is a computer vision challenge to detect characters in input images, emphasizing image processing, analysis, and modern deep learning techniques. It's more aligned with computer vision than Optical Character Recognition (OCR), utilizing various models like ResNet, Xception, Inception, and MobileNet to process and analyze the dataset for accurate predictions.</p>

  <h2>GitHub Repository</h2>
    <p>The code for this project is hosted on GitHub. You can clone the repository using the following command:</p>
    <pre><code>gh repo clone AIBabyTeaching/deep-learning-project-Geo-y20</code></pre>

  <h2>Solution Framework</h2>
    <ul>
        <li><strong>Set Up</strong>: Importing necessary modules, setting hyperparameters, and constants.</li>
        <li><strong>Data Loading</strong>: Loading the dataset into memory for processing.</li>
        <li><strong>Data Processing</strong>: Converting raw data, including techniques like data augmentation, normalization, and resizing images.</li>
        <li><strong>Data Visualization</strong>: Inspecting the dataset for insights and potential issues.</li>
        <li><strong>Backbone Comparison</strong>: Comparing different pre-trained backbones to identify the best performer.</li>
        <li><strong>Model Building</strong>: Constructing a model architecture using selected backbones.</li>
        <li><strong>Model Predictions</strong>: Evaluating model performance on unseen data, analyzing predictions, and identifying areas for improvement.</li>
    </ul>

  <h2>Folder Structure</h2>
    <ul>
        <li><code>app.py</code>: Contains Flask web application code for image prediction.</li>
        <li><code>templates/</code>: Directory for HTML templates.</li>
        <li><code>static/</code>: Directory for static files (CSS, JS, images).</li>
    </ul>

  <h2>Getting Started</h2>
    <ol>
        <li>Install necessary libraries and dependencies.</li>
        <li>Ensure Python environment compatibility.</li>
        <li>Run <code>pip install -r requirements.txt</code> to install dependencies.</li>
        <li>Train and save your model using the provided dataset.</li>
        <li>Update <code>app.py</code> with the path to your trained model.</li>
        <li>Run the Flask application (<code>python app.py</code>) and navigate to <code>localhost:5000</code> in your browser.</li>
    </ol>

  <h2>Usage</h2>
    <ol>
        <li>Access the application through the browser.</li>
        <li>Upload an image containing characters.</li>
        <li>Get predictions for the characters present in the image.</li>
    </ol>

  <h2>Download the Model</h2>
    <p>To download the H5 model file, click <a href="https://drive.google.com/file/d/1RlZ0oqee9UgcBOi5w07dTNKwsJ8nOaD1/view?usp=sharing">here</a>.</p>

  <h2>Sample Images</h2>
    <p>
      <img src="https://drive.google.com/uc?export=view&id=1MzsL6GlmHYlLxPBp8vJ1VMuzp_URVfQF" alt="Sample 1">
      <img src="https://drive.google.com/uc?export=view&id=1APZ0ElDgxUzDTL36ovjwbZmSL3fWxUVt" alt="Sample 2">
    </p>
</body>
</html>
