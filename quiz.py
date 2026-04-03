def test(question_text, correct_answer, answer_type):
  print(question_text)
  print(answer_type)
  guess = input("Your answer: ")

  while not guess.isnumeric() and answer_type == "number_answer":
    guess = input("Please enter a fully numeric answer: Your answer: ")
  while guess.isnumeric() and answer_type == "word_answer":
    guess = input("Please enter a word answer: Your answer: ")

  if guess.lower() == correct_answer.lower():
    print("correct")
    return 1
  else:
    print("wrong")
    return 0
def mc_test(question_text, correct_answer, answer_option):
  print("Multiple Choice: Select One (a,b,c,d):")
  abcd = ["a", "b", "c", "d"]
  print(question_text)
  for option in range(len(answer_option)):
    print(abcd[option], answer_option[option])
  guess = input()
  while guess not in abcd: 
    guess = input()
def start_quiz():
  score = 0
  print("Welcome to my Quiz")
  """score += test("What is 3+4", "7")
  score += test("What is 3+10", "13")
  score += test("What is 8+22", "30")
  score += test("12*12", "144")"""
  
  #score += test("10*10,000", "100000","number_answer")
  #score += test("what is ten times ten", "hundred", "word_answer")
  
  score += mc_test("1+1", "c", ("5","6","2","1"))
  
  
  print(f"Game Over! score: {score}")
  # what is ten times ten, (hundred, 100)
x = "100,000"
print(x.isnumeric())
start_quiz()
#,100
