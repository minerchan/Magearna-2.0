from funcoes import *

largura_da_tela, altura_da_tela = pyautogui.size()
regiao_esquerda_da_tela = (0, 0, largura_da_tela // 2, altura_da_tela)

try:
    pokemon = pyautogui.locateOnScreen('./imagens/pokemon_sandile.png', confidence=0.8, region=(regiao_esquerda_da_tela))
    controle_de_pokemon = True
    print("achei o pokemon")
    controle_teste = True
    
except pyautogui.ImageNotFoundException:
    print("não achei o pokemon")
    time.sleep(0.2)