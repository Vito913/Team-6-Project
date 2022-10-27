from owlready2 import *
from pprint import pprint
from nltk.corpus import WordNet

class Agent:
    
    def __init__(self, path="ontology.owl"):
        self.onto = get_ontology(path).load()
        with self.onto:
            sync_reasoner(infer_property_values=True)
    
    def sanity_check(self):
        pprint(self.onto.classes)
        pprint(self.onto.properties)
        pprint(self.onto.individuals)
    
    def query(self, query):
        #the query is transformed into a list of words
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        transformedInput = ''.join(filter(whitelist.__contains__, query))
        sentenceListUncap = transformedInput1.split()
        sentenceList = map(lambda word: word.capitalize(), sentenceListUncap)

        #looping over the list and mapping words to something in the ontology if possible
        interpretableList = []
        for i in sentenceList:
            searchWord = '*' + i
            ontList = onto.search(iri = searchWord)
            if ontList:
                interpretableList.append(ontList[0])
            else:
                synonyms = []
                for syn in wordnet.synsets(i.lower()):
                    for j in syn.lemmas():
                     synonyms.append(j.name())
                for synonym in synonyms:
                    searchSynonym = '*' + synonym.capitalize()
                    synList = onto.search(iri = searchSynonym)
                    if synList:
                        interpretableList.append(synList[0])
                        break

        return interpretableList