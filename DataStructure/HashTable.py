class HashTbale:

    def __init__(self, arrSize):
        self.data_arr = [arrSize - 1]
        self.key_arr = [arrSize - 1]
        self.size = arrSize

    def hashkey(self, key):
        return key

    def Add(self, key, value):
        index = key - 1
        if index > self.size:
            raise RuntimeError(
                'index id is out of range, max id value is ', self.size)
        hash_key = self.hashkey(index)
        if self.key_arr[hash_key] != None:
            raise RuntimeError('this key is already taken, key code :', key)
        self.key_arr[hash_key] = key
        self.data_arr[hash_key] = value
        print('Added !')

    def Remove(self, key):
        index = key - 1
        hash_key = self.hashkey(index)
        if self.key_arr[hash_key] == None:
            raise RuntimeError('this key does not existis, key code', key)
        self.key_arr[hash_key] = None
        self.key_arr[hash_key] = None
        print('Deleted !')

    def print(self, printEmpty=False):
        for i in range(self.size):
            hash_key = self.hashkey(i)
            if self.key_arr[hash_key] == None and printEmpty == True:
                print('data in line', i + 1, 'is empty')
            elif self.key_arr[hash_key] != None:
                print('line id', i + 1, 'line value', self.data_arr[hash_key])
        print('end of printing')
