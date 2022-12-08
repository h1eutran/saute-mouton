from tabulate import tabulate
import random


# Defining lists

mouton = []
generated = []

option = eval(input("Please select a program: "))

# Defining function generator which test a range of random number

def generator():
  a = 1 #random.randint(1,9)
  b = 2 #random.randint(0,1)
  c = random.randint(0,9)
  # Create the number in the form abc
  composed = a*100+b*10+c
  
  list = [a,b,c]
  generated.append(composed)
  
  counter=c
  while composed>counter:
    counter=counter+a
    list.append(counter)
    counter=counter+b
    list.append(counter)
    counter=counter+c
    list.append(counter)
  if composed==counter:
    mouton.append(counter)

# Making a table
def table():
  mouton_count = len(mouton)
  generated_count = len(generated)
  mouton.sort()
  generated.sort()
  no_dup_generated = list(dict.fromkeys(generated))        
  no_dup_mouton = list(dict.fromkeys(mouton))

  col_names = ["Total Generated","List of Generated Numbers","Total Moutons","List of Mouton"]
  data = [[generated_count,no_dup_generated, mouton_count, no_dup_mouton]]
  print(tabulate(data, headers=col_names))


# Asking user for inputing a number of choice
def manually():
  number = eval(input("Please input a number: "))
  digits = [int(x) for x in str(number)]
  letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  #numbers = [(ord(letter) - ord("A") + 1) = digits for letter in letters]
  print()



def function_select():
  if option == 1:
    for i in range(1,100):
        generator ()
    table()
function_select()