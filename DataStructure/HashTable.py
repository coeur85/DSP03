class HashTbale:
    cell_is_empty = 0
    cell_is_full = 1

    def __init__(self, arrSize):
        self.data_arr = [0] * (arrSize)
        self.key_arr = [0] * (arrSize)
        self.status_arr = [0] * (arrSize)
        self.size = arrSize

    def __computeHashkey(self, key):        # privet method
        return key

    def __validatekey(self, key):
        if key < 1:
            raise RuntimeError(
                'index must be greater than or equal to 1, key :', key)
        if key > self.size:
            raise RuntimeError('index is out of range of the hash table')

    def Add(self, key, value):
        self.__validatekey(key)
        index = key - 1
        hash_key = self.__computeHashkey(index)
        if self.status_arr[hash_key] == self.cell_is_full:
            raise RuntimeError('this key is already taken, key code :', key)
        self.key_arr[hash_key] = key
        self.data_arr[hash_key] = value
        self.status_arr[hash_key] = self.cell_is_full

    def Remove(self, key):
        self.__validatekey(key)
        index = key - 1
        hash_key = self.__computeHashkey(index)
        if self.status_arr[hash_key] == self.cell_is_empty:
            raise RuntimeError('this key does not existis, key code', key)
        self.key_arr[hash_key] = None
        self.key_arr[hash_key] = None
        self.status_arr[hash_key] = self.cell_is_empty

    def Select(self, key):
        self.__validatekey(key)
        index = key - 1
        hash_key = self.__computeHashkey(index)
        if self.status_arr[hash_key] == self.cell_is_empty:
            return None
        else:
            return self.data_arr[hash_key]

    def Update(self, key, value):
        self.__validatekey(key)
        index = key - 1
        hash_key = self.__computeHashkey(index)
        if self.status_arr[hash_key] == self.cell_is_empty:
            raise RuntimeError('this key does not existis, key code', key)
        else:
            self.data_arr[hash_key] = value
