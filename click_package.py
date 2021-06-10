import pyautogui as pag
import pywinauto    #pip install pywinauto
import pygetwindow as gw
#집 window : 622, 1040  click : 50 , 951

#학원 window: 796, 1000 click : 64, 893
def click():
    win = gw.getWindowsWithTitle('Telegram')[0] # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
    app =pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate() #윈도우 활성화
    app.move_window(x=0, y=0, width=622, height=1040, repaint=True)
    pag.click(win.left + 50, win.top + 951) # 해당 윈도우의 left ,top 클릭