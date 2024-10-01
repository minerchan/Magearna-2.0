from funcoes import *

while True:
    try:
        move1 = pyautogui.locateOnScreen('./imagens/x.png', confidence=0.9)
        print(move1)
        pyautogui.moveTo(move1)
        break

    except pyautogui.ImageNotFoundException:
        print("não achei o botão lutar")
        time.sleep(0.2)
        