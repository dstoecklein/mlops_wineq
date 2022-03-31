import pandas as pd
from pathlib import Path
from random_forest_regressor.config.core import DATA_PATH, config

def load_data() -> pd.DataFrame:
    df = pd.read_csv(Path(f"{DATA_PATH}/{config.app_config.raw_data}"))
    cols = df.columns
    cols = [col.replace(" ", "_") for col in cols]
    df.columns = cols
    return df