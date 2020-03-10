#-*- encoding:utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import WebDriverException
;3from selenium.webdriver.chrome.options import Options
from mod_auxiliar.filtro import usuarios_coletados
from config import Config as mensagem_escrita
from time import sleep
import csv
import re


class PilotoFacebookEnv:

    standard = "https://pt-br.facebook.com"
    perfis_links = [ ]

    def __init__(self,email,senha):
        self.email = email
        self.senha = senha
        self.loginFacebook(self.email, self.senha)

    def input_cmd_lines(self, cmd):
        return str(input(cmd))

    def _driver():
       # options = Options()
       # options.headless = False
        #chrome_options = webdriver.ChromeOptions()
        #prefs = {"profile.default_content_setting_values.notifications": 2}
        #chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=r'mod_auxiliar/___>aquivo___<')

        return driver
    _driver = staticmethod(_driver)

    def code_html(self, param, elem):
        return elem.find_element_by_id(str(param)).get_attribute("outerHTML")

    def filtro(self, item):
        return re.compile(str(item))

    def loginFacebook(self, user, passwd):

        try:
  
            pagLogin = self._driver()
            pagLogin.get(self.standard)
            pagLogin.find_element_by_id("email").send_keys(user)
            pagLogin.find_element_by_id('pass').send_keys(passwd)
            pagLogin.find_element_by_id('loginbutton').click()
            self.enviarmsgparticipante(pagLogin)
        except WebDriverException as erroPaginaLogin:
            print("Erro, verifique a conexao")



    def enviarmsgparticipante(self, driver_msg):
        print('-' * 50)
        message_all = mensagem_escrita(open("mensagem.txt"))
        mensagem_mass = message_all["msg"]

        usuarios_coletados.reverse()
        subscrevendo = []
        for usuario_aba1 in range(0, len(usuarios_coletados)):
            try:
                messages = 'https://www.facebook.com/messages/t/{}'.format(usuarios_coletados[usuario_aba1])

                if usuario_aba1 <= 10:
                    driver_msg.get(messages)
                    sleep(3)
                    print('[ +  ] - carregado')
                    _cod_msg = driver_msg.find_element_by_class_name('_5rpb').get_attribute("outerHTML")
                    buscar_class = re.compile(r'<div data-offset-key="(.*?)"')
                    class_cht = buscar_class.search(_cod_msg).group(1)
                    setHTML = 'div[data-offset-key="{}"]'.format(class_cht)
                    print('[ ok ] - preparando envio')
                    msgF = driver_msg.find_element_by_css_selector(setHTML).send_keys(str(mensagem_mass+"\n"))
                    sleep(2)
                    print('[ up ] enviada')
                    print('-' * 50)
                elif usuario_aba1 == 10:
                    driver_msg.close()
                    print("Atualizando lista")
                    csvSub = open("perfis_facebook.csv")
                    leitura = csv.reader(csvSub)
                    for row in leitura:
                        if not (leitura.line_num) in list(range(1, 10)):
                            subscrevendo = subscrevendo + [row[0]]

            except Exception as error:
               # print('Erro inesperado pfv comunicar ao dev', error)
                continue
        print("Arquivo atualizado")
        f = open("perfis_facebook.csv", "w", encoding='UTF-8')
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        for i in subscrevendo:
            writer.writerow([i])







if __name__ == '__main__':
    #-------------------------------------------------------adicionar contas
    senha = "ooh"  # <=======================  senha Padrao

    lista_emails = ["emails"] # <============adicionar emails


    for todos_emails in lista_emails:
        PilotoFacebookEnv(todos_emails, senha)



