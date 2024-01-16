# Parking Space Classifier

This project is a simple image classifier designed for learning purposes. It is specifically trained to classify images into two categories: "empty" and "not_empty," indicating whether a parking space is vacant or occupied. The classifier uses a Support Vector Machine (SVM) implemented with the Scikit-learn library.

## Dataset

The dataset used for training and testing the model consists of images of parking spaces. The dataset is structured with two main categories:
1. empty - Images of empty parking spaces.
2. not_empty - Images of parking spaces with vehicles.

## Model Training

The script `parking_space_classifier.py` loads the dataset, preprocesses the images, and trains an SVM classifier using a grid search for hyperparameter tuning. The hyperparameters considered in the grid search are 'gamma' and 'C'. The best-performing model is selected based on cross-validated accuracy.

## Usage

1. Ensure you have the required dependencies installed ( `scikit-image`, `numpy`, `scikit-learn`).
2. Set the `input_dir` variable in the script to the path containing the dataset( Make sure to extract the data set file).
3. Run the script `parking_space_classifier.py`.
4. The trained model will be saved as 'model.p' in the current directory.

## Model Evaluation

The script evaluates the model on a test set and prints the accuracy score, indicating the percentage of correctly classified samples.

## Note

This project is intended for educational purposes to understand the basics of image classification using a Support Vector Machine. It uses a small and simple dataset, and the model may not perform optimally on more complex datasets.

Feel free to experiment with different datasets, hyperparameters, or model architectures to enhance your understanding of machine learning and image classification.

Happy learning!
