# data-science-education-salaries

# Project Overview
This project analyzes post-college salary data, exploring trends in early and mid-career pay across different majors. It includes data preprocessing, statistical analysis, visualizations, and predictive modeling to provide insights into career earnings growth.

# Folder Structure
```
project-root/
├── data/                # Contains raw and cleaned datasets
├── scripts/             # Python scripts for processing, analyzing, and modeling the data
├── outputs/             # Results from analysis, including plots and model performance
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

# Usage
## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```
pip install -r requirements.txt
```

## 2. Preprocess the Data:
Run the preprocessing script to clean and format the dataset.
```
python scripts/01_preprocess.py
```

## 3. Generate Summary Statistics:
Run the script to obtain key insights and summary statistics.
```
python scripts/02_summary_statistics.py
```

## 4. Create Visualizations:
Generate histograms and scatter plots to explore salary trends.
```
python scripts/03_visualizations.py
```

## 5. Train and Evaluate the Model:
Train a linear regression model to predict mid-career pay and evaluate its performance.
```
python scripts/04_modeling.py
```

# Requirements
- Python 3.x
- pandas
- matplotlib
- scikit-learn

Install dependencies using:
```
pip install -r requirements.txt
```

# Acknowledgments
Dataset Name: U.S Post College Salaries  
Dataset Author: Dharmendra Rathod  
Dataset Source: [Kaggle](https://www.kaggle.com/datasets/rathoddharmendra/post-college-salaries)