"""
    Auto accept for League of Legends PT-BR
    Criado por Sagos dia 01/01/2019
"""

import pyautogui
from time import sleep


action_time = 0.8

def select(status):
    if status == 'play':
        button_play = pyautogui.locateCenterOnScreen('button_play.png', grayscale=True)

        if button_play != None:
            pyautogui.click(button_play)
            print('Botao encontrado: Jogar')
            sleep(action_time)
            select('queue_normal')
        else:
            button_play_inactive = pyautogui.locateCenterOnScreen('button_play_inactive.png', grayscale=True)
            if button_play_inactive != None:
                print('Botao jogar inativo')
                select('begin')
            else:
                print('Procurando botao: Jogar')
                sleep(action_time)
                select('play')

    if status == 'begin':
        button_begin = pyautogui.locateCenterOnScreen('button_begin.png', grayscale=True)

        if button_begin != None:
            pyautogui.click(button_begin)
            print('Botao encontrado: Inicio')
            sleep(action_time)
            select('play')
        else:
            print('Procurando botao: Inicio')
            sleep(action_time)
            select('begin')

    if status == 'queue_normal':
        queue_normal = pyautogui.locateCenterOnScreen('queue_normal.png', grayscale=True)

        if queue_normal != None:
            pyautogui.click(queue_normal)
            print('Botao encontrado: Escolha as cegas')
            sleep(action_time)
            select('button_confirm')
        else:
            print('Procurando botao: Escolha as cegas')
            sleep(action_time)
            select('queue_normal')

    if status == 'button_confirm':
        button_confirm = pyautogui.locateCenterOnScreen('button_confirm.png', grayscale=True)

        if button_confirm != None:
            pyautogui.click(button_confirm)
            pyautogui.moveRel(None,-100)
            print('Botao encontrado: Confirmar')
            sleep(action_time)
            select('find_match')
        else:
            print('Procurando botao: Confirmar')
            sleep(action_time)
            select('button_confirm')

    if status == 'find_match':
        find_match = pyautogui.locateCenterOnScreen('find_match.png', grayscale=True)

        if find_match != None:
            pyautogui.click(find_match)
            print('Entrou na fila: Escolha as cegas')
            sleep(action_time)
            select('accept')
        else:
            print('Procurando botao: Encontrar partida')
            sleep(action_time)
            select('find_match')

    if status == 'accept':
        button_accept = pyautogui.locateCenterOnScreen('button_accept.png', grayscale=True)

        if button_accept != None:
            pyautogui.click(button_accept)
            print('Partida aceita')
            sleep(action_time)
            select('say_lane')
        else:
            in_queue = pyautogui.locateCenterOnScreen('in_queue.png', grayscale=True)

            if in_queue != None:
                print('Na fila')
                sleep(action_time)
                select('accept')
            else:
                print('Jogador saiu da fila')
                sleep(action_time)
                select('find_match')

select('play')