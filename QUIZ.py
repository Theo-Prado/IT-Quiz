print("==========IT=Quiz==========")

print()
name = input("Enter your name:")
print()
print(f"Welcome, {name}!")
print("This quiz has ten questions about the world of Information Technology.")
print("Can you get them all right?")
print(f"Play now and find out,{name}!")
print()
points = 0

p1 = input("Who was the first programmer in the world?")
if p1.lower() == "ada lovelace" or p1.lower() == "ada" or p1.lower() == "lovelace":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! The first programmer in the world was Ada Lovelace.")

print()

p2 = input("Who invented the Python programming language?")
if p2.lower() == "guido" or p2.lower() == "guido van" or p2.lower() == "guido van rossum":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! Who invented the Python programming language was Guido van Rossum.")

print()

p3 = input("What type of software system does TOTVS develop?")
if p3.lower() == "erp" or p3.lower() == "enterprise resource planning":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! TOTVS develops ERP system (Enterprise Resource Planning).")

print()

p4 = input("Who is considered the father of Artificial Intelligence?")
if p4.lower() == "alan" or p4.lower() == "turing" or p4.lower() == "alan turing":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! The father of Artificial Intelligence is Alan Turing.")

print()

p5 = input("What is the name given to the set of instructions, data or logical programs used to operate computers and devices?")
if p5.lower() == "software":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! It is software.")

print()

p6 = input("What is the physical and tangible part of computers and electronic devices, including internal components (processor, memory, motherboard) and external (mouse, keyboard, monitor)?")
if p6.lower() == "hardware":
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! It is hardware.")

print()

p7 = input("What is the name of an accumulated list of unfinished tasks, requirements, or work items that need to be addressed, often prioritized by importance?")
if p7.lower() == "backlog"
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! It is backlog.")

print()

p7 = input("What is the process of reverting a system, database, or software application to a previous, stable state to undo errors, faulty updates, or undesirable changes?")
if p7.lower() == "rollback"
  points += 1
  print("Correct! Points:",points,"/ 10")
else:
  print("Wrong! It is rollback.")

if points == 10:
  print("Congratulations, you won! You got all the questions right!")
elif points >= 6:
  print("Good! You got",points,"/ 10 correct!")
elif points == 5:
  print("Median score. You got",points,"/ 10 correct!")
else:
  print("You lost! You got",points,"/ 10 correct!")
print(f"Thank you for playing, {name}!
