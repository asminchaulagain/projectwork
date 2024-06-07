import random
import tkinter as tk
from tkinter import messagebox
import threading

questions = [
    "What is the capital city of india?",
    "Who painted the Mona Lisa?",
    "In which year did the Titanic sink?",
    "What is the largest organ in the human body?",
    "What is the chemical symbol for the gold?",
    "Who wrote the novel 'To Kill a Mockingbird'?",
    "Which planet is known as the 'Red Planet'?",
    "What is the tallest mountain in the world?",
    "Who is the Greek god of the sea?",
    "What is the chemical formula for water?",
    "Which famous scientist developed the theory of relativity?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the capital city of china?",
    "Which element has the atomic number 6?",
    "Who is the current president of the United States (as of 2024)?",
    "Which continent is the largest by land area?",
    "What is the currency of France?",
    "Who painted 'Starry Night'?",
    "What is the largest mammal in the world?",
    "What is the chemical symbol for sodium?",
    "In which year did World War II end?",
    "Who is the author of the Harry Potter series?",
    "What is the tallest animal in the world?",
    "Which country is known as the Land of the Rising Sun?",
    "What is the capital city of Brazil?",
    "Who discovered penicillin?",
    "What is the chemical formula for methane?",
    "Which planet is closest to the Sun?",
    "Who wrote '1984'?",
    "What is the largest ocean on Earth?",
    "Which famous composer wrote the 'Moonlight Sonata'?",
    "Who painted the ceiling of the Sistine Chapel?",
    "What is the chemical symbol for iron?",
    "Which country is famous for its tulips?",
    "Who was the first woman to win a Nobel Prize?",
    "What is the speed of light in a vacuum (approximately)?",
    "Who is known as the 'Father of Geometry'?",
    "Which ocean is the largest by surface area?",
    "What is the capital city of india?",
    "What is the chemical formula for glucose?"
]

answers = [
    "delhi",
    "Leonardo da Vinci",
    "1912",
    "Skin",
    "Au",
    "Harper Lee",
    "Mars",
    "Mount Everest",
    "Poseidon",
    "H2O",
    "Albert Einstein",
    "William Shakespeare",
    "bejing",
    "Carbon",
    "Varies (based on current president)",
    "Asia",
    "Euro",
    "Vincent van Gogh",
    "Blue whale",
    "Na",
    "1945",
    "J.K. Rowling",
    "Giraffe",
    "Japan",
    "Brasília",
    "Alexander Fleming",
    "CH4",
    "Mercury",
    "George Orwell",
    "Pacific Ocean",
    "Ludwig van Beethoven",
    "Michelangelo",
    "Fe",
    "Netherlands",
    "Marie Curie",
    "299,792,458 meters per second",
    "Euclid",
    "Pacific Ocean",
    "delhi",
    "C6H12O6"
]

combined = list(zip(questions, answers))
random.shuffle(combined)
questions, answers = zip(*combined)

def display_question(index):
    question_label.config(text=f"Question {index + 1}: {questions[index]}")
    answer_entry.delete(0, tk.END)
    root.after(10000, next_question)
  
def check_answer():
    global timer_thread
    timer_thread.cancel()
    user_answer = answer_entry.get()
    if user_answer.lower() == answers[current_index].lower():
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror("Result", f"Wrong! The correct answer is {answers[current_index]}")
    if current_index < len(questions) - 1:
        next_question()
    else:
        messagebox.showinfo("Quiz Completed", "Quiz completed! Thanks for participating!")

def next_question():
    global current_index
    current_index += 1
    if current_index < len(questions):
        display_question(current_index)
    else:
        messagebox.showinfo("Quiz Completed", "Quiz completed! Thanks for participating!")

def exit_quiz():
    if self.timer_thread:
        self.timer_thread.cancel()
    self.root.destroy()


root = tk.Tk()
root.title("General Knowledge Quiz")
root.protocol("WM_DELETE_WINDOW",exit_quiz)

question_label = tk.Label(root, text="")
answer_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=check_answer, bg="green")
next_button = tk.Button(root, text="Next", command=next_question)
exit_button = tk.Button(root, text="Exit", command=exit_quiz, bg="red")

question_label.pack(pady=10)
answer_entry.pack(pady=5)
submit_button.pack(pady=5)
next_button.pack(pady=5)
exit_button.pack(pady=5)

current_index = 0
display_question(current_index)

root.mainloop()
