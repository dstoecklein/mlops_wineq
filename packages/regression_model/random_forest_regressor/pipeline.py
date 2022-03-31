from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from random_forest_regressor.config.core import config

pipeline = Pipeline(
    [ 
        ("MinMaxScaler", MinMaxScaler()), # sklearn will do fit & transform
        ("RandomForestRegressor", RandomForestRegressor(
            n_estimators=config.model_config.n_estimators,
            random_state=config.model_config.seed))
    ]
)