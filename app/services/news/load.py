import csv
from typing import List
from pydantic import BaseModel

from app.decorator.wrapper_log import wrapper_log

class NewsItem(BaseModel):
    date: str
    title: str
    description: str

@wrapper_log("GERAR AS NOTICIAS EM CSV")
def write_to_csv(news_items_list: List[List[NewsItem]], file_path: str):
    with open(f'data/news/{file_path}', mode='w', newline='', encoding="utf8") as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho do CSV
        writer.writerow(['Date', 'Title', 'Description'])
        # Escreve cada NewsItem no arquivo CSV
        for news_items in news_items_list:
            for news_item in news_items:
                writer.writerow([news_item.date, news_item.title, news_item.description])
