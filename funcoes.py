import pyautogui
import time
from playsound import playsound
from colorama import Fore, Style



def clicar_no_move_1():
    
    move1 = (211, 638, 114, 24)
    pyautogui.moveTo(move1, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    
def clicar_no_move_2():
    move2 = (440, 627, 282, 47)
    pyautogui.moveTo(move2, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    
def clicar_no_move_4():
    move4 = (549, 722, 69, 19)
    pyautogui.moveTo(move4, duration=0.2)
    pyautogui.click()
    time.sleep(0.5)
    
def clicar_na_pokeball():
    pokeball = (404, 467, 130, 25)
    pyautogui.moveTo(pokeball, duration=0.2)
    pyautogui.click()
    # Tempo da ball rolar 3x
    time.sleep(7)
    
    
    
def Clicar_ataque_e_False_Swipe_mais_tempo_de_animacao_do_inimigo(tempo):
    # Clicar em ataque
    clicar_no_move_1()
    # Segudno False swipe
    clicar_no_move_1()
    # Esperar animação do False Swipe e animação do ataque dele que pode ser grande
    time.sleep(tempo)


# Esta função espera uma string no 1 argumento um number no 2
def manter_pressionado_a_tecla(tecla, segundos):
    # aperta a tecla
    pyautogui.press(tecla)
    # Pressiona a tecla '...'
    pyautogui.keyDown(tecla)
    # Aguarda 2 segundos
    time.sleep(segundos)
    # Solta a tecla '...'
    pyautogui.keyUp(tecla)
    
def texto_verde(texto):
    print(Fore.GREEN + texto)

def texto_vermelho(texto):
    print(Fore.RED + texto)

def texto_amarelo(texto):
    print(Fore.YELLOW + texto)
