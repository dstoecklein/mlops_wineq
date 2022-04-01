from sklearn.model_selection import train_test_split
from random_forest_regressor.config.core import config
from random_forest_regressor.src.pipeline import pipeline
from random_forest_regressor.src.data_manager import get_train_test_data, save_pipeline

def fit() -> None:
    train_data, _ = get_train_test_data()
    X = train_data.drop("TARGET", axis=1)[config.model_config.features]
    y = train_data["TARGET"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=config.model_config.test_size,
        random_state=config.model_config.seed
    )
    pipeline.fit(X_train, y_train)
    save_pipeline(pipeline=pipeline)

if __name__ == "__main__":
    fit()