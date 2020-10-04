from playsound import playsound
import random
import sys
import pyfiglet

def welcome():
    f = pyfiglet.Figlet(font='isometric1')
    print(f.renderText("THE MIMIK"))
    print("The Mimik: gra tekstowa o skrzyni potworze.\n")
    print("Witaj mimiku! Jesteś potworem o wyglądzie skrzyni, który zjada ludzi. W swoim życiu musisz podjąć decyzje czy zjeść człowieka, ukryć się i oddać skarby albo uciec narażając się na pościg lub wykrycie.")

#---------STAGES---------#
def firstStage(health):
    print("\nObok Ciebie przechodzi wieśniak uzbrojony w widły. Co robisz?")
    while True:
        try:
            playerChoice = int(input("1. Zwróć na siebie uwagę\t2. Schowaj się: "))
            break
        except ValueError:
            wrongChoiceMessage()
            continue

    if playerChoice == 1:
        playsound('sounds/whistle.mp3')
        while True:
            try:
                playerChoice = int(input("Pomyślnie przyciągasz uwagę wieśniaka. Co chcesz zrobić?\n1. Zjedz go\t2. Oddaj skarby: "))
                break
            except ValueError:
                wrongChoiceMessage()
                continue
        if playerChoice == 1:
            print("Zjadasz wieśniaka i zyskujesz 10HP")
            health += 10
            healthInfoMessage(health)
            playsound('sounds/eating.mp3')

        elif playerChoice == 2:
            print("Oddałeś skarby wieśniakowi. Tracisz 5HP!")
            playsound('sounds/treasures.mp3')
            health -= 5
            if health <= 0:
                endGame()
            healthInfoMessage(health)

    elif playerChoice == 2:
        print("Chowasz się i czekasz na następną ofiarę")
        playsound('sounds/crickets.mp3')
        healthInfoMessage(health)

    else:
        wrongChoiceMessage()
        firstStage(health)

    return health

def secondStage(health):
    print("\nZbliża się do Ciebie Palladyn ubarany w błyszczącą zbroje,  wyposażony w magiczny, dwuręczny miecz, który dzierży w jednej ręce. \nDo tego widzisz tarcze w jego drugiej ręce. Jaką decyzje podejmiesz?")
    while True:
        try:
            playerChoice = int(input("1. Walcz\t2. Uciekaj\t3. Oddaj skarby: "))
            break
        except ValueError:
            wrongChoiceMessage()
            continue

    if playerChoice == 1:
        playsound('sounds/fight.mp3')
        print("Podejmujesz walkę, ale z marnym skutkiem!")
        playsound('sounds/ugh.mp3')
        endGame()

    elif playerChoice == 2:
        print("Próbujesz uciekać")
        playsound('sounds/footsteps.mp3')
        generate = random.randint(1,2)
        if generate == 1:
            print("Palladyn cię dogania, tracisz 99HP")
            playsound('sounds/ugh.mp3')
            health -= 99
            if health <= 0:
                endGame()
            healthInfoMessage(health)
        else:
            print("Udaje ci się uciec!")
            playsound('sounds/panting.mp3')
        healthInfoMessage(health)
        
    elif playerChoice == 3:
        print("Udaje Ci się przekonać wroga do wzięcia łapówki")
        playsound('sounds/treasures.mp3')
        healthInfoMessage(health)

    else:
        wrongChoiceMessage()
        secondStage(health)

    return health

def thirdStage(health):
    print("\nPodchodzi do Ciebie dwu osobowy zespół złożony z wojownika i uzdrowiciela. Twój wybór: ")
    while True:
        try:
            playerChoice = int(input("1. Walcz\t2. Oddaj skarby\t3. Uciekaj: "))
            break
        except ValueError:
            wrongChoiceMessage()
            continue

    if playerChoice == 1:
        health = fight(health)

    elif playerChoice == 2:
        print("Udaje Ci się przekonać wroga do wzięcia łapówki")
        playsound('sounds/treasures.mp3')
        healthInfoMessage(health)

    elif playerChoice == 3:
        runAway(health)

    else:
        wrongChoiceMessage()
        playsound('sonds/error.mp3')
        thirdStage(health)
    
    return health

#---------STAGES---------#
def healthInfoMessage(health):
    print("Twoje punkty zdrowia:", health)

def wrongChoiceMessage():
    playsound('sounds/error.mp3')
    dialogOptions = ["Nie kombinuj!", "Nie masz innych opcji!", "Ciekawość może zabić!"]
    print('\n', random.choice(dialogOptions), '\n')

def endGame():
    print(pyfiglet.figlet_format("Giniesz", font = "banner3-D"))
    playsound('sounds/you_lose.mp3')
    input("Nacisnij enter aby zamknąć")
    sys.exit()

def fight(health):
    print("Kogo chcesz zaatakować?")
    while True:
        try:
            playerChoice = int(input("1. Wojownika\t2. Uzdrowiciela: "))
            break
        except ValueError:
            wrongChoiceMessage()
            continue

    if playerChoice == 1:
        print("Podejmujesz walkę z wojownikiem, który jest leczony przez uzdrowiciela.")
        playsound('sounds/fight.mp3')
        print("Tracisz 50HP")
        playsound('sounds/ugh.mp3')
        health -= 50
        healthInfoMessage(health)
        if health <= 0:
            endGame()

    elif playerChoice == 2:
        playsound('sounds/fight.mp3')
        print("Uzdrowiciel ginie. Wojownik sam nie daje rady po walce z tobą ginie. Zjadasz obydwa trupy")
        health += 25
        healthInfoMessage(health)

    else:
        wrongChoiceMessage()
    
    return health

def runAway(health):
    print("Próbujesz uciekać")
    playsound('sounds/footsteps.mp3')
    generate = random.randint(1,2)
    if generate == 1:
        print("Udaje Ci się uciec!")
        playsound('sounds/panting.mp3')
        healthInfoMessage(health)
    else:
        enemiesAreChasing(health)

def enemiesAreChasing(health):
    print("Wrogowie Cię gonią! Co chcesz zrobić?")
    while True:
        try:
            playerChoice = int(input("1. Walcz\t2. Uciekaj: "))
            break
        except ValueError:
            wrongChoiceMessage()
            continue

    if playerChoice == 1:
        health = fight(health)
    elif playerChoice == 2:
        runAway(health)
    else:
        wrongChoiceMessage()
        enemiesAreChasing(health)

def winScreen():
    print(pyfiglet.figlet_format("Koniec Gry!", font = "banner3-D"))
    playsound('sounds/you_win.mp3')
    input("Nacisnij enter aby zamknąć")

def main():
    health = 100
    funcHealth = 0
    welcome()
    x = []
    while len(x) != 3:
        randomStage = random.randint(1, 3)
        if randomStage not in x:
            x.append(randomStage)
            if randomStage == 1:
                funcHealth = firstStage(health)
                health = funcHealth
            elif randomStage == 2:
                funcHealth = secondStage(health)
                health = funcHealth
            else:
                funcHealth = thirdStage(health)
                health = funcHealth

    winScreen()


main()