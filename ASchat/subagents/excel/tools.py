import pandas as pd
import os

def list_files():
    """List files in the current directory."""
    import os
    return os.listdir('../../../resources/*.xlsx')

def load_excel(file_path):
    """Load an Excel file and return its content as a DataFrame."""
    df = pd.read_excel(file_path)
    return df

def list_sheets(file_path):
    """List all sheet names in the given Excel file."""
    xlsx = pd.ExcelFile(file_path)
    return xlsx.sheet_names