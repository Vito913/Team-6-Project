from agent import Agent
import twitter
import helpers as h
from owlready2 import World


def main():
    
    h.delete_data()
    agent = Agent()

    while(True):
        print("Type the query you want to run:")
        question = input()
        df = twitter.get_tweet_dataframe(question)
        my_world = World()
        graph = my_world.as_rdflib_graph()
        #get text from the first value in dataframe
        query = df['text'].iloc[0]
        agentAnswer = agent.query(query)
        if agentAnswer == 't':
            print("This is true according to the ontology.")
        elif agentAnswer == 'f':
            print("This is false according to the ontology.")
        else:
            print("The question is not answerable.")


if __name__ == "__main__":
    main()

