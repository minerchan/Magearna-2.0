from funcoes import *

largura_da_tela, altura_da_tela = pyautogui.size()
regiao_esquerda_da_tela = (0, 0, largura_da_tela // 2, altura_da_tela)

controle_de_combo_de_captura = False
while controle_de_combo_de_captura is False:
    try:
        botao_lutar = pyautogui.locateOnScreen('./imagens/lutar.png', confidence=0.8, region=(regiao_esquerda_da_tela))
        pyautogui.moveTo(botao_lutar, duration=0.1)
        pyautogui.click()
        controle_de_spore = False
        
        time.sleep(1)
        while controle_de_spore is False:
            try:
                botao_spore = pyautogui.locateOnScreen('./imagens/spore.png', confidence=0.8, region=(regiao_esquerda_da_tela))
                pyautogui.moveTo(botao_lutar, duration=0.1)
                pyautogui.click()
                print("cliquei no spore")
                # tempo da animação do spore
                time.sleep(8)
                controle_de_spore = True
                controle_de_false_swipe = False
                while controle_de_false_swipe is False:
                    try:
                        botao_false_swipe = pyautogui.locateOnScreen('./imagens/false_swipe.png', confidence=0.8, region=(regiao_esquerda_da_tela))
                        pyautogui.moveTo(botao_false_swipe, duration=0.1)
                        pyautogui.click()
                        print("cliquei no false swipe")
                        # tempo da animação do false swipe
                        time.sleep(6)
                        controle_de_false_swipe = True
                        controle_de_combo_de_captura = True
                    except pyautogui.ImageNotFoundException:
                        print("não achei o botão false swipe")
                        time.sleep(0.2)
            except pyautogui.ImageNotFoundException:
                print("não achei o botão spore")
                time.sleep(0.2)
        
       
        
    except pyautogui.ImageNotFoundException:
        print("não achei o botão lutar")
        time.sleep(0.2)