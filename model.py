from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def load_model_and_scaler():
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = data.feature_names
    means = X.mean(axis=0)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=10000)
    model.fit(X_scaled, y)

    return model, scaler, feature_names, means

