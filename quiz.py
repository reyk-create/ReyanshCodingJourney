def test(question_text, correct_answer):
  print(question_text)
  guess = input("Your answer: ")
  if guess.lower() == correct_answer.lower():
    print("correct")
    return 1
  else:
    print("wrong")
    return 0
def start_quiz():
  score = 0
  print("Welcome to my Quiz")
  score += test("What is 3+4", "7")
  score += test("What is 3+10", "13")
  score += test("What is 8+22", "30")
  score += test("12*12", "144")
  score += test("10*10,000", "100,000")
  print(f"Game Over! score: {score}")
start_quiz()
