

bt_novamsg = '//*[@id="side"]/header/div[2]/div/span/div[2]/div/span'
campo_procura = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]'
primeiro_contato = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span/span'
botao_enviar = '//*[@id="main"]/footer/div[1]/div[3]'
msg_campo = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

from selenium import webdriver
from time import sleep

chrome_path= 'C:\\Users\\caioa\\Desktop\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(chrome_path)
driver.get('https://web.whatsapp.com/')

nova_msg = driver.find_element_by_xpath(bt_novamsg)
nova_msg.click()

proc_camp = driver.find_element_by_xpath(campo_procura)
proc_camp.click()
proc_camp.send_keys( 'Vitor Almeida' )
proc_contato = driver.find_element_by_xpath(primeiro_contato)
proc_contato.click()

proc_contato = driver.find_element_by_xpath(msg_campo)
proc_contato.click()
proc_contato.send_keys('Isso é um teste')


send = driver.find_element_by_xpath(botao_enviar)
send.click()
