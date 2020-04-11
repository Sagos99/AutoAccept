'''
    Segunda tentativa do script de auto accept para o LoL
    Criado dia 26/12/2019
    Funcionando na versão: 10.6
'''

from multiprocessing import Process
from time import sleep
import pyautogui

try:
    import config
except:
    print("Erro ao importar suas configurações, por favor revise-o")
    exit()

try:
    lane = config.lane.lower()
    lane = lane.replace(' ','')
    lane = lane.split('/')
except:
    lane = None

try:
    champ = config.champ.lower()
    ban = config.ban.lower()
    mode = config.mode
except:
    champ,ban,mode = None,None,None


path = 'img/'

blindly = [150,517]
alternate = [149,549]
solo_duo = [180,581]
flex = [150,610]
button_confirm = [573,690]
search_champ = [843,107]
select_champ = [423,173]


def click_mouse(x,y):
    pyautogui.click(x, y)



def create_match(x,y):
    click_mouse(x,y)
    sleep(1.5)

    if mode == 1:
        click_mouse(blindly[0],blindly[1])
    elif mode == 2:
        click_mouse(alternate[0],alternate[1])
    elif mode == 3:
        click_mouse(solo_duo[0],solo_duo[1])
    elif mode == 4:
        click_mouse(flex[0],flex[1])

    sleep(0.5)
    click_mouse(button_confirm[0],button_confirm[1])

    if mode == 1:
        sleep(3)
        pyautogui.click()
    elif mode >= 2 and mode <= 4:
        sleep(3)
        select_lane()
    
    return True



def select_lane():
    pyautogui.moveTo(520,482)
    pyautogui.mouseDown(button='left')
    
    if len(lane) == 1:
        if lane[0] != 'preencher':
            if lane[0] == 'top':
                pyautogui.moveRel(-100,0)
            elif lane[0] == 'mid':
                pyautogui.moveRel(0,-100)
            elif lane[0] == 'jg':
                pyautogui.moveRel(-100,-100)
            elif lane[0] == 'adc':
                pyautogui.moveRel(+100,-100)
            elif lane[0] == 'sup':
                pyautogui.moveRel(+100,0)
                
            pyautogui.mouseUp(button='left')

            pyautogui.moveTo(613,482)
            pyautogui.mouseDown(button='left')
            pyautogui.moveRel(0,+100)
            pyautogui.mouseUp(button='left')
        else:
            pyautogui.moveRel(0,+100)
            pyautogui.mouseUp(button='left')
    elif len(lane) == 2:
        if lane[0] == 'top':
            pyautogui.moveRel(-100,0)
        elif lane[0] == 'mid':
            pyautogui.moveRel(0,-100)
        elif lane[0] == 'jg':
            pyautogui.moveRel(-100,-100)
        elif lane[0] == 'adc':
            pyautogui.moveRel(+100,-100)
        elif lane[0] == 'sup':
            pyautogui.moveRel(+100,0)
        
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(613,482)
        pyautogui.mouseDown(button='left')

        if lane[0] != lane[1]:
            if lane[1] == 'top':
                pyautogui.moveRel(-100,0)
            elif lane[1] == 'mid':
                pyautogui.moveRel(0,-100)
            elif lane[1] == 'jg':
                pyautogui.moveRel(-100,-100)
            elif lane[1] == 'adc':
                pyautogui.moveRel(+100,-100)
            elif lane[1] == 'sup':
                pyautogui.moveRel(+100,0)
            elif lane[1] == 'preencher':
                pyautogui.moveRel(0,+100)
        else:
            pyautogui.moveRel(0,+100)

        pyautogui.mouseUp(button='left')

    sleep(1.5)
    click_mouse(button_confirm[0],button_confirm[1])
    watch_button_accept()


def watch_button_play():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(path+'button_play.png', grayscale=True)
        except:
            x, y = None,None

        if not x and not y:
            try:
                x, y = pyautogui.locateCenterOnScreen(path+'button_play2.png', grayscale=True)
            except:
                x, y = None,None

        if not x and not y:
            try:
                x, y = pyautogui.locateCenterOnScreen(path+'button_play3.png', grayscale=True)
            except:
                x, y = None,None

        if x and y:
            print('Criando nova partida')
            create_match(x,y)

        sleep(1)

    

def watch_button_accept():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(path+'button_accept.png', grayscale=True)
        except:
            x, y = None,None

        if not x and not y:
            try:
                x, y = pyautogui.locateCenterOnScreen(path+'button_accept2.png', grayscale=True)
            except:
                x, y = None,None

        if x and y:
            print('Partida encontrada!')
            click_mouse(x, y)
            pyautogui.moveRel(0,-100)
        
        sleep(1)



def watch_button_ban():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(path+'button_ban.png', grayscale=True)
        except:
            x, y = None,None

        if x and y:
            click_mouse(search_champ[0], search_champ[1])
            pyautogui.write(ban)
            sleep(1.5)
            click_mouse(select_champ[0], select_champ[1])
            sleep(1.5)
            click_mouse(x, y)
            pyautogui.moveRel(+100,0)

        sleep(1)



def watch_button_confirm():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen(path+'button_confirm.png', grayscale=True)
        except:
            x, y = None,None

        if x and y:
            click_mouse(search_champ[0], search_champ[1])
            pyautogui.write(champ)
            sleep(1.5)
            click_mouse(select_champ[0], select_champ[1])
            sleep(1.5)
            click_mouse(x, y)
            pyautogui.moveRel(+100,0)

        sleep(1)



if __name__ == "__main__":
    tWatch_button_play = Process(target=watch_button_play)
    tWatch_button_accept = Process(target=watch_button_accept)
    tWatch_button_ban = Process(target=watch_button_ban)
    tWatch_button_confirm = Process(target=watch_button_confirm)

    tWatch_button_play.start()
    tWatch_button_accept.start()
    tWatch_button_ban.start()
    tWatch_button_confirm.start()

    tWatch_button_play.join()
    tWatch_button_accept.join()
    tWatch_button_ban.join()
    tWatch_button_confirm.join()