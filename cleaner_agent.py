# agents/cleaner_agent.py

import pandas as pd
import os
import numpy as np

class CSVCleaner:
    def __init__(self):
        pass

    def clean_csv(self, path):
        df = pd.read_csv(path)
        before_rows = df.shape[0]

        # Step 1: Normalize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Step 2: Convert ₹, %, etc.
        def clean_numeric(val):
            if isinstance(val, str):
                val = val.replace("₹", "").replace(",", "").replace("%", "")
            try:
                return float(val)
            except:
                return val

        df = df.applymap(clean_numeric)

        # Step 3: Parse datetime columns
        for col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                continue

        # Step 4: Fill missing values
        for col in df.select_dtypes(include=['float64', 'int64']):
            df[col].fillna(df[col].mean(), inplace=True)

        for col in df.select_dtypes(include=['object']):
            if df[col].isnull().any():
                df[col].fillna(df[col].mode()[0], inplace=True)

        # Step 5: Drop duplicates
        df = df.drop_duplicates()
        after_rows = df.shape[0]

        # Save cleaned file
        cleaned_path = os.path.join("uploads", "cleaned_" + os.path.basename(path))
        df.to_csv(cleaned_path, index=False)

        return cleaned_path, before_rows, after_rows
