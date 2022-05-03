import numpy as np
import pandas as pd
from datetime import datetime

tableColumnNameMap = {
    'Affiliations': ['AffiliationId', 'Rank', 'NormalizedName', 'DisplayName', 'GridId', 'OfficialPage', 'WikiPage', 'PaperCount', 'PaperFamilyCount', 'CitationCount', 'Iso3166Code', 'Latitude', 'Longitude', 'CreatedDate'],
    'Authors': ['AuthorId', 'Rank', 'NormalizedName', 'DisplayName', 'LastKnownAffiliationId',	'PaperCount', 'PaperFamilyCount', 'CitationCount', 'CreatedDate'],
    'PaperAuthorAffiliations': ['PaperId', 'AuthorId', 'AffiliationId', 'AuthorSequenceNumber', 'OriginalAuthor', 'OriginalAffiliation'],
    'PaperReferences': ['PaperId', 'PaperReferenceId'],
    'Papers': ['PaperId','Rank','Doi','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','OnlineDate','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId','Volume','Issue','FirstPage','LastPage','ReferenceCount','CitationCount','EstimatedCitation','OriginalVenue','FamilyId','FamilyRank','CreatedDate']
}

datatypeMap = {
    'Affiliations': {'AffiliationId': 	'Int64',
                     'Rank': 	np.uint,
                     'NormalizedName': 	str,
                     'DisplayName': 	str,
                     'GridId': 	str,
                     'OfficialPage': 	str,
                     'WikiPage': 	str,
                     'PaperCount': 	'Int64',
                     'PaperFamilyCount': 	'Int64',
                     'CitationCount': 	'Int64',
                     'Iso3166Code': 	str,
                     'Latitude': 	np.float64,
                     'Longitude': 	np.float64,
                     'CreatedDate': 	str},
    'Authors': {'AuthorId': 'Int64',
                'Rank': np.uint,
                'NormalizedName': str,
                'DisplayName': str,
                'LastKnownAffiliationId': 'Int64',
                'PaperCount': 'Int64',
                'PaperFamilyCount': 'Int64',
                'CitationCount': 'Int64',
                'CreatedDate': str},
    'PaperAuthorAffiliations': {'PaperId': 'Int64',
                                'AuthorId': 'Int64',
                                'AffiliationId': 'Int64',
                                'AuthorSequenceNumber': np.uint,
                                'OriginalAuthor': str,
                                'OriginalAffiliation': str},
    'PaperReferences': {'PaperId': 'Int64',
                        'PaperReferenceId': 'Int64'},
    'Papers': {'PaperId': 'Int64',
               'Rank': np.uint,
               'Doi': str,
               'DocType': str,
               'PaperTitle': str,
               'OriginalTitle': str,
               'BookTitle': str,
               'Year': 'Int64',
               'Date': 'datetime64[ns]',
               'OnlineDate': 'datetime64[ns]',
               'Publisher': str,
               'JournalId': 'Int64',
               'ConferenceSeriesId': 'Int64',
               'ConferenceInstanceId': 'Int64',
               'Volume': str,
               'Issue': str,
               'FirstPage': str,
               'LastPage': str,
               'ReferenceCount': 'Int64',
               'CitationCount': str,
               'EstimatedCitation': 'Int64',
               'OriginalVenue': str,
               'FamilyId': 'Int64',
               'FamilyRank': 'Int64',
               'CreatedDate': 'datetime64[ns]'}
}

class Parser:
    '''
    Seperate parser method for the PaperAuthorAffiliation table
    '''
    def parsePaperAuthorAffiliations(self, tableFileChunkName):
        data = []
        with open('./data/{}.txt'.format(tableFileChunkName), 'r') as fp:
            for line in fp.readlines():
                if(len(line.split('\t')) == 6):
                    row = [val.strip() for val in line.split('\t')]
                    row[0] = int(row[0]) if(len(row[0]) != 0) else None
                    row[1] = int(row[1]) if(len(row[1]) != 0) else None
                    row[2] = int(row[2]) if(len(row[2]) != 0) else None
                    row[3] = int(row[3]) if(len(row[3]) != 0) else None
                    data.append(row)
            data = pd.DataFrame(data, columns = tableColumnNameMap['PaperAuthorAffiliations'])
            data = data.astype(datatypeMap['PaperAuthorAffiliations'])
        return data

    '''
    Seperate parser method for the Papers table
    '''
    def parsePapers(self, tableFileChunkName):
        data = []
        custom_date_parser = lambda x: datetime.strptime(x, "%Y-%m-%d")
        with open('./data/{}.txt'.format(tableFileChunkName), 'r') as fp:
            lineNumber = 0
            for line in fp.readlines():

                lineNumber += 1
                if(lineNumber%100000 == 0):
                    print('processed ', lineNumber)

                if(len(line.split('\t')) == 25):
                    row = [val.strip() for val in line.split('\t')]
                    row[0] = int(row[0]) if(len(row[0]) != 0) else None
                    row[1] = int(row[1]) if(len(row[1]) != 0) else None
                    row[7] = int(row[7]) if(len(row[7]) != 0) else None
                    row[8] = custom_date_parser(row[8]) if(len(row[8]) != 0) else None
                    row[9] = custom_date_parser(row[9]) if(len(row[9]) != 0) else None
                    row[11] = int(row[11]) if(len(row[11]) != 0) else None
                    row[12] = int(row[12]) if(len(row[12]) != 0) else None
                    row[13] = int(row[13]) if(len(row[13]) != 0) else None
                    row[18] = int(row[18]) if(len(row[18]) != 0) else None
                    row[19] = int(row[19]) if(len(row[19]) != 0) else None
                    row[20] = int(row[20]) if(len(row[20]) != 0) else None
                    row[22] = int(row[22]) if(len(row[22]) != 0) else None
                    row[23] = int(row[23]) if(len(row[23]) != 0) else None
                    row[24] = custom_date_parser(row[24]) if(len(row[24]) != 0) else None
                    data.append(row)
            data = pd.DataFrame(data, columns = tableColumnNameMap['Papers'])
            data = data.astype(datatypeMap['Papers'])
        return data

    '''
    Common parser method used to parse data from different .txt files for Tables
    '''
    def parseTableData(self, tableName, tableFileChunkName):
        if(tableName == 'PaperAuthorAffiliations'):
            data = self.parsePaperAuthorAffiliations(tableFileChunkName)
        elif(tableName == 'Papers'):
            data = self.parsePapers(tableFileChunkName)
        else:
            columnNames = tableColumnNameMap[tableName]
            columnDatatypes = datatypeMap[tableName]
            dataFilePath = './data/{}.txt'.format(tableFileChunkName)
            data =  pd.read_csv(dataFilePath, sep='\t', names=columnNames, dtype=columnDatatypes, parse_dates=True)

            if(tableName in ['Authors', 'Affiliations']):
                data['CreatedDate'] = data['CreatedDate'].astype('datetime64[ns]')

        return data


