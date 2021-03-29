from DateTime import DateTime
from pyautogui import ImageNotFoundException, click, locateCenterOnScreen, moveTo, sleep
import pyautogui
import OpenClient
from WriteMail import setTime, writeMail
import random

def colored(r, g, b, text): #colored(255, 0, 0, text)
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def randomOggetto():
    oggetti = ["Indovina di chi e' questa mail?", 
               "Tanti auguri al migliore amico del mondo :)", 
               "Fra c'ho speso una notte",
               "Bro stai invecchiando",
               "E questa e' la numero????",
               ":)))))))",
               "In onore di tutte le partite di Minecraft giocate assieme",
               "16 anni wow",
               "Bro stai invecchiando",
               "LOL",
               "lol",
               "lollllllllll",
               "Never gonna give you up, nananananana"]
    
    return random.choice(oggetti)
    
def randomCorpo():
    corpi = ["*Mail formale lol*\nBuongiorno Mr. Nicolo',\noggi abbiamo sapute che lei compie 16 anni e siamo lieti di porgerle i nostri auguri.\nCon ammirazione,\nIl Team Mojang",
             "Pazzesco oggi compi 16 anni, e di questi 16 anni 12 tipo li hai vissuti con me, wow che storia la nostra amicizia",
             "Cara Nicolo',\nsono Nicole Aniston e sarei felici di invitarti assieme a me ad una serata.\nCon affetto,\nIo e il Team Brazzers <3",
             "Soldato, qua ci siamo conosciuti, che ricordi :'( --> https://goo.gl/maps/ksSEYaVaa6gDYcbs8",
             "Se vuoi ti do' il codice sorgente di questo programma...",
             "Con le ragazze c'e' solo una via, cioe' --> https://youtu.be/dQw4w9WgXcQ",
             "Ore 05 e 36 il programma sta ancora mando le mail, sono 3 ore che va avanti cosi' inizio a pensare di aver esagerato lol",
             "L\nO\nL"]
    
    return random.choice(corpi)

pyautogui.FAILSAFE = False

#var
writeButtonLocation = None
MAIL = 'zampierinicolo0@gmail.com'
ora = DateTime(14, 46)

OpenClient.main()

while True:
    try:
        writeButtonLocation = locateCenterOnScreen('Source\\Scrivi.jpeg', confidence = 0.9, grayscale = True)
        
        if writeButtonLocation == None:
            print("Non trovato")
            continue
        else:
            moveTo(0,0)
        
        break
    except ImageNotFoundException:
        continue
    
print(writeButtonLocation)

print(colored(255, 0, 0, 'Inizio Spam'))

while True:
    sleep(1)
    
    #open box
    click(writeButtonLocation)

    writeMail(MAIL, randomOggetto(), randomCorpo())
    setTime(ora.toStr())
    print(colored(255, 255, 0, f'Consegnata alle {ora.toStr()}'))
    ora.addTime(minute=2)
    
    if '2' in ora.toStr()[0] and '4' in ora.toStr()[1]:
        print('Fine')
        break
    
print('Programma concluso')