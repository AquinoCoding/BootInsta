import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Element


def painelPrincipal():

    bottom = [
        [sg.Button('Seguidores', size=(20,3), key='_Follow_'), sg.B('Curtidas & Comentários', size=(20,3), key='_Like_')],
    ]

    layout = [
        [sg.Text('InstaBoot', font=50)],
        [sg.Frame('', bottom, element_justification='center')],
    ]

    Janela = sg.Window('Seleção', layout, element_justification='center', size=(450, 250))

    events, values = Janela.Read()

    if events == sg.WINDOW_CLOSED:
        exit()
    
    elif events == '_Like_':
        Janela.close()
        painelLoginCC()
    
    elif events == '_Follow_':
        Janela.close()
        painelLoginFF()
        
def painelLoginFF():
    dados = [
        [sg.Text('Login: ', size=(7,0)), sg.Input(size=(15, 0), key='_username_')],
        [sg.T('Senha: ', size=(7,0)), sg.Input(size=(15, 0),  password_char='*' ,key='_pass_')],
        [sg.Checkbox('Google Chrome', key='_chrome_'), sg.Checkbox('Firefox', key='_firefox_')],
        [sg.Text('Informe um @: ', size=(7,0), justification='left'), sg.Input(size=(15, 0), key='_initFollow_', justification='right')],
    ]

    botoes = [
        
        [sg.B('Entrar', key='_entrar_')]
    ]

    layout = [
        [sg.Fr('', dados)],
        [sg.Frame('', botoes)]
    ]

    Janela = sg.Window('Tela de Login', layout,
                           element_justification='center', size=(400, 300))

    events, values = Janela.Read()

    _username_ = values['_username_']
    _pass_ = values['_pass_']
    _firefox_ = values['_firefox_']
    _chrome_ = values['_chrome_']
    _initFollow_ = values['_initFollow_']
    
    if events == sg.WINDOW_CLOSED:
        exit()
    
    if _chrome_ == True and _firefox_ == True:

        layout= [
            [sg.T('Informe apenas um Navegador')],
            [sg.B('Firefox', key='_firefox_'), sg.B('Google Chrome', key='_Chrome_')]
        ]

        Janela_pop = sg.Window('Seleção de Navegador', layout,
                           element_justification='center', size=(250, 100))

        events, values = Janela_pop.Read()

        if events == sg.WINDOW_CLOSED:
            exit()

        if events == '_Chrome_':
            navegador = 1
            Janela.Close()
            Janela_pop.Close()
            initboot(_username_, _pass_, navegador, _initFollow_)

        if events == '_firefox_':
            navegador = 2
            Janela.Close()
            Janela_pop.Close()
            initboot(_username_, _pass_, navegador, _initFollow_)

    else:
        if _chrome_ == True:
            navegador = 1
            if events == '_entrar_':
                Janela.Close()
                initboot(_username_, _pass_, navegador, _initFollow_)

        if _firefox_ == True:
            navegador = 2
            if events == '_entrar_':
                Janela.Close()
                initboot(_username_, _pass_, navegador, _initFollow_)              

def painelLoginCC():
    
    dados = [
        [sg.Text('Login: ', size=(7,0)), sg.Input(size=(15, 0), key='_username_')],
        [sg.T('Senha: ', size=(7,0)), sg.Input(size=(15, 0),  password_char='*' ,key='_pass_')],
        [sg.T('HashTag: ', size=(7,0)), sg.Input(size=(15, 0), key='_tag_')],
        [sg.Checkbox('Google Chrome', key='_chrome_'), sg.Checkbox('Firefox', key='_firefox_')],
        [sg.Text('Informe uma lista de comentários:')],
        [sg.InputText(size=(28,), key='_ListComent_')],
    ]

    botoes = [
        [sg.B('Entrar', key='_entrar_')]
    ]

    layout = [
        [sg.Fr('', dados)],
        [sg.Frame('', botoes)]
    ]

    Janela = sg.Window('Tela de Login', layout,
                           element_justification='center', size=(400, 300))

    events, values = Janela.Read()

    _username_ = values['_username_']
    _pass_ = values['_pass_']
    _tag_ = values['_tag_']
    _firefox_ = values['_firefox_']
    _chrome_ = values['_chrome_']
    _ListComent_ = values['_ListComent_']

    _ListComent_ = _ListComent_.split(',')
    
    if events == sg.WINDOW_CLOSED:
        exit()
    
    if _chrome_ == True and _firefox_ == True:

        layout= [
            [sg.T('Informe apenas um Navegador')],
            [sg.B('Firefox', key='_firefox_'), sg.B('Google Chrome', key='_Chrome_')]
        ]

        Janela_pop = sg.Window('Seleção de Navegador', layout,
                           element_justification='center', size=(250, 100))

        events, values = Janela_pop.Read()

        if events == sg.WINDOW_CLOSED:
            exit()

        if events == '_Chrome_':
            navegador = 1
            Janela.Close()
            Janela_pop.Close()
            initboot(_username_, _pass_, _tag_, navegador, _ListComent_)

        if events == '_firefox_':
            navegador = 2
            Janela.Close()
            Janela_pop.Close()
            initboot(_username_, _pass_, _tag_, navegador, _ListComent_)

    else:
        if _chrome_ == True:
            navegador = 1
            if events == '_entrar_':
                Janela.Close()
                initboot(_username_, _pass_, _tag_, navegador, _ListComent_)

        if _firefox_ == True:
            navegador = 2
            if events == '_entrar_':
                Janela.Close()
                initboot(_username_, _pass_, _tag_, navegador, _ListComent_)
                 
painelPrincipal()
