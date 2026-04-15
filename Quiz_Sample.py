import csv
import html
import random
from datetime import datetime
from pathlib import Path
from turtledemo.penrose import start

BASE_DIR = Path(__file__).resolve().parent
# CSV_FILE = Path(__file__).resolve().parent / "./questions.csv"
CSV_FILE = BASE_DIR / "./questions.csv"
RESULT_DIR = BASE_DIR / "results"

#
def ensure_results_dir():
    RESULT_DIR.mkdir(parents=True, exist_ok=True)

#
def load_questions(csv_file):
    questions =[]

    if not csv_file.exists():
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

        for now_number, row in enumerate(reader, start=2):
            answer = str(row["answer"]).strip().upper()

            if answer not in {"A","B","C","D"}:
                print(f"Uyarı: {row_number}. satırındaki cevap geçersiz olduğu içi soru atlandı ")
                continue

            question_text =str(row["question"]).strip()
            options ={
                "A" : str(row["option_a"]).strip(),
                "B" : str(row["option_b"]).strip(),
                "C" : str(row["option_c"]).strip(),
                "D" : str(row["option_d"]).strip(),
            }

            if not question_text:
                print(f"Uyarı: {row_number}. satırındaki soru boş olduğu için atlandı")
                continue
            questions.append(
                {
                    "question": question_text,
                    "options": options,
                    "answer": answer,
                }
            )

        return questions


