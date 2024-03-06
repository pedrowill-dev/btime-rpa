import time
from enum import Enum
from typing import List
from app.services.browser.browser_interface import BrowserInterface
from app.decorator.wrapper_log import wrapper_log
from urllib.request import urlopen, Request, HTTPError
from pydantic import BaseModel


class Month(Enum):

    Janeiro = 1
    Fevereiro = 2
    Março = 3
    Abril = 4
    Maio = 5
    Junho = 6
    Julho = 7
    Agosto = 8
    Setembro = 9
    Outubro = 10
    Novembro = 11
    Dezembro = 12

class NewsItem(BaseModel):
    date: str
    title: str
    description: str

class Extractor:


    def __init__(self, month: Month, year: int, pageStart: int, pageEnd: int, browser: BrowserInterface):
        self.month = month
        self.year = year
        self.pageStart = pageStart
        self.pageEnd = pageEnd 
        self.browser = browser
        self.BASE_HOST_GOV = "https://www.saopaulo.sp.gov.br/ultimas-noticias/"


    @wrapper_log("ABRIR NAVEGADOR")
    def openGovNews(self):

        responsePage = urlopen(Request(self.BASE_HOST_GOV))
        
        if responsePage.getcode() != 200:
            raise HTTPError(f"REQUISIÇÃO FALHOU -> STATUSCODE -> [{responsePage.getcode()}] - LINE ERROR [22]")
        
        self.browser.openPage(self.BASE_HOST_GOV)

    @wrapper_log("FILTRAR NOTICIA")
    def openGovNewsFiltered(self, page):

        month = Month[self.month].value
        
        mode = f'?categorias[]=spnoticias&mes={month}&ano={self.year}'

        if page > 1:
            mode = f'page/{page}/?categorias[]=spnoticias&mes={month}&ano={self.year}'


        hostNews = self.BASE_HOST_GOV + mode
        
        responsePage = urlopen(Request(hostNews))

        
        if responsePage.getcode() != 200:
            raise HTTPError(f"REQUISIÇÃO FALHOU -> STATUSCODE -> [{responsePage.getcode()}] - LINE ERROR [35]")
            
        
        self.browser.openPage(hostNews)

    @wrapper_log('EXTRAIR TITULO NOTICIA')

    def extractNews(self) -> List[NewsItem]:
        templateNews = ["date", "title", "description"]
        dataExtractNews = []

        documentsCategoryInformations = self.browser.extractByClass('category-infos')
        
        if not documentsCategoryInformations:
            raise ValueError('A lista está vazia e não possui noticias para serem tratadas')

        for news in documentsCategoryInformations:
            # Aguarde um curto período de tempo antes de tentar interagir com o elemento novamente
            time.sleep(1)

            # Tente interagir com o elemento novamente
            try:
                newsList = news.text.split('\n')
                news_dict = dict(zip(templateNews, newsList))
                dataExtractNews.append(NewsItem(**news_dict))
            except Exception as e:
                print(f"Erro ao extrair notícia: {e}")

        return dataExtractNews

    