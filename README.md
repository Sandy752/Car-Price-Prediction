![GitHub repo size](https://img.shields.io/github/repo-size/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/sumit0072/Car-Price-Prediction-Project?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/sumit0072/Car-Price-Prediction-Project?color=red&style=for-the-badge)


<h1>Car Dekho Price Prediction</h1>


### Model Performance Summary

| Model                      | Training RMSE      | Training MAE       | Training R² | Test RMSE         | Test MAE          | Test R²  |
|----------------------------|---------------------|---------------------|-------------|--------------------|--------------------|----------|
| **Linear Regression**      | 553,855.67          | 268,101.61          | 0.6218      | 502,543.59         | 279,618.58         | 0.6645   |
| **Lasso**                  | 553,855.67          | 268,099.22          | 0.6218      | 502,542.67         | 279,614.75         | 0.6645   |
| **Ridge**                  | 553,856.32          | 268,059.80          | 0.6218      | 502,533.82         | 279,557.22         | 0.6645   |
| **K-Neighbors Regressor**  | 325,886.87          | 91,467.67           | 0.8691      | 253,118.42         | 112,704.35         | 0.9149   |
| **Decision Tree**          | 20,797.24           | 5,164.82            | 0.9995      | 309,775.55         | 125,501.42         | 0.8725   |
| **Random Forest Regressor**| 139,138.17          | 39,895.98           | 0.9761      | 221,936.27         | 100,966.59         | 0.9346   |

### Summary
The K-Neighbors Regressor and Random Forest Regressor performed the best on the test set, achieving high R² scores and lower RMSE compared to other models. In contrast, while the Decision Tree had excellent performance on the training set, it showed a significant drop in performance on the test set, indicating potential overfitting.
