# coding: utf-8 #

__author__ = 'Javaly'
__contact__ = ''
__version__ = ''

from requests import get
from termcolor import colored
from json import loads, dumps

class FiveMInfo(object):
    def __init__(self, address, port=30120):
        self.address = address
        self.port = port
    
    @staticmethod
    def Screenfetch():
        return '''   _        __       __ _                     
 (_)      / _|     / _(_)                    
  _ _ __ | |_ ___ | |_ ___   _____ _ __ ___  
 | | '_ \|  _/ _ \|  _| \ \ / / _ \ '_ ` _ \ 
 | | | | | || (_) | | | |\ V /  __/ | | | | |
 |_|_| |_|_| \___/|_| |_| \_/ \___|_| |_| |_|
                                              '''

    def GetDynamicResponse(self):
        try:
            return loads(get(f'http://{self.address}:{self.port}/dynamic.json').text)
        except Exception as err:
            print(err)
            exit(1)
    
    def GetPlayersResponse(self):
        try:
            return loads(get(f'http://{self.address}:{self.port}/players.json').text)
        except Exception as err:
            print(err)
            exit(1)
    
    def ShowServerInfo(self, response):
        print(colored(f" -Players: {response['clients']}", 'yellow'))
        print(colored(f' -Tipo de jogo: {response["gametype"]}', 'yellow'))
        print(colored(f' -Nome do host: {response["hostname"]}', 'yellow'))
        print(colored(f' -Nome do mapa: {response["mapname"]}', 'yellow'))
        print(colored(f' -Número máximo de players: {response["sv_maxclients"]}', 'yellow'))
    
    def SavePlayersInfo(self, response):
        for _json in response:
            with open(f'{_json["name"].split(" ")[0]}.json', 'w') as log:
                log.write(dumps(_json))
    
    def Run(self):
        self.ShowServerInfo(self.GetDynamicResponse())
        print(colored(' {*} Salvando lista dos Players online no momento...', 'green'))
        self.SavePlayersInfo(self.GetPlayersResponse())

if __name__ == '__main__':
    print(colored(FiveMInfo.Screenfetch(), 'red'))
    adress = str(input(colored('Endereço: ', 'green')))
    fivem = FiveMInfo(adress, 30120)
    fivem.Run()