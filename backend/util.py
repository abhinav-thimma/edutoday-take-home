from .parser import Parser
from .data import Data

parser = Parser()
dataRepo = Data()

def parseAndStoreTableData(tableName, tableFileChunkName):
    data = parser.parseTableData(tableName, tableFileChunkName)
    print(data.info())

    dataRepo.storeTableData(data, 'papers')
    print('Successfully stored the data in DB for:', tableName)

def splitFile():
    with open('./data/Papers.txt', 'r') as fp:
        lines = fp.readlines()
        count = 1
        chunkSize = 1000000
        totalCount = len(lines)

        for i in range(0, totalCount, chunkSize):
            fileName = 'Papers{}.txt'.format(count)
            writeFile = open('./data/' + fileName, 'w+') 
            writeFile.writelines(lines[i: min(i+chunkSize, totalCount)])
            count += 1
