import sqlalchemy
import pandas as pd
from functools import lru_cache


class Data:
    def __init__(self) -> None:
        config = {
            'database_username': '<username>',
            'database_password': '<password>',
            'database_ip': '<database_host>',
            'database_name': 'educationtoday'
        }

        self.database_connection = sqlalchemy.create_engine(
            'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(config['database_username'], config['database_password'],
                                                            config['database_ip'], config['database_name']), connect_args={'connect_timeout': 3600})

    def closeConnection(self):
        self.database_connection.dispose()

    '''
    Helps store a given pandas dataframe (tableDataFrame) into DB
    '''
    def storeTableData(self, tableDataFrame, tableName):
        tableDataFrame.to_sql(con=self.database_connection,
                              name=tableName, if_exists='append', chunksize=10000)

    '''
    This method helps check if a given author ID exists in DB
    '''
    def checkAuthorExists(self, authorId):
        sqlQuery = sqlalchemy.text(
            'SELECT authorId FROM authors WHERE AuthorId = {}'.format(authorId))

        result = self.database_connection.execute(sqlQuery)
        resultList = result.fetchall()

        return len(resultList) > 0

    '''
    This method finds the Paper's title given its ID
    '''
    def findPaperName(self, paperId):
        sqlQuery = sqlalchemy.text(
            'SELECT OriginalTitle FROM papers WHERE PaperId = {}'.format(paperId))

        result = self.database_connection.execute(sqlQuery)
        return result.fetchone()[0]

    @lru_cache
    def topReferencedPapers(self, authorId, topK=10):
        if(self.checkAuthorExists(authorId)):
            query = ''' SELECT PaperReferenceId, count(PaperReferenceId) FROM paperreferences 
                WHERE PaperId in (SELECT PaperId from paperauthoraffiliations where AuthorId = {0})
                GROUP BY(PaperReferenceId) 
                ORDER BY count(PaperReferenceId) DESC
                LIMIT {1}
            '''.format(authorId, topK)

            sqlQuery = sqlalchemy.text(query)
            result = self.database_connection.execute(sqlQuery)
            resultList = result.fetchall()

            topReferencedPaperIds = [refId for refId,count in resultList]
            print(topReferencedPaperIds)

            return [self.findPaperName(paperId) for paperId in topReferencedPaperIds]
        else:
            return []

    '''
    Returns the list of PaperID's published by authors from a given Institute
    '''
    @lru_cache
    def getPapersFromAnInstitution(self, affliationId):
        query = '''SELECT DISTINCT PaperId FROM paperauthoraffiliations 
                WHERE AuthorId IN (SELECT AuthorId FROM authors WHERE LastKnownAffiliationId = {})
                '''.format(affliationId)

        sqlQuery = sqlalchemy.text(query)
        result = self.database_connection.execute(sqlQuery)
        resultList = result.fetchall()

        print(resultList)
        return [str(row[0]) for row in resultList] 

    '''
    Returns the list of top collaborating Affliations to a given institute
    '''
    def getTopCollabInstitutions(self, affliationId):
        associatedPapers = self.getPapersFromAnInstitution(affliationId)

        query = '''
        SELECT LastKnownAffiliationId, count(LastKnownAffiliationId) FROM authors 
        WHERE AuthorId IN (SELECT DISTINCT AuthorId FROM paperauthoraffiliations WHERE PaperId IN ({})) 
        GROUP BY(LastKnownAffiliationId)
        ORDER BY count(LastKnownAffiliationId) DESC;
        '''.format(','.join(associatedPapers))

        sqlQuery = sqlalchemy.text(query)
        result = self.database_connection.execute(sqlQuery)
        resultList = result.fetchall()

        print(resultList)
        return [{'affiliationId': affiliationId, 'count':count} for affiliationId, count in resultList]
    
