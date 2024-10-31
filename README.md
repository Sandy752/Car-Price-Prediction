![GitHub repo size](https://img.shields.io/github/repo-size/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/sumit0072/Car-Price-Prediction-Project?color=red&style=for-the-badge)


# Car Dekho Price Prediction

## Table of contents
* [Dataset Preview](#dataset-preview)
* [Demo](#demo)   
* [Tools Used](#3)
* [Libraries](#4)
* [Algorithms Used](#5)
* [Model Performance Summary](#model-performance-summary)
* [Hyperparameter tuning](#hyperparameter-tuning)
* [Best Parameters](#best-parameters)
* [Installation](#installation)


## Dataset Preview

A preview of top five rows of the Car Dekho dataset.

| car_name          | brand   | model  | vehicle_age | km_driven | seller_type | fuel_type | transmission_type | mileage | engine | max_power | seats | selling_price |
|--------------------|---------|--------|-------------|-----------|-------------|-----------|-------------------|---------|--------|-----------|-------|----------------|
| Maruti Alto        | Maruti  | Alto   | 9           | 120000    | Individual   | Petrol    | Manual            | 19.70   | 796    | 46.30     | 5     | 120000         |
| Hyundai Grand      | Hyundai | Grand  | 5           | 20000     | Individual   | Petrol    | Manual            | 18.90   | 1197   | 82.00     | 5     | 550000         |
| Hyundai i20        | Hyundai | i20    | 11          | 60000     | Individual   | Petrol    | Manual            | 17.00   | 1197   | 80.00     | 5     | 215000         |
| Maruti Alto        | Maruti  | Alto   | 9           | 37000     | Individual   | Petrol    | Manual            | 20.92   | 998    | 67.10     | 5     | 226000         |
| Ford Ecosport      | Ford    | Ecosport | 6         | 30000     | Dealer       | Diesel    | Manual            | 22.77   | 1498   | 98.59     | 5     | 570000         |

## Demo

progress!!!!

<h3>Tools Used </h3><a id="3"></a>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

<h3>Libraries</h3><a id="4"></a>

![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-FF7F0E?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-30B5E3?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)


<h3>Algorithms Used<h3><a id="5"></a>

1. Decision Tree
2. Random Forest (yielding highest accuracy)
3. Linear Regression
4. Lasso
5. K-Neighbors Regressor

## Model Performance Summary

| Model                      | Training RMSE      | Training MAE       | Training R² | Test RMSE         | Test MAE          | Test R²  |
|----------------------------|---------------------|---------------------|-------------|--------------------|--------------------|----------|
| **Linear Regression**      | 553,855.67          | 268,101.61          | 0.6218      | 502,543.59         | 279,618.58         | 0.6645   |
| **Lasso**                  | 553,855.67          | 268,099.22          | 0.6218      | 502,542.67         | 279,614.75         | 0.6645   |
| **Ridge**                  | 553,856.32          | 268,059.80          | 0.6218      | 502,533.82         | 279,557.22         | 0.6645   |
| **K-Neighbors Regressor**  | 325,886.87          | 91,467.67           | 0.8691      | 253,118.42         | 112,704.35         | 0.9149   |
| **Decision Tree**          | 20,797.24           | 5,164.82            | 0.9995      | 309,775.55         | 125,501.42         | 0.8725   |
| **Random Forest Regressor**| 139,138.17          | 39,895.98           | 0.9761      | 221,936.27         | 100,966.59         | 0.9346   |


The K-Neighbors Regressor and Random Forest Regressor performed the best on the test set, achieving high R² scores and lower RMSE compared to other models. Therefore, we will perform hyperparameter tuning on the K-Neighbors Regressor and Random Forest Regressor. In contrast, while the Decision Tree had excellent performance on the training set, it showed a significant drop in performance on the test set, indicating potential overfitting.

## Hyperparameter tuning
``` Python
knn_params = {"n_neighbors": [2, 3, 10, 20, 40, 50]}
rf_params = {"max_depth": [5, 8, 15, None, 10],
             "max_features": [5, 7, "auto", 8],
             "min_samples_split": [2, 8, 15, 20],
             "n_estimators": [100, 200, 500, 1000]}
```
## Best Parameters  
``` python
models = {
    "Random Forest Regressor": RandomForestRegressor(n_estimators=100, min_samples_split=2, max_features='auto', max_depth=None, 
                                                     n_jobs=-1),
     "K-Neighbors Regressor": KNeighborsRegressor(n_neighbors=10, n_jobs=-1)
    }
```

## Installation

* Clone this repository and unzip it.

* create new  venv with python 3 and activate it .

* Install the required packages using
 ``` bash
pip install -r requirements.txt
```

* Execute the command:
``` bash
  python3 app.py
```

* Open ```http://127.0.0.1:5000/``` in your browser.
