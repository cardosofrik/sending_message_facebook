#-*- encoding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
#rom selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import re


class PilotoFacebook:

    standard = "https://pt-br.facebook.com"
    perfis_links = [ ]

    def input_cmd_lines(self, cmd):
        return str(input(cmd))


    def _driver():
       # options = Options()
       # options.add_argument('profile.default_content_setting_values.notifications')
        driver = webdriver.Chrome(executable_path=r'mod_auxiliar/___>aquivo___<')
        return driver
    _driver = staticmethod(_driver)

    def code_html(self, param, elem):
        return elem.find_element_by_id(str(param)).get_attribute("outerHTML")

    def filtro(self, item):
        return re.compile(str(item))

    def loginFacebook(self, user, passwd):

        try:
            pagLogin = PilotoFacebook()._driver()
            pagLogin.get(self.standard)
            pagLogin.find_element_by_id("email").send_keys(user)
            pagLogin.find_element_by_id('pass').send_keys(passwd)
            pagLogin.find_element_by_id('loginbutton').click()
            self.extract_users(pagLogin)
        except WebDriverException as erroPaginaLogin:
            print("Erro, verifique a conexao")

    def extract_users(self, usr):

        f = open("perfis_facebook.csv", "w", encoding='UTF-8')
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        group = self.input_cmd_lines("group@URL_GRUPO:~#  ")
        usr.get(str(group[0:len(group)-1])+"/members/")
        perfil = usr.find_element_by_tag_name('html')
        for quantidade_paginas in range(1,80):
            perfil.send_keys(Keys.END)
            sleep(1)
        _code_html_user = self.code_html(param='mainContainer', elem=usr)
        pe = self.filtro('<div class="_60ri">(.*?)</div>')
        for i, s in enumerate(pe.findall(_code_html_user)):
            perfilF1 =self.filtro('href="(.*?)"')
            for ii in perfilF1.findall(string=s):
                self.perfis_links = self.perfis_links + [ii]
        print("Usuarios coletado ")
        print("-"*50)
        for perfil_usuario in self.perfis_links:
            writer.writerow([perfil_usuario])
            print("usuario coletado =: %s" % perfil_usuario)
        print("-" * 50)
        print("[ * ] Total de perfis coletados : %s" % len(self.perfis_links))

if __name__ == '__main__':

    user_email = "emails" #<===== insira e-mail ou numero
    senha = "oohh" # adicione a senha

    PilotoFacebook().loginFacebook(user_email, senha)







