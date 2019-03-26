# -*- coding: utf-8 -*-
# import sys
import requests
from bs4 import BeautifulSoup
import mechanize

def conectarWebApp(palabra2):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open('https://aulex.org/es-nah/') #Abrir Webpage
    br.select_form(nr=0)
    br.form['busca'] = str(palabra2) #Llenar el formulario
    response = br.submit()
    html2 = response.read()
    soup = BeautifulSoup(html2, 'html.parser')
    print("\n""-----------------RESULTADOS-------------------")
    for link in soup.find_all("p"): #Extraer los resultados con ciclo for
        print(link.text)
    print("-----------------RESULTADOS-------------------")

