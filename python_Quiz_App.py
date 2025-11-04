# python_quiz_app.py

def run_quiz(questions):
    score = 0
    for question, info in questions.items():
        print("\n" + question)
        for option in info["options"]:
            print(option)
        answer = input("Your answer: ").strip().lower()

        if answer == info["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is: {info['answer']}")
    print(f"\n🎯 You got {score}/{len(questions)} correct!")


def main():
    print("=== 🐍 Welcome to the Python Quiz App ===")

    questions = {
        # Easy Level
        "1. What is the correct file extension for Python files?": {
            "options": ["a) .pyth", "b) .pt", "c) .py", "d) .pyt"],
            "answer": "c"
        },
        "2. Which keyword is used to define a function in Python?": {
            "options": ["a) define", "b) def", "c) func", "d) function"],
            "answer": "b"
        },
        "3. How do you insert comments in Python code?": {
            "options": ["a) // comment", "b) /* comment */", "c) # comment", "d) <!-- comment -->"],
            "answer": "c"
        },
        "4. What is the output of print(2 ** 3)?": {
            "options": ["a) 6", "b) 8", "c) 9", "d) 5"],
            "answer": "b"
        },
        "5. Which data type is immutable in Python?": {
            "options": ["a) List", "b) Dictionary", "c) Set", "d) Tuple"],
            "answer": "d"
        },

        # Intermediate Level
        "6. What is the output of print(type([]))?": {
            "options": ["a) <class 'list'>", "b) <class 'tuple'>", "c) <class 'dict'>", "d) <class 'set'>"],
            "answer": "a"
        },
        "7. What will bool([]) return?": {
            "options": ["a) True", "b) False"],
            "answer": "b"
        },
        "8. Which of these is not a Python keyword?": {
            "options": ["a) pass", "b) eval", "c) assert", "d) repeat"],
            "answer": "d"
        },
        "9. What is the output of this code?\n\na = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)": {
            "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [4, 1, 2, 3]", "d) Error"],
            "answer": "b"
        },
        "10. Which built-in function returns the length of an object?": {
            "options": ["a) count()", "b) length()", "c) len()", "d) size()"],
            "answer": "c"
        },
    }

    run_quiz(questions)
    print("\nThanks for playing the Python Quiz! 🐍")


if __name__ == "__main__":
    main()
