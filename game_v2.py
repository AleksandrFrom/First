"""Finde numbers
Computer own work"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomno ugadivaetsya chislo

    Args:
        number (int, optional): Zagadanoe chislo. Defaults to 1.

    Returns:
        : chislo popitok
    """
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #predpolagaemoe chislo
        if number == predict_number:
            break # end cycle
    return(count) 

def score_game(random_predict) -> int:
    """Za kakoe kolichestvo podhodov proishodit ugadivanie

    Args:
        random_predict ([type]): funkciya ugadivaniya

    Returns:
        int: srednee kolichestvo popitok
    """
    count_ls = []
    np.random.seed(1) #fiksiruem seed dlya vosproizvodimosti
    random_array = np.random.randint(1, 100, size=1000) # zagadali spisok chisel
    for number in random_array:
        count_ls.append(random_predict(number))
    score=int(np.mean(count_ls))
    print(f'Vash algoritm ugadivaet chislo d srednem za :{score} popitok')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(random_predict)