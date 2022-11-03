# Explanation of the files

## agent.py

The agent class. Has the initialization method, has a 'sanity check' method for outputting classes and properties and the query method.
The latter method is supposed to extract keywords for the type of question and concepts in the ontology from natural language, to then use those to check for (in)consistency with the ontology. But alas, due to time constraints (loading of the ontology taking 15 minutes for each testing of the code and owlready2 being particularly unfit to work with natural language) this method is currently, in the latest version, inoperable and incomplete.

## helpers.py

A file containing methods used for reading information from twitter-data.

## main.py

Main method. Initializes the agent and has a loop for asking for and passing on input.

## ontology.owl

Contains the ontology.

## twitter.py

For reading tweets.
