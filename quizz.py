import random

def quiz_game():
    print("Welcome to the Quiz Game!\n")

    # Player name input
    player_name = input("Please enter your name: ").strip()
    print(f"Hello {player_name}! Let's start the quiz!\n")

    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Madrid", "C. Rome", "D. Berlin"],
            "answer": "A",
            "hint": "It's also known as the City of Light."
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C",
            "hint": "It's greater than 10 but less than 13."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
            "answer": "B",
            "hint": "It's the 4th planet in our solar system."
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
            "answer": "C",
            "hint": "He is often referred to as 'The Bard.'"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. H2"],
            "answer": "B",
            "hint": "It's made up of two hydrogen atoms and one oxygen atom."
        }
    ]

    # Randomize the order of questions
    random.shuffle(questions)

    score = 0  # Player's score
    total_questions = len(questions)  # Total number of questions
    hints_used = 0  # Counter for hints used

    # Iterate through questions
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        
        # Randomize options
        options = q["options"]
        random.shuffle(options)
        
        for option in options:
            print(option)

        # Player input
        while True:
            answer = input("Your answer (A, B, C, or D) or type 'hint' for a clue: ").strip().upper()
            if answer == "HINT":
                print(f"HINT: {q['hint']}")
                hints_used += 1
            elif answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, D, or 'hint'.")

        # Check the answer
        correct_option = next(opt for opt in options if opt.startswith(q['answer']))
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_option}.\n")

    # Calculate the average score (percentage)
    average_score = (score / total_questions) * 100

    # Final score and feedback
    print(f"\nGame Over! {player_name}, your final score is {score}/{total_questions}.")
    print(f"Your average score is: {average_score:.2f}%")

    # Personalized feedback messages
    if average_score == 100:
        print("\nExcellent! You got a perfect score! You're a quiz master!")
    elif average_score >= 80:
        print("\nGreat job! You scored really high. Keep it up!")
    elif average_score >= 50:
        print("\nGood effort! You scored above average. With a little more practice, you'll be even better!")
    elif average_score > 0:
        print("\nDon't worry, you'll get better with practice! Keep trying, and you'll improve your score!")
    else:
        print("\nBetter luck next time. Don't give up! You'll ace it in the future!")

    # Display the number of hints used
    print(f"\nYou used {hints_used} hint(s) during the quiz.")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()
