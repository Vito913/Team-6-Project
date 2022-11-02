from owlready2 import *
from pprint import pprint
from nltk.corpus import wordnet

class Agent:
    
    def __init__(self, path="ontology.owl"):
        # Loads ontology to self.onto
        self.onto = get_ontology(path).load()
        self.class_type = type(list(self.onto.classes())[0])
        self.propery_type = type(list(self.onto.properties())[0])
        # Sanity check
        with self.onto:
            sync_reasoner_pellet()
    
    def sanity_check(self):
        print("Classes: "+ "\n")
        for i in self.onto.classes():
            print(i)
        print("\n")
        print("Properties:"+"\n")
        for i in self.onto.properties():
            print(i)
            
        
    def query(self, query):
        decision = False
        #for determining the type of query
        subclassQuestion = False

        #the query is transformed into a list of words
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        transformedInput = ''.join(filter(whitelist.__contains__, query))
        sentenceListUncap = transformedInput.split()
        sentenceList = map(lambda word: word.capitalize(), sentenceListUncap)

        #looping over the list and mapping words to something in the ontology if possible
        interpretableList = []
        for i in sentenceList:
            if i == 'Is':
                subclassQuestion = True
            else:
                searchWord = '*' + i
                ontList = self.onto.search(iri = searchWord)
                if ontList:
                    interpretableList.append(ontList[0])
        
        if subclassQuestion:
            #print(self.onto.get_parents_of(interpretableList[0])[0])
            #print(interpretableList[1])
            if interpretableList[1] == self.onto.get_parents_of(interpretableList[0])[0]:
                decision = True
         

        return decision