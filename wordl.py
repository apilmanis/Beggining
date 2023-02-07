import random
from colorama import Fore, Back, Style
#print(f"{Fore.RED}Tests{Style.RESET_ALL}!")

words = ["viens","divi","trīs","cits"]

while True:
    word = random.choice(words)
    gueesdWord = list("_" for _ in word)
    guessed = False
    dzīvibas = 5
    print(word)

    while dzīvibas > 0 and "".join(gueesdWord) != word:

        inp = input(f"Vārds: ({len(word)} burti): ")
        if len(inp) != len(word):
            continue
        
        

        for i in range(0, len(word)):
            if inp[i] == word[i]:
                print(f"{Back.GREEN}{inp[i]}{Style.RESET_ALL}", end="")
                gueesdWord[i] = inp[i]
                guessed = True
            elif inp[i] in word:
                    print(f"{Back.YELLOW}{inp[i]}{Style.RESET_ALL}", end="")
            else:
                print(f"{inp[i]}", end="")
        print()
        
        if not guessed:
            dzīvibas -= 1

        print(f'Dzīvības: {dzīvibas}')
        print(gueesdWord)

    if dzīvibas == 0:
        print("Game Over")
    else:   
        print("victory")

    if input("Vai sākt jaunu spēli? y/n ").lower() != "y":
        break