

import joblib

from sklearn.ensemble import RandomForestRegressor

def train_model(X,y):

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X,y)

    joblib.dump(
        model,
        "model/sales_forecast_model.pkl"
    )

    return model