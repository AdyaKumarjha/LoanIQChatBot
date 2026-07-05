from fastapi import APIRouter
fromutils.data_loader import loan_loader
import pandas as pd
import numpy as np

router = APIRouter()


@router.get("/dataset/info")
def dataset_info():
    df = loan_loader.load_data()

    return {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": list(df.columns)
    }


@router.get("/dataset/head")
def dataset_head():
    df = loan_loader.load_data().head().copy()

    # Replace NaN, NaT with None
    df = df.replace({np.nan: None})
    df = df.where(pd.notnull(df), None)

    # Convert datetime columns to strings
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].astype(str)

    return df.to_dict(orient="records")