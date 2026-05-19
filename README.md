# Diabetes Prediction Machine Learning

## Overview
A set of notebooks for diabetes outcome prediction using classical ML models and model comparison workflows.

## Problem Statement
Diabetes risk prediction needs transparent baselines that can compare model families on structured patient features.

## Features
- EDA on diabetes dataset
- Model comparison workflow
- Baseline logistic regression implementation

## Tech Stack
- Python
- Pandas
- Scikit-learn
- LightGBM
- Matplotlib
- Seaborn

## Dataset
- diabetes.csv

## Models / Algorithms
- Logistic Regression
- KNN
- SVM
- Decision Tree
- Random Forest
- LightGBM

## Results
The source contains accuracy, classification-report, confusion-matrix, MSE, and R2 evaluation code. Exact final metrics should be read from the notebooks after rerun.

## Project Structure
- notebooks/
  - diabetes-classification-baseline.ipynb
  - diabetes-logistic-regression-demo.ipynb
  - diabetes-prediction-ml-comparison.ipynb

## How to Run
- `pip install -r requirements.txt`
- `jupyter notebook notebooks/diabetes-prediction-ml-comparison.ipynb`

## Screenshots / Demo
Screenshots or demo media can be added after deployment.

## Future Improvements
- Add clean dataset download instructions
- Track experiment results in a table
- Package the best model for inference

## Author
Ramadan Mohamed Hassan
