from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from .parser import Parser
from .data import Data

app = Flask(__name__)
cors = CORS(app)
parser = Parser()
dataRepo = Data()

'''
API
Returns the most referenced papers for a given Author
'''
@app.route('/mostcited', methods = ['GET', 'OPTIONS'])
@cross_origin()
def topReferencedPapers():
    authorId = request.args.get('authorId')
    topK = request.args.get('topK') if(request.args.get('topK')) else 10

    response = dataRepo.topReferencedPapers(authorId, topK)

    return jsonify(response)

'''
API
Returns the List of instituions which collaborated the most with the authors of a given institution
'''
@app.route('/mostaffliated', methods = ['GET', 'OPTIONS'])
@cross_origin()
def topAffliatedInstitutions():
    affiliationId = request.args.get('affiliationId')
    response = dataRepo.getTopCollabInstitutions(affiliationId)

    return jsonify(response)