from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Classe


class Follow:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # quem sera o primeiro insta a ser aberto
        self.userInitial = ''

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

        driver.get('https://instagram.com/' + self.userInitial)
        time.sleep(2)

        driver.find_element_by_xpath(
            '//a[@href="/' + self.userInitial + '/followers/"]').click()

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


# variavel com usuario + senha do instagram
insta = Follow('aquino.py', '******')
time.sleep(3)

# 1 Passo - fazer login
insta.login()

# 2 Passo Buscar seguidores
insta.buscar_seguidores(5)

# Segue os seguidores dos influencers
insta.Seguir_usuarios(10)
