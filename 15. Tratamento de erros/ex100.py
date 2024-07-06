#Faça um programa que verifique se o site pudim está acessível ou não

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está aceesível no momento')
else:
    print('O site pudim está aceesível no momento')

    
