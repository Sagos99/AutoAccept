'''
    Auto accept para League of Legends PT-BR
    Criado por Sagos dia 01/01/2019
    Funcionando na versao 9.1
'''

import pyautogui
from time import sleep


################# Configuraçoes do Jogador ###############
mode = 3
champ = 'pyke'
banir = 'morgana'
primary_lane = 'sup'
second_lane = 'mid'
##########################################################


action_time = 0.8
first_lane_selected = False


def select(status):
    global first_lane_selected

    if status == 'play':
        button_play = pyautogui.locateCenterOnScreen('img/lol/button_play.png', grayscale=True)

        if button_play != None:
            pyautogui.click(button_play)
            print('Botao encontrado: Jogar')
            sleep(action_time)

            if mode == 1:
                select('button_confirm_mode')
            elif mode == 2:
                select('queue_normal')
            elif mode == 3:
                select('queue_duo')
            elif mode == 4:
                select('queue_flex')
        else:
            button_play_inactive = pyautogui.locateCenterOnScreen('img/lol/button_play_inactive.png', grayscale=True)
            if button_play_inactive != None:
                print('Botao jogar inativo')
                select('begin')
            else:
                print('Procurando botao: Jogar')
                sleep(action_time)
                select('play')

    if status == 'begin':
        button_begin = pyautogui.locateCenterOnScreen('img/lol/button_begin.png', grayscale=True)

        if button_begin != None:
            pyautogui.click(button_begin)
            print('Botao encontrado: Inicio')
            sleep(action_time)
            select('play')
        else:
            print('Procurando botao: Inicio')
            sleep(action_time)
            select('begin')

    if status == 'queue_duo':
        queue_duo = pyautogui.locateCenterOnScreen('img/lol/queue_duo.png', grayscale=True)
        queue_duo_selected = pyautogui.locateCenterOnScreen('img/lol/queue_duo_selected.png', grayscale=True)
    
        if queue_duo != None:
            pyautogui.click(queue_duo)
            print('Modo de jogo: Ranqueada Solo/Duo')
            sleep(action_time)
            select('button_confirm_mode')
        elif queue_duo_selected != None:
            select('button_confirm_mode')
        else:
            print('Procurando modo: Ranqueada Solo/Duo')
            sleep(action_time)
            select('queue_duo')

    if status == 'button_confirm_mode':
        button_confirm_mode = pyautogui.locateCenterOnScreen('img/lol/button_confirm_mode.png', grayscale=True)

        if button_confirm_mode != None:
            pyautogui.click(button_confirm_mode)
            pyautogui.moveRel(None,-100)
            print('Botao encontrado: Confirmar')
            sleep(action_time)

            if mode == 1:
                select('find_match')
            else:
                select('select_lane')
        else:
            print('Procurando botao: Confirmar')
            sleep(action_time)
            select('button_confirm_mode')

    if status == 'select_lane':
        select_lane = pyautogui.locateCenterOnScreen('img/lol/select_lane.png', grayscale=True)

        if select_lane != None:
            pyautogui.moveTo(select_lane)
            pyautogui.mouseDown(button='left')

            if first_lane_selected == False:
                if primary_lane == 'mid':
                    pyautogui.moveRel(None,-100)
                    first_lane_selected = True
                    pyautogui.mouseUp(button='left')
                    print('Lane primaria selecionada: MID')
                    pyautogui.moveRel(None,-200)
                    select('select_lane')
                elif primary_lane == 'top':
                    pyautogui.moveRel(-100,None)
                    first_lane_selected = True
                    pyautogui.mouseUp(button='left')
                    print('Lane primaria selecionada: TOP')
                    pyautogui.moveRel(None,-200)
                    select('select_lane')
                elif primary_lane == 'sup':
                    pyautogui.moveRel(100,None)
                    first_lane_selected = True
                    pyautogui.mouseUp(button='left')
                    print('Lane primaria selecionada: SUP')
                    pyautogui.moveRel(None,-200)
                    select('select_lane')
                elif primary_lane == 'jg':
                    pyautogui.moveRel(-100,-100)
                    first_lane_selected = True
                    pyautogui.mouseUp(button='left')
                    print('Lane primaria selecionada: JG')
                    pyautogui.moveRel(None,-200)
                    select('select_lane')
                elif primary_lane == 'adc':
                    pyautogui.moveRel(100,-100)
                    first_lane_selected = True
                    pyautogui.mouseUp(button='left')
                    print('Lane primaria selecionada: ADC')
                    pyautogui.moveRel(None,-200)
                    select('select_lane')
                else:
                    pyautogui.moveRel(None,100)
                    pyautogui.mouseUp(button='left')
                    print('Lane  primaria selecionada: Preencher')
                    select('find_match')
            else:
                if second_lane == 'mid':
                    pyautogui.moveRel(None,-100)
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: MID')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
                elif second_lane == 'top':
                    pyautogui.moveRel(-100,None)
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: TOP')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
                elif second_lane == 'sup':
                    pyautogui.moveRel(100,None)
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: SUP')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
                elif second_lane == 'jg':
                    pyautogui.moveRel(-100,-100)
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: JG')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
                elif second_lane == 'adc':
                    pyautogui.moveRel(100,-100)
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: ADC')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
                else:
                    first_lane_selected = False
                    pyautogui.mouseUp(button='left')
                    pyautogui.moveRel(None,100)
                    pyautogui.mouseUp(button='left')
                    print('Lane secundária selecionada: Preencher')
                    pyautogui.moveRel(None,-200)
                    select('find_match')
        else:
            print('Tentando selecionar lane')
            sleep(action_time)
            select('select_lane')

    if status == 'find_match':
        find_match = pyautogui.locateCenterOnScreen('img/lol/find_match.png', grayscale=True)

        if find_match != None:
            pyautogui.click(find_match)
            if mode == 1:
                print('Entrou na fila: Escolha as cegas')
            elif mode == 2:
                print('Entrou na fila: Escolha alternada')
            elif mode == 3:
                print('Entrou na fila: Ranqueada Solo/Duo')
            else:
                print('Entrou na fila: Ranqueada Flexivel')
            sleep(action_time)
            select('accept')
        else:
            print('Procurando botao: Encontrar partida')
            sleep(action_time)
            select('find_match')

    if status == 'accept':
        button_accept = pyautogui.locateCenterOnScreen('img/lol/button_accept.png', grayscale=True)

        if button_accept != None:
            pyautogui.click(button_accept)
            print('Partida aceita')
            sleep(action_time)
            select('verify')
        else:
            in_queue = pyautogui.locateCenterOnScreen('img/lol/in_queue.png', grayscale=True)
            button_accept = pyautogui.locateCenterOnScreen('img/lol/button_accept.png', grayscale=True)

            if in_queue != None:
                print('Na fila')
                sleep(action_time)
                select('accept')
            elif button_accept != None:
                pyautogui.click(button_accept)
                print('Partida aceita')
                sleep(action_time)
                select('verify')
            else:
                print('Na fila')
                sleep(action_time)
                select('accept')

    if status == 'verify': # Sagos
        button_accept = pyautogui.locateCenterOnScreen('img/lol/button_accept.png', grayscale=True)
        in_queue = pyautogui.locateCenterOnScreen('img/lol/in_queue.png', grayscale=True)
        find_match = pyautogui.locateCenterOnScreen('img/lol/find_match.png', grayscale=True)
        search_champ = pyautogui.locateCenterOnScreen('img/lol/search_champ.png', grayscale=True)
        print('Aguardando seleçao de campeao')

        if search_champ != None:
            select('search_champ')
        elif button_accept != None or in_queue != None:
            select('accept')
        elif find_match != None:
            select('find_match')
        else:
            select('verify')

    if status == 'search_champ':
        search_champ = pyautogui.locateCenterOnScreen('img/lol/search_champ.png', grayscale=True)

        if search_champ != None:
            if mode == 1:
                pyautogui.click(208,690) # Barra de escrita
                pyautogui.typewrite(primary_lane+'\n')
                print('Escreveu lane desejada')
                pyautogui.click(829,108) # Busca de champ
                pyautogui.typewrite(champ)
                sleep(0.5)
                pyautogui.click(421,170) # Selecionar o champ
                sleep(0.5)
                pyautogui.click(680,608) # Botao de confirmar champ
            elif mode == 2:
                pass
            elif mode == 3:
                pyautogui.click(search_champ)
                pyautogui.typewrite(champ)
                sleep(0.5)
                pyautogui.click(421,170) # Selecionar o champ

    if status == 'csgo':
        cs_accept = pyautogui.locateCenterOnScreen('img/csgo/accept.png', grayscale=True)
        cs_accept2 = pyautogui.locateCenterOnScreen('img/csgo/accept2.png', grayscale=True)
        cs_ok = pyautogui.locateCenterOnScreen('img/csgo/ok.png', grayscale=True)

        valor = None

        if cs_accept != None:
            valor = cs_accept
        elif cs_accept2 != None:
            valor = cs_accept2

        if valor != None:
            pyautogui.click(valor)
            print('CS:GP - Partida encontrada')
            sleep(action_time)
        elif cs_ok != None:
            pyautogui.click(cs_ok)
            print('CS:GP - Entrando na fila')
            pyautogui.moveRel(None,-100)
            sleep(action_time)
            select('csgo')
        else:
            print('CS:GO - Na fila')
            sleep(action_time)
            select('csgo')

select('find_match')