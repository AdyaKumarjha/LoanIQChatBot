from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent

load_dotenv()

DATASET_PATH = BASE_DIR / "dataset" / "loans.xlsx"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")