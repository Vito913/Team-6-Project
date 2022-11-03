from owlready2 import *
from pprint import pprint

class Agent:
    
    def __init__(self, path="ontology.owl"):
        # Loads ontology to self.onto
        self.onto = get_ontology(path).load()
        
        #saves classes and properties to self.classes and self.properties
        self.class_type = type(list(self.onto.classes())[0])
        self.propery_type = type(list(self.onto.properties())[0])

        # Initializes the reasoner
        with self.onto:
            sync_reasoner_pellet()
            
    # Sanity check
    def sanity_check(self):
        print("Classes: "+ "\n")
        for i in self.onto.classes():
            print(i)
        print("\n")
        print("Properties:"+"\n")
        for i in self.onto.properties():
            print(i)
            
        
    def query(self, query):
        #t = true, f = false, u = undecided
        decision = 'u'
        #for determining the type of query
        subclassQuestion = False
        causalQuestion = False
        valueQuestion = False
        someQuestion = False

        #the query is transformed into a list of words fit for processing
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        transformedInput = ''.join(filter(whitelist.__contains__, query))
        sentenceListUncap = transformedInput.split()
        sentenceListUncap2 = []
        for word in sentenceListUncap:
            if word == "higher":
                sentenceListUncap2.append("high")
            elif word == "lower":
                sentenceListUncap2.append("low")
            else:
                sentenceListUncap2.append(word)
        sentenceList = map(lambda word: word.capitalize(), sentenceListUncap2)

        #looping over the list and mapping words to something in the ontology if possible
        interpretableList = []

        for i in range(len(sentenceList)):
            if sentenceList[i] == 'Is':
                subclassQuestion = True
            elif sentenceList[i] == 'Cause':
                causalQuestion = True
            elif sentenceList[i] == 'Has':
                valueQuestion = True
            elif sentenceList[i] == 'Which':
                someQuestion = True
            else:
                searchWord = '*' + sentenceList[i]
                ontList = self.onto.search(iri = searchWord)
                if ontList:
                    interpretableList.append(ontList[0])
                elif i+1 < len(sentenceList):
                    concatWord = '*' + sentenceList[i] + '*'
                    concatList = self.onto.search(iri = concatWord)
                    nextConcatWord = concatWord = '*' + sentenceList[i+1]
                    nextConcatList = self.onto.search(iri = nextConcatWord)
                    finalConcatList= [value for value in concatList if value in nextConcatList]
                    if finalConcatList:
                        interpretableList.append(finalConcatList[0])
                        i += 1

        #answering the question, based on the concepts found and the type of question        
        if subclassQuestion:
            if interpretableList[1] == self.onto.get_parents_of(interpretableList[0])[0]:
                decision = 't'
            elif interpretableList[0] == self.onto.get_parents_of(interpretableList[1])[0]:
                decision = 'f'

        if causalQuestion:
            causalList = list(self.self.onto.CanCause.get_relations())
            for item in causalList:
                if (interpretableList[0], interpretableList[1]) == item:
                    decision = 't'
                    break

        if valueQuestion:
            print("test")

        if someQuestion:
            print("test")
         
        return decision