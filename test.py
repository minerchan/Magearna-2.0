from funcoes import *

largura_da_tela, altura_da_tela = pyautogui.size()
regiao_esquerda_da_tela = (0, 0, largura_da_tela // 2, altura_da_tela)

pyautogui.click(regiao_esquerda_da_tela)
posicao_escape = (900, 58, 43, 33)
pyautogui.moveTo(posicao_escape)
time.sleep(0.5)
pyautogui.click()

teleporte = (753, 45, 49, 52)
pyautogui.moveTo(teleporte)
time.sleep(0.4)
pyautogui.click()
# tempo para estar no pokecenter
time.sleep(7)
manter_pressionado_a_tecla('K', 0.5)
time.sleep(1)
manter_pressionado_a_tecla('K', 0.5)
# healando o pokemon
time.sleep(6)
manter_pressionado_a_tecla('K', 0.5)
time.sleep(1)