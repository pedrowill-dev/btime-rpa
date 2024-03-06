from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from app.services.browser.chrome import Chrome
from app.services.news.extract import Extractor
from app.services.news.load import write_to_csv

def process_page(extractor, page_number):
    extractor.openGovNewsFiltered(page=page_number)
    return extractor.extractNews()

def generate_filename():
    today = datetime.today()
    return f"NEWS_SP_{today.strftime('%d_%m_%Y')}.csv"

filename = generate_filename()

def main():
    # Deve acessar o site
    chrome = Chrome()

    # Responsável por armazenar
    data = []

    # Deve criar um objeto do tipo Extractor
    extractorNewsGovSp = Extractor(month="Fevereiro", year="2023", pageStart=1, pageEnd=8, browser=chrome)

    # Lista para armazenar os objetos futuros
    futures = []

    # Para cada página em um range de páginas
    with ThreadPoolExecutor() as executor:
        for page_number in range(extractorNewsGovSp.pageStart, extractorNewsGovSp.pageEnd + 1):
            # Adiciona a execução da função process_page à pool de threads
            future = executor.submit(process_page, extractorNewsGovSp, page_number)
            futures.append(future)

    # Coleta os resultados das threads
    for future in futures:
        data.append(future.result())


    write_to_csv(file_path=filename, news_items_list=data)

