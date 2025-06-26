from pathlib import Path
import os

# Automatically determine the project root (where config.py is located)
try:
    PROJECT_ROOT = Path(__file__).resolve().parent
except NameError:
    PROJECT_ROOT = Path(os.getcwd()).parent

# Define data paths
DATA_RAW = PROJECT_ROOT / "Data" / "Raw" / "listings.csv"
PROCESSED_DATA = PROJECT_ROOT / "Data" / "Processed"
CLEANED_DATA = PROCESSED_DATA / "listings_cleaned.csv"

# Optionally create the 'Processed' folder if it doesn't exist
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

import importlib
import config
importlib.reload(config)

# Now access the cleaned data path
import pandas as pd
listing_cleaned = pd.read_csv(config.CLEANED_DATA)
listing_cleaned.head()
