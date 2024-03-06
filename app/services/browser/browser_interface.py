from abc import ABC, abstractmethod

class BrowserInterface(ABC):

    @abstractmethod
    def openPage(self, host):
        pass

    def extractByClass(self, elemento):
        pass