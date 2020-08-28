from getpass import getpass
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    visibility_of_element_located
)


class Acess:

    def __init__(self, browser):
        #acessa a página de login do sigaa
        browser.get("https://sigaa.ufpb.br/sigaa/logon.jsf")

    def login(self):
        try:
            #Espera o elemento está carregado para abrir e o coloca na variável e digita no elemento caixa do login
            form_login = WebDriverWait(browser, 10).until(presence_of_element_located((By.ID, "form:login")))
            form_login.send_keys(input("Usuário: "))
            #acha a caixa de senha e envia a senha digitada
            form_senha = browser.find_element(By.ID, "form:senha")
            form_senha.send_keys(getpass(prompt="Senha: ", stream=None))
            #acha o botão e clica para entrar no sigaa
            button = browser.find_element(By.ID, "form:entrar")
            button.click()
        except:
            print("Um erro ocorreu ao carregar a página, tente novamente mais tarde.")

    def questionario(self):
        try:
            #resgata o texto do modal indicando a existência de questionários não respondidos
            head = WebDriverWait(browser, 10).until(visibility_of_element_located((By.ID, "modalTitle")))
            print(head.text)
            print("Se desejar respondê-los entre no site do sigaa!")
            #acha o botão responsável pelo fechamento do modal e clica.
            button_x = browser.find_element_by_css_selector(".close")
            button_x.click()
        except:
            #se não existir questionários não faz nada.
            pass

    def identifica(self):
        #acha o nome do usuário e o seu curso
        usuario = browser.find_element_by_css_selector(".painel-usuario-identificacao")
        texto = usuario.text.split('\n')
        return texto

if __name__ == '__main__':

    #define o Firefox como browser
    browser = Firefox()

    #instância acesso
    acesso = Acess(browser)

    #realiza o login no sigaa
    acesso.login()

    #salva nome, curso e semestre atual do candidato
    dados_user = acesso.identifica()
    nome = dados_user[0][5:]
    curso = dados_user[1]
    semestre = dados_user[2]

    #Boas vindas e introdução do programa
    print(f"Bem vindo, {nome}\n")
    print("Esse programa é desenvolvido como forma de aprendizado,\n sugestões de melhorias serão sempre bem vindas")

    #verifica a existência de questionários, mostra na tela para o usuário a ocorrência e fecha a notificação
    acesso.questionario()

    
