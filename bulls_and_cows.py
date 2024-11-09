"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Dita Velčevová
email: d.velcevova@gmail.com
discord: dita8703
"""

import random
import time

separator = "-" * 47

def say_hello():
    """
    Vytiskne úvodní zprávu pro hráče.
    """
    print("Hi there!")
    print(separator)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    print("If you want to give up, press 'X'.")
    print(separator)

def generate_secret_number():
    """
    Vygeneruje náhodné 4-ciferné číslo bez duplicitních číslic.
    
    Vrací:
        str: Náhodné 4-ciferné číslo jako řetězec.
    """
    return ''.join(random.sample('1234567890', 4))

def check_tip(tip):
    """
    Ověří platnost vstupního čísla hráče (tip).

    Argumenty:
        tip (str): Číslo, které hráč zadal jako tip.
    
    Vrací:
        str nebo None: Chybová zpráva, pokud je vstup neplatný, jinak None.
    """
    # Ověření délky a formátu
    if not tip.isdigit() or len(tip) != 4:
        return "The number must be 4 digits long and contain only digits."  
    
    # Ověření, že číslo nezačíná nulou
    if tip[0] == '0':
        return "The number cannot start with zero."
    
    # Ověření, že číslo neobsahuje duplicitní číslice
    if len(set(tip)) != len(tip):
        return "The number cannot contain duplicate digits."
    
    return None

def evaluate_tip(secret_number, tip):
    """
    Vyhodnocení tipu hráče vůči tajnému číslu.

    Argumenty:
        secret_number (str): Tajné číslo.
        tip (str): Tip hráče.
    
    Vrací:
        tuple: Počet bulls (správné číslice na správných pozicích) a cows (správné číslice na nesprávných pozicích).
    """
    bulls = 0
    cows = 0
    
    for a, b in zip(secret_number, tip):
        if a == b:
            bulls += 1
        elif b in secret_number:
            cows += 1
    return bulls, cows

def print_result(bulls, cows):
    """
    Vypíše výsledek vyhodnocení ve srozumitelné formě.

    Argumenty:
        bulls (int): Počet bulls (správné číslice na správných pozicích).
        cows (int): Počet cows (správné číslice na nesprávných pozicích).
    """

    if bulls == 1:
        bull_text = "1 bull"
    else:
        bull_text = f"{bulls} bulls"
    
    if cows == 1:
        cow_text = "1 cow"
    else:
        cow_text = f"{cows} cows"
    
    print(f"{bull_text}, {cow_text}")

def measure_time(start_time):
    """
    Funkce pro výpočet uplynulého času od start_time.

    Argumenty:
        start_time (float): Čas, kdy začal hráč hrát.

    Vrací:
        float: Uplynulý čas v sekundách.
    """
    return time.time() - start_time

def main():
    """
    Hlavní funkce pro spuštění hry Bulls and Cows.
    """
    say_hello()
    secret_number = generate_secret_number()
    attemps = 0
    start_time = time.time()

    while True:
        tip = input("Enter a number: ")
        
        # Kontrola pro vzdání se hry
        if tip.upper() == 'X':
            print("You have given up. The secret number was:", secret_number)
            break
        
        # Ověření, zda je tip validní
        fail = check_tip(tip)
        if fail:
            print(fail)
            continue

        attemps += 1
        bulls, cows = evaluate_tip(secret_number, tip)
        print_result(bulls, cows)

        print(separator) 

        # Pokud hráč uhodl číslo
        if bulls == 4:
            elapsed_time = measure_time(start_time)
            print(f"Correct, you've guessed the right number in {attemps} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            print(separator)
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()
