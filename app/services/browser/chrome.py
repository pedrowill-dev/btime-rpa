from selenium import webdriver
from app.services.browser.browser_interface import BrowserInterface
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random


from selenium.webdriver.common.by import By


class Chrome(BrowserInterface):

    def __init__(self):
        # Lista de user-agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            # Adicione mais user-agents conforme necessário
        ]

        # Seleciona um user-agent aleatório
        self.random_user_agent = random.choice(self.user_agents)

        # Configurações do Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument(f'user-agent={self.random_user_agent}')
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option("useAutomationExtension", False)


        # Instancia o driver do Chrome usando o ChromeDriverManager
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def openPage(self, host):
        return self.driver.get(host)

    def extractByClass(self, elemento: str):
        response = self.driver.find_elements(By.CLASS_NAME, elemento)
        return response



