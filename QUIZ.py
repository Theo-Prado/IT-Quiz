print("==========IT=Quiz==========")

print()
name = input("Enter your name:")
print()
print(f"Welcome, {name}!")
print("This quiz has forty questions about the world of Information Technology.")
print("Can you get them all right?")
print(f"Play now and find out,{name}!")
print()
points = 0

p1 = input("Who was the first programmer in the world?")
if p1.lower() == "ada lovelace" or p1.lower() == "ada" or p1.lower() == "lovelace":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The first programmer in the world was Ada Lovelace.")

print()

p2 = input("Who invented the Python programming language?")
if p2.lower() == "guido" or p2.lower() == "guido van" or p2.lower() == "guido van rossum":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! Who invented the Python programming language was Guido van Rossum.")

print()

p3 = input("What type of software system does TOTVS develop?")
if p3.lower() == "erp" or p3.lower() == "enterprise resource planning":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! TOTVS develops ERP system (Enterprise Resource Planning).")

print()

p4 = input("Who is considered the father of Artificial Intelligence?")
if p4.lower() == "alan" or p4.lower() == "turing" or p4.lower() == "alan turing":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The father of Artificial Intelligence is Alan Turing.")

print()

p5 = input("What is the name given to the set of instructions, data or logical programs used to operate computers and devices?")
if p5.lower() == "software":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is software.")

print()

p6 = input("What is the physical and tangible part of computers and electronic devices, including internal components (processor, memory, motherboard) and external (mouse, keyboard, monitor)?")
if p6.lower() == "hardware":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is hardware.")

print()

p7 = input("What is the name of an accumulated list of unfinished tasks, requirements, or work items that need to be addressed, often prioritized by importance?")
if p7.lower() == "backlog":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is backlog.")

print()

p8 = input("What is the process of reverting a system, database, or software application to a previous, stable state to undo errors, faulty updates, or undesirable changes?")
if p8.lower() == "rollback":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is rollback.")

print()

p9 = input("What is a distinctive attribute, aspect, or functionality of a product, system, or service that adds value, improves usability, or makes it unique?")
if p9.lower() == "feature":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is feature.")

p10 = input("what is the most recommended language for automation?")
if p10.lower() == "python":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! It is Python.")

p11 = input("What does CPU stand for?")
if p11.lower() == "central processing unit":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! CPU stands for Central Processing Unit.")

print()

p12 = input("Which protocol is used to securely browse websites (encrypted web traffic)?")
if p12.lower() == "https":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The correct answer is HTTPS.")

print()

p13 = input("What does RAM stand for?")
if p13.lower() == "random access memory":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! RAM stands for Random Access Memory.")

print()

p14 = input("Which database language is commonly used for querying relational databases?")
if p14.lower() == "sql" or p14.lower() == "structured query language":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The correct answer is SQL (Structured Query Language).")

print()

p15 = input("What does DNS stand for?")
if p15.lower() == "domain name system":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! DNS stands for Domain Name System.")

print()

p16 = input("Which command is used in Git to create a copy of a remote repository locally?")
if p16.lower() == "git clone":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The command is git clone.")

print()

p17 = input("In cybersecurity, what does MFA stand for?")
if p17.lower() == "multi-factor authentication" or p17.lower() == "multifactor authentication":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! MFA stands for Multi-Factor Authentication.")

print()

p18 = input("What does API stand for?")
if p18.lower() == "application programming interface":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! API stands for Application Programming Interface.")

print()

p19 = input("Which cloud service model provides virtual servers, storage, and networking resources on demand?")
if p19.lower() == "iaas" or p19.lower() == "infrastructure as a service":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The correct answer is IaaS (Infrastructure as a Service).")

print()

p20 = input("What is the binary value of decimal number 10?")
if p20.lower() == "1010":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! Decimal 10 in binary is 1010.")

print()

p21 = input("What does LAN stand for?")
if p21.lower() == "local area network":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! LAN stands for Local Area Network.")

print()

p22 = input("Which HTTP method is commonly used to retrieve data from a server?")
if p22.lower() == "get":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The correct answer is GET.")

print()

p23 = input("What does SSD stand for in computer storage?")
if p23.lower() == "solid-state drive" or p23.lower() == "solid state drive":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! SSD stands for Solid-State Drive.")

print()

p24 = input("Which symbol is used in Python for single-line comments?")
if p24.lower() == "#" or p24.lower() == "hash" or p24.lower() == "hashtag":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! Single-line comments in Python use the # symbol.")

print()


p25 = input("What does URL stand for?")
if p25.lower() == "uniform resource locator":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! URL stands for Uniform Resource Locator.")

print()

p26 = input("What does VPN stand for?")
if p26.lower() == "virtual private network":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! VPN stands for Virtual Private Network.")

print()

p27 = input("Which port is used by default for HTTPS?")
if p27.lower() == "443":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The default HTTPS port is 443.")

print()

p28 = input("What does OS stand for in computing?")
if p28.lower() == "operating system":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! OS stands for Operating System.")

print()

p29 = input("Which data structure uses LIFO order?")
if p29.lower() == "stack":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The correct answer is Stack.")

print()

p30 = input("Which SQL clause is used to filter query results?")
if p30.lower() == "where":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The clause is WHERE.")

print()

p31 = input("What does IDE stand for?")
if p31.lower() == "integrated development environment":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! IDE stands for Integrated Development Environment.")

print()

p32 = input("Which Linux command is used to change directory?")
if p32.lower() == "cd":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The command is cd.")

print()

p33 = input("What does JSON stand for?")
if p33.lower() == "javascript object notation":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! JSON stands for JavaScript Object Notation.")

print()

p34 = input("Which company developed the Java programming language?")
if p34.lower() == "sun microsystems" or p34.lower() == "sun":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! Java was developed by Sun Microsystems.")

print()

p35 = input("What does GUI stand for?")
if p35.lower() == "graphical user interface":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! GUI stands for Graphical User Interface.")

print()

p36 = input("Which keyword is used in Python to define a function?")
if p36.lower() == "def":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! Use def to define a function in Python.")

print()

p37 = input("What does BIOS stand for?")
if p37.lower() == "basic input output system" or p37.lower() == "basic input/output system":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! BIOS stands for Basic Input/Output System.")

print()

p38 = input("In networking, what does IP stand for?")
if p38.lower() == "internet protocol":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! IP stands for Internet Protocol.")

print()

p39 = input("Which Git command is used to upload local commits to a remote repository?")
if p39.lower() == "git push":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! The command is git push.")

print()

p40 = input("What does HTML stand for?")
if p40.lower() == "hypertext markup language":
  points += 1
  print("Correct! Points:",points,"/ 40")
else:
  print("Wrong! HTML stands for HyperText Markup Language.")

if points == 40:
  print("Congratulations, you won! You got all the questions right!")
elif points >= 28:
  print("Good! You got",points,"/ 40 correct!")
elif points >= 20:
  print("Median score. You got",points,"/ 40 correct!")
else:
  print("You lost! You got",points,"/ 40 correct!")
print(f"Thank you for playing, {name}!")
