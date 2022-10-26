from owlready2 import *
from pprint import pprint

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
        return self.onto.search(query)