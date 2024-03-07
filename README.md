## README - Extração de Notícias Governamentais de São Paulo

<p>
 Este script Python realiza a extração de notícias governamentais de São Paulo a partir de um site específico, utilizando threads para melhorar a eficiência do processo.
</p>


## Pré-requisitos
- Python 3.x instalado<br>
- Bibliotecas Python necessarias : instalada `pip install -r requirements.txt`


## Uso 
- Clone ou baixe este repositório para sua máquina local.
- No terminal, navegue até o diretório do projeto
- Execute o script `python run.py`:


```sh
python run.py
```

## Funcionalidades

- O script acessa um site específico para extrair notícias governamentais de São Paulo.
- Utiliza threads para processar várias páginas simultaneamente, aumentando a eficiência da extração de dados.
- Salva as notícias extraídas em um arquivo CSV na pasta `data/news` com o nome no formato `NEWS_SP_DD_MM_YYYY.csv`, onde `DD_MM_YYYY` representa a data atual.

## Arquivos do Projeto
- `run.py`: Script principal que executa a extração de notícias.
- `app/services/browser/chrome.py`: Módulo responsável pela inicialização e manipulação de uma instância do navegador Chrome.
- `app/services/news/extract.py`: Módulo que contém a classe Extractor responsável pela extração de notícias do site.
- `app/services/news/load.py`: Módulo para salvar os dados extraídos em um arquivo CSV.


## Autor
Este script foi desenvolvido por @Pedro Willian
