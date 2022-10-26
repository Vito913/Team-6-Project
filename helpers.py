import os

#Open the file twitter_data.txt and read the data
def get_data():
    __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, "twitter_data.txt"),"r")
    return file.read()

# open the file_twitter.txt data and delete the contents
def delete_data():
    __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, "twitter_data.txt"), "w")
    file.write("")
    file.close()
    
# open the file twitter_data.txt and add the data
def add_data(data):
    __location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, "twitter_data.txt"), "a")
    file.write(data)
    file.close()

