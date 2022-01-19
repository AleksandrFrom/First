"""Finde numbers"""

import numpy as np

number = np.random.randint(1, 101) # think about number

#quality time
count = 0

while True:
    count+=1
    predict_number = int(input("Ugaday chislo ot 1 do 100:  "))
    if predict_number > number:
        print("Chislo nado menshe")
        
    elif predict_number < number:
        print("Chislo nado bolshe")
    else:
        print(f"Vy ugadali! Eto chislo ={number} za {count} popitok")
        break # end game and exit from cycle