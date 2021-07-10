from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint
import PySimpleGUI as sg


def painelPrincipal():

    bottom = [
        [sg.Button('Seguidores', size=(20,3), key='_Follow_'), sg.B('Curtidas & Comentários', size=(20,3), key='_Like_')],
    ]

    layout = [
        [sg.Text('InstaBoot', font=50)],
        [sg.Frame('', bottom, element_justification='center')],
    ]

    Janela = sg.Window('Seleção', layout, element_justification='center', size=(450, 150))

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
        [sg.Text('Login: ', size=(7,0)), sg.Input(size=(15, 0), key='_username_', justification='center')],
        [sg.T('Senha: ', size=(7,0)), sg.Input(size=(15, 0),  password_char='*' ,key='_pass_', justification='center')],
        [sg.Checkbox('Google Chrome', key='_chrome_'), sg.Checkbox('Firefox', key='_firefox_')],
        [sg.Text('Informe um @: ', size=(7,0)), sg.Input(size=(15, 0), key='_initFollow_', justification='center', )],
    ]

    botoes = [
        
        [sg.B('Entrar', key='_entrar_')]
    ]

    layout = [
        [sg.Fr('', dados)],
        [sg.Frame('', botoes)]
    ]

    Janela = sg.Window('Tela de Login', layout,
                           element_justification='center', size=(400, 200))

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
            initFF(_username_, _pass_, navegador, _initFollow_)

        if events == '_firefox_':
            navegador = 2
            Janela.Close()
            Janela_pop.Close()
            initFF(_username_, _pass_, navegador, _initFollow_)

    else:
        if _chrome_ == True:
            navegador = 1
            if events == '_entrar_':
                Janela.Close()
                initFF(_username_, _pass_, navegador, _initFollow_)

        if _firefox_ == True:
            navegador = 2
            if events == '_entrar_':
                Janela.Close()
                initFF(_username_, _pass_, navegador, _initFollow_)              

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
                           element_justification='center', size=(400, 250))

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
            initCC(_username_, _pass_, _tag_, navegador, _ListComent_)

        if events == '_firefox_':
            navegador = 2
            Janela.Close()
            Janela_pop.Close()
            initCC(_username_, _pass_, _tag_, navegador, _ListComent_)

    else:
        if _chrome_ == True:
            navegador = 1
            if events == '_entrar_':
                Janela.Close()
                initCC(_username_, _pass_, _tag_, navegador, _ListComent_)

        if _firefox_ == True:
            navegador = 2
            if events == '_entrar_':
                Janela.Close()
                initCC(_username_, _pass_, _tag_, navegador, _ListComent_)

class Follow:
    def __init__(self, username, password, navegador, _initFollow_):
        self.username = username
        self.password = password
        self.navegador = navegador
        self._initFollow_ = _initFollow_

        print(username, password, navegador, _initFollow_)

        if navegador == 1:
            self.driver = webdriver.Chrome(
                executable_path=r".\geckodriver\chromedriver.exe")
        else:
            self.driver = webdriver.Firefox(
                executable_path=r".\geckodriver\geckodriver.exe")

    # A função irá nos conectar ao Instagram
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        # Encontre as caixas de e-mail e senha, insira nossas credenciais de login
        campo_usuario = driver.find_element_by_name(
            'username').send_keys(self.username)

        campo_password = driver.find_element_by_name(
            'password').send_keys(self.password)

        # Aguarde 1 segundo e pressione ENTER
        time.sleep(1)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)

        # Aguarda 3 segundos do pos-login
        time.sleep(3)

    def buscar_seguidores(self, number_of_followers):
        driver = self.driver

        driver.get('https://instagram.com/' + self._initFollow_)
        time.sleep(2)

        driver.find_element_by_xpath(
            '//a[@href="/' + self._initFollow_ + '/followers/"]').click()

        time.sleep(1)

        popup = driver.find_element_by_class_name('isgrP')

        # lista de seguidores do influencer
        followers_array = []

        i = 1

        while len(followers_array) <= number_of_followers:
            driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight', popup)
            time.sleep(0.4)

            followers = driver.find_elements_by_class_name('FPmhX')

            for follower in followers:
                if follower not in followers_array:
                    followers_array.append(follower.text)

            i += 1

        self.followers = followers_array

    def Seguir_usuarios(self, number_to_follow):
        driver = self.driver
        cont = 1
        Stooped = False

        for follower in self.followers:
            driver.get('https://instagram.com/' + follower)
            time.sleep(2)
           

            if(len(driver.find_elements_by_xpath("//*[contains(text(), 'Esta conta é privada')]")) > 0):
                # Se eles forem privados, não podemos ver sua lista de seguidores, então pule-os
                continue

            driver.find_element_by_xpath(
                '//a[@href="/' + follower + '/followers/"]').click()
            time.sleep(3)

            follow = driver.find_elements_by_xpath(
                "//button[contains(text(), 'Seguir')]")

            i = 1

            if Stooped == True:
                break

            for follower in follow:
                if(i != 1):
                    driver.execute_script("arguments[0].click();", follower)
                    print(f"seguiu {cont}")
                    cont += 1
                    if cont == 45:
                        Stooped = True
                        break
                        
                    time.sleep(1)

                i += 1

            time.sleep(2)

