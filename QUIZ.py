print("==========Quiz=de=TI==========")

print()

pontos = 0

p1 = input("Quem foi a primeira programadora do mundo?")
if p1.lower() == "ada lovelace" or p1.lower() == "ada" or p1.lower() == "lovelace":
  pontos += 1
  print("Correto! Pontos:",pontos,"/ 3")
else:
  print("Errado! A primeira programadora do mundo foi Ada Lovelace.")

print()

p2 = input("Quem inventou a linguagem de programação Python?")
if p2.lower() == "guido" or p2.lower() == "guido van" or p2.lower() == "guido van rossum":
  pontos += 1
  print("Correto! Pontos:",pontos,"/ 3")
else:
  print("Errado! Quem inventou a linguagem de programação Python foi Guido van Rossum.")

print()

p3 = input("Qual tipo de sistema de software a TOTVS desenvolve?")
if p3.lower() == "erp" or p3.lower() == "enterprise resource planning" or p3.lower() == "planejamento de recursos empresariais":
  pontos += 1
  print("Correto! Pontos:",pontos,"/ 3")
else:
  print("Errado! A TOTVS desenvolve sistema de ERP (Enterprise Resource Planning).")

print()

if pontos == 3:
  print("Parabéns, você ganhou! Acertou todas as questões!")
else:
  print("Você perdeu! Acertou",pontos,"/ 3!")
