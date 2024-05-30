import random

# Questions and Answers
questions = [
    "What is the capital city of Australia?",
    "Who painted the Mona Lisa?",
    "In which year did the Titanic sink?",
    "What is the largest organ in the human body?",
    "What is the chemical symbol for gold?",
    "Who wrote the novel 'To Kill a Mockingbird'?",
    "Which planet is known as the 'Red Planet'?",
    "What is the tallest mountain in the world?",
    "Who is the Greek god of the sea?",
    "What is the chemical formula for water?",
    "Which famous scientist developed the theory of relativity?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the capital city of Japan?",
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
    "What is the capital city of South Africa?",
    "What is the chemical formula for glucose?"
]

answers = [
    "Canberra",
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
    "Tokyo",
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
    "Pretoria (Executive), Bloemfontein (Judicial), Cape Town (Legislative)",
    "C6H12O6"
]

# Shuffle the questions and answers
combined = list(zip(questions, answers))
random.shuffle(combined)
questions, answers = zip(*combined)

# Generate the quiz
print("Welcome to the General Knowledge Quiz!\n")

