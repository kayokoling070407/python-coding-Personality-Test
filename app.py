print("CCA Personality Test")
print()
print("Welcome! Please answer the following questions truthfully to your own preferences and I will suggest a CCA which might be suitable for you based on your personality and your interests.")
print("Please answer the questions with numbers 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

Com1 = input("I enjoy coding and computing lessons.")
Bball1 = input("I love to stay active!")
Orchestra1 = input("I love to play musical instruments.")
Drama1 = input("I like to act and perform.")

Com2 = input("I'm good at coding and helping others solve computing problems.")
Orchestra2 = input("I play at least one musical instrument well.")
Drama2 = input("I want to perform in front of people.")

outdoor3 = input("I have experiene in partcipating in art competitions.")

music3 = input("I can see shapes and colours everywhere I go.")

tech4 = input("I listen to chinese music often.")

outdoor4 = input("I feel calm and relaxed when I listen to an orchestra play music.")

music4 = input("I hope to be part of an orchestra.")

tech5 = input("I like watching plays and dramas.")

outdoor5 = input("I enjoy conversing with others in mandarin.")

music5 = input("I like working with props, music and lights backstage.")


tech_final = int(tech1) + int(tech2) + int(tech3)
outdoor_final = int(outdoor1) + int(outdoor2) + int(outdoor3)
music_final = int(music1) + int(music2) + int(music3)

print()

if tech_final > outdoor_final and tech_final > music_final:
  print("You might be suitable for Infocomm club!")
if outdoor_final > music_final:
  print("You might be stuiable for ODAC!")
if music_final > outdoor_final:
  print("You might be suitable for Band!")
if tech_final == outdoor_final :
  print("You might be suitable for Art Club!")
if outdoor_final == tech_final or outdoor_final == music_final: 
  print("You might be suitable for Chinese Orchestra!")
if music_final > tech_final and music_final > outdoor_final: 
  print("You might be suitable for Chinese Drama!")
