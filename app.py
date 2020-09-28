print("Title of program: CCA Personality Test")
print()
print("Welcome! Please answer the following questions truthfully according to your own preferences and I will suggest a CCA which might be suitable for you based on your personality and your interests.")
print("Please answer the questions with numbers 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

Com1 = input("I enjoy coding and computing lessons.")
Bball1 = input("I love to stay active!")
Orchestra1 = input("I love to play musical instruments.")
Drama1 = input("I like to act and perform.")
Art1 = input("I enjoy drawing or doing art during my free time.")

Com2 = input("I'm good at coding and helping others solve computing problems.")
Bball2 = input("I love to play sports!")
Orchestra2 = input("I play at least one musical instrument well.")
Drama2 = input("I want to perform in front of people.")
Art2 = input("I like to be creative and can draw/paint etc very well.")

Com3 = input("I have a lot of experience and is confident in computing.")
Bball3 = input("I like to run and play sports with my friends.")
Orchestra3 = input("I like to listen to chinese music.")
Drama3 = input("I like to handle with props, music, lights etc backstage.")
Art3 = input("I can express myself through art.")

Com4 = input("I feel confident and happy doing computing.")
Bball4 = input("I enjoy being competitive and like to win.")
Orchestra4 = input("I feel calm and relaxed when I listen to an orchestra.")
Drama4 = input("I enjoy watching plays and dramas.")
Art4 = input("I admire art a lot and loved it.")

Com5 = input("I hope to join Infocomm Club.")
Bball5 = input("I hope to be in a Basketball team.")
Orchestra5 = input("I hope to be part of an Orchestra.")
Drama5 = input("I hope to be in Drama Club.")
Art5 = input("I hope to express myself through art even more in Art Club.")


Com_final = int(Com1) + int(Com2) + int(Com3) + int(Com4) + int(Com5)
Bball_final = int(Bball1) + int(Bball2) + int(Bball3) + int(Bball4) + int(Bball5)
Orchestra_final = int(Orchestra1) + int(Orchestra2) + int(Orchestra3) + int(Orchestra4) + int(Orchestra5)
Drama_final = int(Drama1)+ int(Drama2)+ int(Drama3)+ int(Drama4)+ int(Drama5)
Art_final = int(Art1)+ int(Art2)+ int(Art3)+ int(Art4)+ int(Art5)

print()

if Com_final > Bball_final and Com_final > Orchestra_final and Com_final > Drama_final and Com_final > Art_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Infocomm club!")
if Bball_final > Com_final and Bball_final > Orchestra_final and Bball_final > Drama_final and Bball_final > Art_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Basketball!")
if Orchestra_final > Bball_final and Orchestra_final > Com_final and Orchestra_final > Drama_final and Orchestra_final > Art_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Chinese Orchestra!")
if Drama_final > Bball_final and Drama_final > Orchestra_final and Drama_final > Com_final and Drama_final > Art_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Drama Society!")
if Art_final > Bball_final and Art_final > Orchestra_final and Art_final > Com_final and Art_final > Drama_final:
  print("Based on your answers you have chosen, it's a high chance you are suitable for Art Club!")
