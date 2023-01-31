import random

words = ["viens","divi","trīs","cits"]

while True:
    word = random.choice(words)
    gueesdWord = list("_" for _ in word)
    print(gueesdWord)
    dzīvibas = 5

    print(word)

    while dzīvibas > 0 and "".join(gueesdWord) != word:

        inp = input("Burts: ")
        
        if inp == "":
            continue 
        inp = inp[0]
        
        print(inp)

        guessed = False
        for i in range(0, len(word)):
            if inp == word[i]:
                gueesdWord[i] = inp
                guessed = True


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