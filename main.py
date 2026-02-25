import tkinter as tk
from tkinter import Tk, messagebox
from PIL import Image, ImageTk
import csv
import os

WHITE = "#FFFFFF"
GRAY = "#666666"

# QUESTION
class Question:
    def __init__(self, text, options, correct):
        self.text = text
        self.options = options
        self.correct = correct.strip()

    def is_correct(self, answer):
        return answer.strip() == self.correct


# QUIZ CLASS 
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current = 0
        self.score = 0

    def get_question(self):
        return self.questions[self.current]

    def submit_answer(self, answer):
        if self.get_question().is_correct(answer):
            self.score += 1
        self.current += 1

    def finished(self):
        return self.current >= len(self.questions)


# LOAD QUESTIONS 
def load_questions(filename):
    questions = []

    if not os.path.exists(filename):
        messagebox.showerror("Error", f"{filename} not found.")
        return []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 6:
                questions.append(
                    Question(row[0], row[1:5], row[5])
                )

    return questions


def save_result(name, score, total):
    percentage = round((score / total) * 100, 2)

    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, score, total, percentage])


# SCREEN CONTROL 
def show_frame(frame):
    frame.tkraise()


# QUIZ FLOW 
def start_quiz(filename):
    global quiz
    questions = load_questions(filename)

    if not questions:
        return

    quiz = Quiz(questions)
    display_question()
    show_frame(quiz_frame)


def display_question():
    question = quiz.get_question()
    question_label.config(text=question.text)

    for i in range(4):
        option_buttons[i].config(
            text=question.options[i],
            value=question.options[i]
        )

    selected.set(None)


def submit_answer():
    answer = selected.get()

    if not answer:
        messagebox.showwarning("Warning", "Please select an answer.")
        return

    quiz.submit_answer(answer)

    if quiz.finished():
        show_result()
    else:
        display_question()


def show_result():
    name = name_entry.get()
    total = len(quiz.questions)

    save_result(name, quiz.score, total)

    percentage = round((quiz.score / total) * 100, 2)

    result_label.config(
        text=f"Final Score: {quiz.score}/{total}\nPercentage: {percentage}%"
    )

    show_frame(result_frame)


def go_to_topic():
    if name_entry.get().strip() == "":
        messagebox.showwarning("Warning", "Please enter your name first.")
        return

    show_frame(topic_frame)


# MAIN WINDOW 
root = tk.Tk()
root.title("Cyber Defence Quiz")
root.geometry("700x500")
root.resizable(False, False)

# Load Background Image
bg_image = Image.open("bmw_background.jpg")
bg_image = bg_image.resize((700, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create Frames
name_frame = tk.Frame(root)
topic_frame = tk.Frame(root)
quiz_frame = tk.Frame(root)
result_frame = tk.Frame(root)

for frame in (name_frame, topic_frame, quiz_frame, result_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Add background to EACH frame (This is the correct way)
    bg_label = tk.Label(frame, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# NAME SCREEN 
tk.Label(
    name_frame,
    text="Enter Your Name",
    fg=WHITE,
    bg=GRAY,
    font=("Arial", 16, "bold")
).pack(pady=40)

name_entry = tk.Entry(name_frame, width=30)
name_entry.pack(pady=10)

tk.Button(
    name_frame,
    text="Submit",
    command=go_to_topic,
    width=20
).pack(pady=20)


# TOPIC SCREEN 
tk.Label(
    topic_frame,
    text="Choose a Topic",
    fg=WHITE,
    bg=GRAY,
    font=("Arial", 16, "bold")
).pack(pady=40)

tk.Button(
    topic_frame,
    text="Topic 1: Phishing & Email Security",
    command=lambda: start_quiz("Phishing.csv"),
    width=35
).pack(pady=10)

tk.Button(
    topic_frame,
    text="Topic 2: Passwords & Data Protection",
    command=lambda: start_quiz("Password.csv"),
    width=35
).pack(pady=10)


# QUIZ SCREEN
question_label = tk.Label(
    quiz_frame,
    text="",
    wraplength=600,
    fg=WHITE,
    bg=GRAY,
    font=("Helvetica", 12)
)
question_label.pack(pady=40)

selected = tk.StringVar()
option_buttons = []

for i in range(4):
    btn = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=selected,
        value="",
        fg=WHITE,
        bg=GRAY,
        font=("Helvetica", 11),
        selectcolor="grey"
    )
    btn.pack(anchor="w", padx=120, pady=5)
    option_buttons.append(btn)

tk.Button(
    quiz_frame,
    text="Submit",
    command=submit_answer,
    width=20
).pack(pady=30)


# RESULT SCREEN 
result_label = tk.Label(
    result_frame,
    text="",
    fg=WHITE,
    bg=GRAY,
    font=("Helvetica", 16)
)
result_label.pack(pady=100)

tk.Button(
    result_frame,
    text="Exit",
    command=root.destroy,
    width=20
).pack(pady=20)

# START
if __name__ == "__main__":
    root = Tk()
    show_frame(name_frame)
    root.mainloop()