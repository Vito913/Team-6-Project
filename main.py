from agent import Agent
import twitter
import helpers as h


def main():
    h.delete_data()
    agent = Agent()

    print("Type the query you want to run:")
    question = input()
    print(agent.return_string(question))
    df = twitter.get_tweet_dataframe(question)
    #get text from the first value in dataframe
    query = df['text'].iloc[0]
    if agent.query(query):
        print("This is true according to the ontology.")

if __name__ == "__main__":
    main()

