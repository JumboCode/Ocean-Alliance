from os import listdir
from time import sleep

# some resources on sockets: https://docs.python.org/3/howto/sockets.html

# TODO look into multi-threading as well, as we probably want the cv code running on a seperate thread
#      so we can continuously listen to messages
#      nice resources: https://dbader.org/blog/understanding-asynchronous-programming-in-python

def dummyInput(files):
    print('received dummy input: {}'.format(files))
    # TODO send back some sort of confirmation, if we end up having python side validation    

def dummyProcessing(filename):
    for i in range(0, 100):
        sleep(0.5)
        # TODO some way to report back to Nodejs side of things
        #      maybe a callback to python server first, then that sends the actual message

def dummyOutput():
    # TODO check for file path issues when running on different OS
    files = listdir('./data/')
    print('found dummy files: {}'.format(files))
    return files
