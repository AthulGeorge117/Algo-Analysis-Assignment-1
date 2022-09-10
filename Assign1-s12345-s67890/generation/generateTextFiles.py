def createFile(dataFile, size, file):
    dList = [] 
    with open(dataFile , "r") as df:
        for each in df:
            dList.append(each)
    sizedList = []
    for each in range(0,size):
        sizedList.append(dList[each])
    output = ""
    for each in sizedList:
        output = output + each
    with open(f"{file}.txt", 'w') as file:
        file.write(output)
    
if __name__ == '__main__':
    sizes = [10, 50, 100, 1000, 5000, 10000, 50000, 100000, 200000]
    for each in sizes:
        createFile('sampleData200k.txt', each , file = "testData" + str(f"{each}words"))