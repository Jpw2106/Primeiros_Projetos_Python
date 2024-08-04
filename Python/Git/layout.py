from PySimpleGUI import PySimpleGUI as sg


# layout

sg.theme('Reddit')
layout = [

    [sg.Text('Usuário'), sg.Input(key='usuario')],
    # passworrd_char, ele não mostra a senha
    [sg.Text('Senha'), sg.Input(key='password', password_char='*')],
    [sg.Checkbox('Salvar o Login')],
    [sg.Button('Entrar')]

]

# Janela

janela = sg.Window('Tela de Login', layout)

# Ler os Eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'joao' and valores['senha'] == '123456':
            print("seja bem vindo")
