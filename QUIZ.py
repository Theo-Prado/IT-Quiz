print("==========IT=Quiz==========")

print()
name = input("Enter your name:")
print()
print(f"Welcome, {name}!")
print("This quiz has twenty questions about the world of Information Technology.")
print("Can you get them all right?")
print(f"Play now and find out,{name}!")
print()
points = 0

p1 = input("Who was the first programmer in the world?")
if p1.lower() == "ada lovelace" or p1.lower() == "ada" or p1.lower() == "lovelace":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The first programmer in the world was Ada Lovelace.")

print()

p2 = input("Who invented the Python programming language?")
if p2.lower() == "guido" or p2.lower() == "guido van" or p2.lower() == "guido van rossum":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! Who invented the Python programming language was Guido van Rossum.")

print()

p3 = input("What type of software system does TOTVS develop?")
if p3.lower() == "erp" or p3.lower() == "enterprise resource planning":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! TOTVS develops ERP system (Enterprise Resource Planning).")

print()

p4 = input("Who is considered the father of Artificial Intelligence?")
if p4.lower() == "alan" or p4.lower() == "turing" or p4.lower() == "alan turing":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The father of Artificial Intelligence is Alan Turing.")

print()

p5 = input("What is the name given to the set of instructions, data or logical programs used to operate computers and devices?")
if p5.lower() == "software":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is software.")

print()

p6 = input("What is the physical and tangible part of computers and electronic devices, including internal components (processor, memory, motherboard) and external (mouse, keyboard, monitor)?")
if p6.lower() == "hardware":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is hardware.")

print()

p7 = input("What is the name of an accumulated list of unfinished tasks, requirements, or work items that need to be addressed, often prioritized by importance?")
if p7.lower() == "backlog":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is backlog.")

print()

p8 = input("What is the process of reverting a system, database, or software application to a previous, stable state to undo errors, faulty updates, or undesirable changes?")
if p8.lower() == "rollback":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is rollback.")

print()

p9 = input("What is a distinctive attribute, aspect, or functionality of a product, system, or service that adds value, improves usability, or makes it unique?")
if p9.lower() == "feature":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is feature.")

p10 = input("what is the most recommended language for automation?")
if p10.lower() == "python":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! It is Python.")

p11 = input("What does CPU stand for?")
if p11.lower() == "central processing unit":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! CPU stands for Central Processing Unit.")

print()

p12 = input("Which protocol is used to securely browse websites (encrypted web traffic)?")
if p12.lower() == "https":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The correct answer is HTTPS.")

print()

p13 = input("What does RAM stand for?")
if p13.lower() == "random access memory":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! RAM stands for Random Access Memory.")

print()

p14 = input("Which database language is commonly used for querying relational databases?")
if p14.lower() == "sql" or p14.lower() == "structured query language":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The correct answer is SQL (Structured Query Language).")

print()

p15 = input("What does DNS stand for?")
if p15.lower() == "domain name system":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! DNS stands for Domain Name System.")

print()

p16 = input("Which command is used in Git to create a copy of a remote repository locally?")
if p16.lower() == "git clone":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The command is git clone.")

print()

p17 = input("In cybersecurity, what does MFA stand for?")
if p17.lower() == "multi-factor authentication" or p17.lower() == "multifactor authentication":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! MFA stands for Multi-Factor Authentication.")

print()

p18 = input("What does API stand for?")
if p18.lower() == "application programming interface":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! API stands for Application Programming Interface.")

print()

p19 = input("Which cloud service model provides virtual servers, storage, and networking resources on demand?")
if p19.lower() == "iaas" or p19.lower() == "infrastructure as a service":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! The correct answer is IaaS (Infrastructure as a Service).")

print()

p20 = input("What is the binary value of decimal number 10?")
if p20.lower() == "1010":
  points += 1
  print("Correct! Points:",points,"/ 20")
else:
  print("Wrong! Decimal 10 in binary is 1010.")

if points == 20:
  print("Congratulations, you won! You got all the questions right!")
elif points >= 12:
  print("Good! You got",points,"/ 20 correct!")
elif points >= 10:
  print("Median score. You got",points,"/ 20 correct!")
else:
  print("You lost! You got",points,"/ 20 correct!")
print(f"Thank you for playing, {name}!")
