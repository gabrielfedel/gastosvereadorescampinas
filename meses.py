#Puxar todas os meses e organiza-los
from lxml import html
import requests


#puxando todos os meses disponíveis
page = requests.get('http://www.campinas.sp.leg.br/transparencia/meses/')


tree = html.fromstring(page.text)

#todos os links disponíveis para cada mes
meses = tree.xpath('//dl//dt//span//a//@href')