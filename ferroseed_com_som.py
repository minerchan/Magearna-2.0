

from funcoes import *

largura_da_tela, altura_da_tela = pyautogui.size()
regiao_esquerda_da_tela = (0, 0, largura_da_tela // 2, altura_da_tela)

pyautogui.click(regiao_esquerda_da_tela)
time.sleep(1)




controle_teste = False
while controle_teste is False:
    controle_da_luta = False
# Loop que fica andando de um lado para o outro até encontrar a luta
    while controle_da_luta is False:
        try:
            entrou_em_luta = pyautogui.locateOnScreen('./imagens/entrouemluta.png', confidence=0.9, region=(regiao_esquerda_da_tela))
            pyautogui.moveTo(entrou_em_luta, duration=0.2)
            controle_da_luta = True
        except pyautogui.ImageNotFoundException:
            # Aqui a imagem não foi encontrada então vamos esperar 0.2 segundos para tentar de novo
            manter_pressionado_a_tecla('A', 1)
            manter_pressionado_a_tecla('D', 1)
            
            
# tempo de resfriamento para dar tempo da interface parar
    time.sleep(2)
    controle_de_pokemon = False
    contador = 0
    while controle_de_pokemon is False:
        if(controle_de_pokemon is True):
            break
        try:
            try:
                horda = pyautogui.locateOnScreen('./imagens/horda.png', confidence=0.9, region=(regiao_esquerda_da_tela))
                clicar_no_move_4()
                controle_da_luta = True
            except pyautogui.ImageNotFoundException:
                pokemon = pyautogui.locateOnScreen('./imagens/pokemon_ferroseed.png', confidence=0.8, region=(regiao_esquerda_da_tela))
                playsound('./sons/achou.mp3')
                break
            
            
            controle_de_pokemon = True
            break
        except pyautogui.ImageNotFoundException:
            contador = contador + 1
            time.sleep(0.2)
            if(controle_de_pokemon is True):
                break
            else:
                if(contador == 10):
                    while True:
                        try:
                            print("não era ele")
                            clicar_no_move_4()
                            time.sleep(0.5)
                            pyautogui.click()
                            controle_de_pokemon = True
                            time.sleep(2)
                            controle_teste = False
                            break
                        except pyautogui.ImageNotFoundException:
                            
                            time.sleep(0.1)
                
                
            # Aqui a imagem não foi encontrada então vamos esperar 0.2 segundos para tentar de novo
            time.sleep(0.1)
