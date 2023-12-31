# Standard OCR Project 

## Introduction

This project aims to create a highly accurate and efficient model for character recognition in images. The dataset used in this project can be found [here](https://www.kaggle.com/datasets/preatcher/standard-ocr-dataset). The dataset consists of two sections: Data and Data2, each having training and testing directories with 36 subdirectories representing different character classes. The training data contains 573 images per class, while the testing data includes approximately 88 images per class. Understanding the dataset's structure is crucial for proper organization and analysis.

## Problem Statement

The task is a computer vision challenge to detect characters in input images, emphasizing image processing, analysis, and modern deep learning techniques. It's more aligned with computer vision than Optical Character Recognition (OCR), utilizing various models like ResNet, Xception, Inception, and MobileNet to process and analyze the dataset for accurate predictions.

## GitHub Repository

The code for this project is hosted on GitHub. You can clone the repository using the following command:

```bash
gh repo clone AIBabyTeaching/deep-learning-project-Geo-y20
```

## Solution Framework

- **Set Up**: Importing necessary modules, setting hyperparameters, and constants.
- **Data Loading**: Loading the dataset into memory for processing.
- **Data Processing**: Converting raw data, including techniques like data augmentation, normalization, and resizing images.
- **Data Visualization**: Inspecting the dataset for insights and potential issues.
- **Backbone Comparison**: Comparing different pre-trained backbones to identify the best performer.
- **Model Building**: Constructing a model architecture using selected backbones.
- **Model Predictions**: Evaluating model performance on unseen data, analyzing predictions, and identifying areas for improvement.

## Folder Structure

- `app.py`: Contains Flask web application code for image prediction.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static files (CSS, JS, images).

## Getting Started

1. Install necessary libraries and dependencies.
2. Ensure Python environment compatibility.
3. Run `pip install -r requirements.txt` to install dependencies.
4. Train and save your model using the provided dataset.
5. Update `app.py` with the path to your trained model.
6. Run the Flask application (`python app.py`) and navigate to `localhost:5000` in your browser.

## Usage

1. Access the application through the browser.
2. Upload an image containing characters.
3. Get predictions for the characters present in the image.

## Download the Model

To download the H5 model file, click [here](https://drive.google.com/file/d/1RlZ0oqee9UgcBOi5w07dTNKwsJ8nOaD1/view?usp=sharing).



