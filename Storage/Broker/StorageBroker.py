import pickle


class StorageBroker:
    def __init__(self) -> None:
        self.path = './Storage/Data'

    def SaveToFile(self, fileName: str, objectToSave):
        with open(f'{self.path}/{fileName}.dbfile', 'wb') as contextFile:
            pickle.dump(objectToSave, contextFile)

    def LoadFromFile(self, fileName: str, objectToLoad):
        with open(f'{self.path}/{fileName}.dbfile', 'rb') as contextFile:
            objectToLoad = pickle.load(contextFile)
