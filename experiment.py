import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ======================
# Dados sintéticos
# ======================
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + np.random.randn(100) * 0.1

# ======================
# Modelo
# ======================
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
rmse = mean_squared_error(y, y_pred, squared=False)

# ======================
# MLflow
# ======================
mlflow.set_experiment("teste-jenkins-mlflow")

with mlflow.start_run():
    mlflow.log_param("model", "LinearRegression")
    mlflow.log_metric("rmse", rmse)
    mlflow.sklearn.log_model(model, "model")

print(f"RMSE: {rmse:.4f}")
