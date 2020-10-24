import random
import pyautogui
import string
#char= "abcdefghijklmnopqrstuvwxyz"
char = string.printable
char_lst = list(char)

password = pyautogui.password("Enter a password : ")
guess_password =""

while (guess_password != password):
    guess_password = random.choices(char_lst, k=len(password))

    print("<==============="+ str(guess_password)+ "===============>")

    if (guess_password == list(password)) :
        print("Your password is :"+"".join(guess_password))
        break
