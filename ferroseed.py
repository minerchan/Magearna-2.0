
from funcoes import *

largura_da_tela, altura_da_tela = pyautogui.size()
regiao_esquerda_da_tela = (0, 0, largura_da_tela // 2, altura_da_tela)

pyautogui.click(regiao_esquerda_da_tela)
time.sleep(1)


# Contagem de pokemons capturados
contagem_de_pokemons_capturados = 0
contagem_de_pokemons_vistos = 0

# Variável que controla o loop eterno, se ela nunca for True loop nunca para
controle_de_loop_eterno = False


while controle_de_loop_eterno is False:
# ================================================ BLOCO PARA CONFERIR SE ENTROU EM LUTA / FICAR ANDANDO ================================================
    relatorio_de_ter_entrado_em_luta = "Não definido"
    controle_da_luta = False
    while controle_da_luta is False:
        try:
            entramos_em_luta = pyautogui.locateOnScreen('./imagens/entramos_em_luta.png', confidence=0.8, region=(regiao_esquerda_da_tela))
            relatorio_de_ter_entrado_em_luta = "Entramos em luta!"
            controle_da_luta = True
        except pyautogui.ImageNotFoundException:
                manter_pressionado_a_tecla('A', 0.5)
                manter_pressionado_a_tecla('D', 0.5)
    
    texto_amarelo(relatorio_de_ter_entrado_em_luta)
    print("=============================")            
# ================================================ BLOCO PARA CONFERIR SE É HORDA ================================================    
    relatorio_de_horda = "Não definido"
    controle_de_horda = False
    contador_de_checagem_de_horda = 0
    while controle_de_horda is False:
        try:
            entrou_em_luta_de_horda = pyautogui.locateOnScreen('./imagens/horda.png', confidence=0.8, region=(regiao_esquerda_da_tela))
            relatorio_de_horda = "É uma horda!"
            clicar_no_move_4()
            # tempo para animação de fugir acabar
            time.sleep(0.6)
            controle_de_luta_normal = True
            identificacao_do_pokemon = True
            controle_de_horda = True
        except pyautogui.ImageNotFoundException:
            contador_de_checagem_de_horda = contador_de_checagem_de_horda + 1
            time.sleep(0.2)

        if(contador_de_checagem_de_horda == 5):
            relatorio_de_horda = 'Não é uma horda'
            controle_de_luta_normal = False
            identificacao_do_pokemon = False
            controle_de_horda = True
    
    texto_amarelo(relatorio_de_horda)
    print("=============================")    
# ================================================ BLOCO PARA CONFERIR SE É LUTA NORMAL ================================================
    relatorio_de_luta_normal = "Não definido"
    
    while controle_de_luta_normal is False:
        try:
            entrou_em_luta_normal = pyautogui.locateOnScreen('./imagens/entrouemluta.png', confidence=0.8, region=(regiao_esquerda_da_tela))
            relatorio_de_luta_normal = 'É uma luta normal'
            controle_de_luta_normal = True
        except pyautogui.ImageNotFoundException:
            pass
        
    texto_amarelo(relatorio_de_luta_normal)
    print("=============================")
    
# ================================================ BLOCO PARA CONFERIR O POKÉMON ================================================
    relatorio_de_identificacao_do_pokemon = "Não definido"
    contador_de_vezes_para_ver_pokemon = 0
    while identificacao_do_pokemon is False:
        try:
            pokemon = pyautogui.locateOnScreen('./imagens/pokemon_ferroseed.png', confidence=0.7, region=(regiao_esquerda_da_tela))
            relatorio_de_identificacao_do_pokemon = 'Pokémon encontrado'
            tentar_capturar = True
            identificacao_do_pokemon = True
        except pyautogui.ImageNotFoundException:
            contador_de_vezes_para_ver_pokemon = contador_de_vezes_para_ver_pokemon + 1
            time.sleep(0.1)

        if(contador_de_vezes_para_ver_pokemon == 20):
            relatorio_de_identificacao_do_pokemon = "Não era o pokémom, estou fugindo"
            clicar_no_move_4()
            # tempo para animação de fugir acabar
            time.sleep(0.6)
            tentar_capturar = False
            identificacao_do_pokemon = True

    texto_amarelo(relatorio_de_identificacao_do_pokemon)
    print("=============================")

# ============================================== BLOCO PARA CAPTURAR O POKEMON SE tentar_capturar for True  ================================================
    contagem_de_pokemons_vistos = contagem_de_pokemons_vistos + 1
    relatorio_de_captura = "Não capturei"
    contador_de_checagem_se_foi_capturado = 0
    while tentar_capturar is True:
        Clicar_ataque_e_False_Swipe_mais_tempo_de_animacao_do_inimigo(15)
        Clicar_ataque_e_False_Swipe_mais_tempo_de_animacao_do_inimigo(15)
        # Apertar a mochila
        clicar_no_move_2()
        clicar_na_pokeball()
        time.sleep(0.5)
        try:
            pokebola_capturada = pyautogui.locateOnScreen('./imagens/pokebola_pegou.png', confidence=0.8, region=(regiao_esquerda_da_tela))
            # tempo para sair da tela da luta pós captura
            time.sleep(4)
            posicao_do_x = (832, 312, 16, 23)
            pyautogui.moveTo(posicao_do_x, duration=0.2)
            pyautogui.click()
            time.sleep(0.5)
            contagem_de_pokemons_capturados = contagem_de_pokemons_capturados + 1
            relatorio_de_captura = "Pokémon capturado"
            tentar_capturar = False
        except pyautogui.ImageNotFoundException:
            contador_de_checagem_se_foi_capturado = contador_de_checagem_se_foi_capturado + 1
            time.sleep(0.1)
        
        if(contador_de_checagem_se_foi_capturado == 20):
            texto_vermelho("Não foi capiturado o pokémon depois de 20 tentativas de checagem")
        
    texto_amarelo(relatorio_de_captura)
    print("=============================")
    texto_verde(f'Até agora vi: {contagem_de_pokemons_vistos} pokémons')
    texto_verde(f'Capturados: {contagem_de_pokemons_capturados} pokémons')
    
    
    
    
    #  quando for 2 pokemon capturado reiniciar pra 0 levar o meu poke pro hospital com teleporte e voltar para o campo
    if(contagem_de_pokemons_capturados == 2):
        posicao_escape = (900, 58, 43, 33)
        pyautogui.moveTo(posicao_escape)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(3)
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
        # Ir andando até o ponto da cave agora até acabar o repelente e confirmar que não quer usar outro
        posicao_do_repelente = (826, 47, 48, 45)
        pyautogui.moveTo(posicao_do_repelente)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(2)
        manter_pressionado_a_tecla('S', 3)
        time.sleep(1)
        manter_pressionado_a_tecla('A', 1.2)
        manter_pressionado_a_tecla('S', 3.2)
        manter_pressionado_a_tecla('A', 2) # 74
        manter_pressionado_a_tecla('S', 1.5)
        manter_pressionado_a_tecla('A', 4)
        manter_pressionado_a_tecla('D', 4)
        manter_pressionado_a_tecla('A', 2)
        manter_pressionado_a_tecla('A', 2)
        manter_pressionado_a_tecla('D', 3)
        manter_pressionado_a_tecla('A', 1.4)
        nao_repelente = (453, 623, 54, 23)
        pyautogui.moveTo(nao_repelente)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        contagem_de_pokemons_capturados = 0
        
        
    
    
    
    
    

