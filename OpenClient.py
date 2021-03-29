from pyautogui import press, sleep, write

def open_browser() -> None:
    press('win')
    write('edge')
    press('enter')
    
def open_gmail() -> None:
    press('f4')
    write('https://mail.google.com/mail/u/1/#inbox')
    press('enter')

def main() -> None:
    """
    Main program
    """
    print("Su le mani")
    
    open_browser()
    sleep(1)
    open_gmail()

if __name__=="__main__": 
    main()