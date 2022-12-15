from DataStructure.HashTable import HashTbale


studentTable = HashTbale(10)

studentTable.Add(1, 'ahmed')
studentTable.Add(2, 'israa')
studentTable.Add(3, 'eman')

studentTable.Remove(2)
studentTable.Print(printEmpty=True)
