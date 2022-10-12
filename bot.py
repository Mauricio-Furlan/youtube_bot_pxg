from time import sleep
import winsound
import pyautogui
import keyboard
import button


def atack_scizor():
  keyboard.press(button.key['F3'])
  keyboard.press(button.key['F4'])
  keyboard.press(button.key['F6'])

def atack_nine():
  keyboard.press(button.key['F4'])
  keyboard.press(button.key['F5'])
  keyboard.press(button.key['F6'])
  keyboard.press(button.key['F8'])
  keyboard.press(button.key['F9'])

def pesca():
  keyboard.press(button.key['CAPS'])

def saque():
  keyboard.press(button.key['F12'])

def pokebola(pokemon):
  keyboard.press(button.key['NUNLOCK'])
  position_x, position_y = pyautogui.center(pokemon)
  pyautogui.moveTo(position_x, position_y, 0.5)
  sleep(1)
  pyautogui.click()

while True:
  bolhas = pyautogui.locateOnScreen("bolhas.PNG", confidence=0.75, region=(907, 204, 102, 100))
  print(bolhas)
  if bolhas != None:
    pesca()

    atack_scizor()
    sleep(2)
    saque()

    x_bolhas, y_bolhas = pyautogui.center(bolhas)
    pyautogui.moveTo(x_bolhas, y_bolhas, 0.5)
    pesca()
    pyautogui.click()
  tenta = pyautogui.locateOnScreen("tenta.PNG", confidence=0.75)
  if tenta != None:
    pokebola(tenta)
    winsound.Beep(440, 500)