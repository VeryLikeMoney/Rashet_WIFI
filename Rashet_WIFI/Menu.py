import Main_count
import PySimpleGUI as sg
sg.theme('DarkAmber')
n,m=35,1 # Размер Text
n_inp,m_inp=10,1 # Полей ввода
layout = [
    [sg.Image(source='System_Comunication.png',data='Raw',size=(700,250))],

    [sg.Text('Введите мощность передачика(дБм/дБ)',size=(n,m)),
    sg.Input(k='transmitter_power',size=(n_inp,m_inp)),
    sg.Text('Введите чувствительность(дБм/дБ)',size=(n,m)), 
    sg.Input(k='sensitivity',size=(n_inp,m_inp))],

    [sg.Text('Введите рабочую частоту\n(Герц с любой приставкой)',size=(n,m)),
    sg.Input(k='frequency',size=(n_inp,m_inp)),
    sg.Text('Введите запас в энергетике радиосвязи\nSOM (дБм/дБ)',size=(n,m)), 
    sg.Input(k='SOM',size=(n_inp,m_inp))],

    [sg.Text('Введите усиление приемника(дБм/дБ)',size=(n,m)),
    sg.Input(k='receiver_gain',size=(n_inp,m_inp)),
    sg.Text('Введите усиление передачика(дБм/дБ)',size=(n,m)), 
    sg.Input(k='transmitter_gain',size=(n_inp,m_inp))],

    [sg.Text('Введите длину кабеля до приемника(метр)',size=(n,m)),
    sg.Input(k='losses_to_receiver',size=(n_inp,m_inp)),
    sg.Text('Введите длину кабеля до передачика(метр)',size=(n,m)), 
    sg.Input(k='losses_to_transmitter',size=(n_inp,m_inp))],

    [sg.Button('Расчёт')],
    [sg.Text('Полученная растояние',size=(n,1)),sg.Text(k='-OUT-',size=(25,1)),sg.Text('метров',size=(5,1))]
]
window = sg.Window('Программа для расчет дальности работы беспроводного канала связи WiFi', layout)
while True:                             # The Event Loop
    event, values = window.read()
    if event=="Расчёт":
        dec=Main_count.leng_out(values)
        window['-OUT-'].update(dec)
    if event in (None, 'Exit', 'Cancel'):
        break