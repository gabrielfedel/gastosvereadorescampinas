from lxml import html
import requests


#puxando a página do mẽs de janeiro
page = requests.get('http://www.campinas.sp.leg.br/transparencia/meses/janeiro-2015/')

tree = html.fromstring(page.text)

#pegando os links de todos os vereadores
vereadores = tree.xpath('//dl//dt//span//a//@href')
