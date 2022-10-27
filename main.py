from agent import Agent
import twitter
import helpers as h

def main():
    h.delete_data()
    agent = Agent()
    print("Type the query you want to run:")
    query = input()
    twitter.get_query_tweets(query)
    
    
if __name__ == "__main__":
    main()

