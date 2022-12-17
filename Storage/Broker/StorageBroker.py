import pickle
import os


class StorageBroker:
    def __init__(self) -> None:
        self.path = './Storage/Data'

    def SaveToFile(self, fileName: str, objectToSave):
        with open(f'{self.path}/{fileName}.dbfile', 'wb') as contextFile:
            pickle.dump(objectToSave, contextFile)

    def LoadFromFile(self, fileName: str):
        if os.path(f'{self.path}/{fileName}.dbfile') != True:
            return None
        with open(f'{self.path}/{fileName}.dbfile', 'rb') as contextFile:
            objectToLoad = pickle.load(contextFile)
            return objectToLoad
