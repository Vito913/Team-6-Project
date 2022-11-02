from agent import Agent
import twitter
import helpers as h


def main():
    h.delete_data()
    agent = Agent()
    agent.sanity_check()
    print("Type the query you want to run:")
    question = input()
    if agent.query(question):
        print("This is true according to the ontology.")
    else:
        twitter.get_tweet_dataframe(question)
    
if __name__ == "__main__":
    main()

