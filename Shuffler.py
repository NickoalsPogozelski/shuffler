import string
import random

user_input = input("escreva sua palavra aqui: ")
string_user = list(str(user_input))
random.shuffle(string_user)
print ("aqui está sua palavra: " + string_user)