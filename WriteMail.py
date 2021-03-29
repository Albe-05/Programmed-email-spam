from pyautogui import ImageNotFoundException, click, hotkey, locateCenterOnScreen, moveTo, press, sleep, write
import pyperclip

recipientsBox = None
sendBox = None
objectBox = None
dateAndTimeButton = None

#setTime button
setTimeButtonX = 1257
setTimeButtonY = 975

CONTATORE = 0

def colored(r, g, b, text): #colored(255, 0, 0, text)
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def breakMail(mail):
    return mail.split('@')

def writeMail(recipient, object = 'Oggetto', body = 'Corpo') -> bool:
    
    global recipientsBox, sendBox, objectBox, CONTATORE
    
    sleep(1)
    
    #trova pulsante invia
    if sendBox == None:
        while True:
            try:
                sendBox = locateCenterOnScreen('Source\\Send.png', confidence = 0.9, grayscale = True)
                
                if sendBox == None:
                    print("Non trovato")
                    continue
                else:
                    moveTo(0,0)
                
                break
            except ImageNotFoundException:
                continue
    
    click(x=1416, y=714)
    print('Box aperto')
    
    #trova pulsante destinatari
    if recipientsBox == None:
        while True:
            try:
                recipientsBox = locateCenterOnScreen('Source\\Recipents.png', confidence = 0.9, grayscale = True)
                
                if recipientsBox == None:
                    print("Non trovato")
                    continue
                else:
                    moveTo(0,0)
                
                break
            except ImageNotFoundException:
                continue
    
    click(recipientsBox)
    
    #scrivere la mail che la @ non la vuole metttere
    newRecipent = breakMail(recipient)
    write(newRecipent[0])
    #press(chr(64))
    pyperclip.copy("@")
    hotkey("ctrl", "v")
    write(newRecipent[1])
    
    press('enter')
    print('Impostati i destinati')
    sleep(0.1)
    
    #trova pulsante oggetto
    if objectBox == None:
        while True:
            try:
                objectBox = locateCenterOnScreen('Source\\ObjectBox.png', confidence = 0.9, grayscale = True)
                
                if objectBox == None:
                    print("Non trovato")
                    continue
                else:
                    moveTo(0,0)
                
                break
            except ImageNotFoundException:
                continue
    
    click(objectBox)
    write(object)
    print('''Impostato l'oggetto''')
    sleep(0.1)
    
    click(x=1416, y=714)
    write(body)
    print('Impostato il corpo')
    sleep(0.1)
    
    CONTATORE += 1
    
    print(colored(0, 255, 255, 'Mail %s scritta'%CONTATORE))
    
def setTime(time):
    
    global dateAndTimeButton, CONTATORE
    
    click(setTimeButtonX, setTimeButtonY)
    press('up')
    press('enter')
    sleep(0.1)
    
    #locate date and time button
    if dateAndTimeButton == None:
        while True:
            try:
                dateAndTimeButton = locateCenterOnScreen('Source\\ChooseTime.jpeg', confidence = 0.9, grayscale = True)
                
                if dateAndTimeButton == None:
                    print("Non trovato")
                    continue
                else:
                    moveTo(0,0)
                
                break
            except ImageNotFoundException:
                continue
    
    click(dateAndTimeButton)
    sleep(0.1)
    press('tab')
    sleep(0.01)
    press('tab')
    sleep(0.01)
    press('tab')
    sleep(0.01)
    press('tab')
    
    write(time)
    press('enter')
    
    print(colored(0, 255, 255, 'Mail %s inviata'%CONTATORE))

if __name__=="__main__": 
    writeMail('zarpellon.alberto@gmail.com')