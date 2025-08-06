# === QUIZ MASTER ===
# Review and comment my code which will be studied by a beginner python programmer

import random
import time

# Quiz data structure: categories -> difficulty -> list of questions
questions = {
    "Science": {
        "easy": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": 1},
            {"question": "What gas do plants breathe in?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": 2},
            {"question": "Water freezes at what temperature (C)?", "options": ["0", "100", "50", "10"], "answer": 0},
            {"question": "How many legs does a spider have?", "options": ["6", "8", "10", "12"], "answer": 1},
            {"question": "Sun is a...", "options": ["Planet", "Comet", "Star", "Asteroid"], "answer": 2}
        ],
        "hard": [
            {"question": "What is the atomic number of Carbon?", "options": ["4", "6", "8", "12"], "answer": 1},
            {"question": "Speed of light?", "options": ["300,000 km/s", "150,000 km/s", "3,000 km/s", "1,000 km/s"], "answer": 0},
            {"question": "Avogadro's number?", "options": ["6.02e23", "3.14", "1.61", "2.71"], "answer": 0},
            {"question": "What organ produces insulin?", "options": ["Liver", "Pancreas", "Heart", "Lung"], "answer": 1},
            {"question": "Gas used in light bulbs?", "options": ["Oxygen", "Neon", "Helium", "Argon"], "answer": 3}
        ]
    },
    "History": {
        "easy": [
            {"question": "Who was the first president of the USA?", "options": ["Lincoln", "Jefferson", "Washington", "Adams"], "answer": 2},
            {"question": "What year did WWII end?", "options": ["1945", "1939", "1950", "1960"], "answer": 0},
            {"question": "Where is the Great Wall?", "options": ["India", "China", "Korea", "Japan"], "answer": 1},
            {"question": "Pyramids built by?", "options": ["Romans", "Greeks", "Egyptians", "Aztecs"], "answer": 2},
            {"question": "What ship sank in 1912?", "options": ["Olympic", "Carpathia", "Titanic", "Lusitania"], "answer": 2}
        ],
        "hard": [
            {"question": "Napoleon exiled to?", "options": ["Elba", "Malta", "Crete", "Corsica"], "answer": 0},
            {"question": "Berlin Wall fell in?", "options": ["1989", "1991", "1980", "1975"], "answer": 0},
            {"question": "Magna Carta signed?", "options": ["1215", "1315", "1415", "1515"], "answer": 0},
            {"question": "Start of WWI?", "options": ["1914", "1920", "1905", "1939"], "answer": 0},
            {"question": "First printing press?", "options": ["Gutenberg", "Tesla", "Newton", "Da Vinci"], "answer": 0}
        ]
    }
}

# Function to run the quiz
def run_quiz():
    print("=== QUIZ MASTER ===")
    categories = list(questions.keys())
    print("Categories:", ", ".join(categories))
    category = input("Choose a category: ").title()

    if category not in questions:
        print("Invalid category.")
        return

    difficulty = input("Choose difficulty (easy/hard): ").lower()
    if difficulty not in questions[category]:
        print("Invalid difficulty.")
        return

    score = 0
    total = len(questions[category][difficulty])

    for i, q in enumerate(questions[category][difficulty]):
        print(f"\nQuestion {i+1}/{total}: {q['question']}")
        print(f"[{'█' * ((i+1)*10//total)}{'░' * (10 - (i+1)*10//total)}] {(i+1)*100//total}% Complete")

        for idx, opt in enumerate(q["options"]):
            print(f"{chr(65+idx)}) {opt}")
        
        start = time.time()
        ans = input("Your answer (A/B/C/D): ").strip().upper()
        end = time.time()

        if ord(ans) - 65 == q["answer"]:
            print(f"✅ Correct! (+10 points)")
            score += 10
        else:
            correct = chr(65 + q["answer"])
            print(f"❌ Wrong! Correct answer was {correct}")
        
        print(f"Time: {(end - start):.1f} seconds")

    print(f"\nFINAL SCORE: {score}/{total*10} ({score//10}/{total} correct)")

run_quiz()
