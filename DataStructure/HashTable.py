class HashTbale:
    cell_is_empty = 0
    cell_is_full = 1

    def __init__(self, arrSize):
        self.data_arr = [0] * (arrSize)
        self.key_arr = [0] * (arrSize)
        self.status_arr = [0] * (arrSize)
        self.size = arrSize

    def hashkey(self, key):
        return key

    def Add(self, key, value):
        index = key - 1
        if index > self.size:
            raise RuntimeError(
                'index id is out of range, max id value is ', self.size)
        hash_key = self.hashkey(index)
        if self.status_arr[hash_key] == self.cell_is_full:
            print(self.status_arr[hash_key])
            raise RuntimeError('this key is already taken, key code :', key)
        self.key_arr[hash_key] = key
        self.data_arr[hash_key] = value
        self.status_arr[hash_key] = self.cell_is_full
        print('Added !')

    def Remove(self, key):
        index = key - 1
        hash_key = self.hashkey(index)
        if self.status_arr[hash_key] == self.cell_is_empty:
            raise RuntimeError('this key does not existis, key code', key)
        self.key_arr[hash_key] = None
        self.key_arr[hash_key] = None
        self.status_arr[hash_key] = self.cell_is_empty
        print('Deleted !')

    def Print(self, printEmpty=False):
        for i in range(self.size):
            hash_key = self.hashkey(i)
            if self.status_arr[hash_key] == self.cell_is_empty and printEmpty == True:
                print('data in line', i + 1, 'is empty')
            elif self.status_arr[hash_key] == self.cell_is_full:
                print('line id', i + 1, 'line value', self.data_arr[hash_key])
        print('end of printing')
