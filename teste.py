from openpyxl import*
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())

#configurando o navegador
navegador = webdriver.Chrome(service=service)

url = 'http://127.0.0.1:5500/index.html'
navegador.get(url=url)

workbook = load_workbook('pessoas.xlsx')
pessoas = workbook['Planilha1']



for pessoa in pessoas.iter_rows(min_row=2):
    nome = pessoa[0].value
    sobrenome = pessoa[1].value
    cpf = pessoa[2].value
    idade = pessoa[3].value
    
    time.sleep(2)
    navegador.find_element('xpath','/html/body/div/form/div[1]/div[1]/input').send_keys(nome)

    time.sleep(0.6)
    navegador.find_element('xpath','/html/body/div/form/div[1]/div[2]/input').send_keys(sobrenome)

    time.sleep(0.6)
    navegador.find_element('xpath','/html/body/div/form/div[1]/div[3]/input').send_keys(cpf)

    time.sleep(0.6)
    navegador.find_element('xpath','/html/body/div/form/div[1]/div[4]/input').send_keys(idade)

    time.sleep(0.6)
    navegador.find_element('xpath','/html/body/div/form/div[2]/input').click() 

    time.sleep(2)   










