import csv
import html
import random
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# CSV_FILE = Path(__file__).resolve().parent / "./questions.csv"
CSV_FILE = BASE_DIR / "./questions.csv"
RESULT_DIR = BASE_DIR / "results"

def ensure_results_dir():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

def load_questions(csv_file):
    questions =[]

    if not csv_file_exists():
        print(f"Hata CSV dosyası bulunamadı -> {csv_file}")
        return questions

    with open(csv_file, "r", encoding="utf-8-sig", newline="") as file:
        reader= csv.DictReader(file)

        required_columns= {
            "question",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
            "answer",
        }

        if not reader.fieldnames:
            print("Hata: CSV başlıklarını bulamadı")
            return questions

        missing= required_columns - set(reader.fieldnames)
        if missing:
            print("Hata CSV içinde eksik kolonlar var:", ", ".join(sorted(missing)))
            return questions


