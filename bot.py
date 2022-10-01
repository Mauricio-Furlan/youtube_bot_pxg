import pyautogui

while True:
  bolhas = pyautogui.locateOnScreen("bolhas.PNG", confidence=0.75)
  print(bolhas)
  if bolhas != None:
    varinha = pyautogui.locateOnScreen("varinha.PNG", confidence=0.75)
    x_varinha, y_varinha = pyautogui.center(varinha)
    pyautogui.moveTo(x_varinha, y_varinha, 1)
    pyautogui.click()

    atack_t4 = pyautogui.locateOnScreen("atack_t4.PNG", confidence=0.75)
    if atack_t4 != None:
      x_atack, y_atack = pyautogui.center(atack_t4)
      pyautogui.moveTo(x_atack, y_atack, 1)
      pyautogui.click()

    pyautogui.moveTo(x_varinha, y_varinha, 1)
    pyautogui.click()

    x_bolhas, y_bolhas = pyautogui.center(bolhas)
    pyautogui.moveTo(x_bolhas, y_bolhas, 0.5)
    pyautogui.click()
