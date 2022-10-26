from agent import Agent

def main():
    print("Type the query you want to run:")
    query = input()
    agent = Agent()
    agent.sanity_check()
    
if __name__ == "__main__":
    main()

