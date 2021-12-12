import pyautogui
import PySimpleGUI as sg

sg.theme('DarkGray4')

layout = [
    [sg.Text('連打する回数'), sg.Text('  連打速度')],
    [sg.InputText(100, size=10), sg.Text('回'), sg.InputText(0.5, size=3), sg.Text('秒')],
    [sg.Text('画面左上にマウスを持っていくと強制終了')],
    [sg.Button('実行', size=(10,2)), sg.Button('キャンセル', size=(10,2))]
]

window = sg.Window('連打アプリ', layout)

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    while True: 
        event, values = window.read()
        if sg.WIN_CLOSED or event == 'キャンセル':
            break
        elif event == '実行':
            if values[0] == "":
                while True:
                    if event == 'Escape:27':
                        break
                    if event == "実行":
                        pyautogui.click()
                        pyautogui.PAUSE = 0.5
            else:
                pyautogui.click(clicks=int(values[0]), interval=float(values[1]))

    window.close()