from sklearn.model_selection import train_test_split
from random_forest_regressor.config.core import config
from random_forest_regressor.src.pipeline import pipeline
from random_forest_regressor.src.data_manager import load_data

def fit() -> None:
    data = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        random_state=config.model_config.seed
    )
    pipeline.fit(X_train, y_train)

if __name__ == "__main__":
    fit()