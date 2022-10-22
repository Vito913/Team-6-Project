import os
from owlready2 import *

script_dir = os.path.dirname(__file__)
rel_path = "New_Ontology.owl"
abs_file_path = os.path.join(script_dir, rel_path)

onto = get_ontology(abs_file_path).load()

print(list(onto.classes()))