# Boot de Curtidas e Comentários

class CurtComet:
  
    def __init__(self, username, password, tag_comment, navegador, ListComent):

        self.username = username
        self.password = password
        self.tag_comment = tag_comment
        self.navegador = navegador
        self.ListComent = ListComent

        print(username, password, tag_comment, navegador, ListComent)

        if navegador == 1: 
            self.driver = webdriver.Chrome(
                executable_path=r".\geckodriver\chromedriver.exe")
        else:
            self.driver = webdriver.Firefox(
                executable_path=r".\geckodriver\geckodriver.exe")


    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        # Entrada para conectar
        '''botao_login = driver.find_element_by_xpath("")
        botao_login.click()'''

        # Aplicar Username
        campo_usuario = driver.find_element_by_name(
            'username').send_keys(self.username)

        # Aplicar Password
        campo_password = driver.find_element_by_name(
            'password').send_keys(self.password)

        time.sleep(1)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        
        time.sleep(5)
        self.action_hastag(self.tag_comment, self.ListComent)

    def action_hastag(self, hashtag, ListComent):

        ListComent = self.ListComent
        driver = self.driver

        # Abri página com HashTags

        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)

        # Rolagem de página

        for i in range(1):
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(2)

        # Gravação de referencia da img

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))
        
        # Contadores curtidas em definição 0
        contador_curt = 0

        # Contadores Comentários em definição 0
        contador_coment = 0

        # loop de img
        for pic_hrefs in pic_hrefs:
            referencia = driver.get(pic_hrefs)

            # Execução de curtidas dentro do loop
            def curtida(self, contador_curt):

                driver = self.driver
                #contador_curt = self.contador_curt
                
                # Configuração para curtir conforme a lista de opção informada
                try:
                    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    print(f'Número de curtidas: {contador_curt}')
                    

                    driver.find_element_by_class_name('RxpZH').click()
                    time.sleep(3)

                # Caso erro do Loop|
                # Configurado para pular img com erro
                except Exception as e:
                    print('Erro ao curtir')
                    time.sleep(5)
            
            def coment(self, contador_coment):

                ListComent = self.ListComent
                driver = self.driver
                #self.contador_coment = contador_coment
        
                # Definidor de comentário a ser usado
                # Aqui se defini qual comentáio será utilizado conforme a lista informada
                len_valor  = len(ListComent) - 1 
                comentario = ListComent[randint(0,len_valor)]

                # Execução de comentários dentro do loop
                try:
                    driver.find_element_by_xpath("//textarea[@placeholder='Adicione um comentário...']").send_keys(comentario)
                    time.sleep(3)
                    print(f'Comentário de número: {contador_coment}, Comentou: {comentario}')

                # Caso erro do Loop|
                # Configurado para pular img com erro
                except Exception as e:
                    print('Erro ao comentar')
                    time.sleep(5)

            # Time de espera configurado para 18 segundos
            def _time_(self):

                driver = self.driver

                try:
                    driver.find_element_by_xpath("//button[@type='submit']").click()
                    print('Publicou\nEntrou em Time: 18seg')
                    time.sleep(18)

                # Caso erro do Loop|
                # Configurado para pular img com erro
                except Exception as e:
                    print('Erro ao mudar de postagem')
                    time.sleep(5)

            # Aqui se conta quantos Curtidas fora executados
            contador_curt += 1
            curtida(self, contador_curt)

            # Aqui se conta quantos comentários fora executados
            contador_coment += 1
            coment(self, contador_coment)

            _time_(self)
            if contador_coment == 17:
                break


        #print(f'Houve {contador_curt} curtidas\n Houve {contador_coment}')
        print('Encerrando...')

# Boot de Seguidores

def initCC(_username_, _pass_, _tag_, navegador, _ListComent_):

    print(_username_, _pass_, _tag_, navegador, _ListComent_)
    Inicie_boot = CurtComet(_username_, _pass_, _tag_, navegador, _ListComent_)
    Inicie_boot.login()

def initFF(_username_, _pass_, navegador, _initFollow_):
    
    print(_username_, _pass_, navegador, _initFollow_)
    # variavel com usuario + senha do instagram
    Inicie_boot = Follow(_username_, _pass_, navegador, _initFollow_)
    time.sleep(3)

    # 1 Passo - fazer login
    Inicie_boot.login()

    # 2 Passo Buscar seguidores
    Inicie_boot.buscar_seguidores(5)

    # Segue os seguidores dos influencers
    Inicie_boot.Seguir_usuarios(10)

painelPrincipal()







