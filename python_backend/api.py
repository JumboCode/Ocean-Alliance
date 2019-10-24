import zerorpc
import cv2
import time, sys

# Create the zeroRPC client to run
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:9106")

class PythonApi(object):
    def echo(self, text):
        return text
    
    def ping(self):
        return 'Python version {}, epoch time {}'.format(sys.version, time.time())

    def startWorking(self, input, output):
        # print(c.hello("RPC"))
        updateProgress(50)
        finished()
        return 'Beginning work'

def main():
    # Create the zeroRPC server to run
    addr = 'tcp://127.0.0.1:' + sys.argv[1]
    s = zerorpc.Server(PythonApi())
    s.bind(addr)
    print('Python: start running on {}'.format(addr))
    s.run()

# Tell the Node.js server the current progress
def updateProgress(progress):
    response = c.progress(progress)
    print(response)

# Tell the Node.js server that we're done processing
def finished():
    response = c.finished()
    print(response)

if __name__ == '__main__':
    main()
