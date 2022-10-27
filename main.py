from agent import Agent
import twitter

def main():
    print("Type the query you want to run:")
    query = input()
    twitter.get_query_tweets(query)
    agent = Agent()
    agent.sanity_check()
    print(agent.property_type)
    print(agent.class_type)
    
if __name__ == "__main__":
    main()

