import zerorpc
import cv2
import time, sys

class PythonApi(object):
    def echo(self, text):
        return text
    
    def ping(self):
        return 'Python version {}, epoch time {}'.format(sys.version, time.time())

def main():
    addr = 'tcp://127.0.0.1:' + sys.argv[1]
    s = zerorpc.Server(PythonApi())
    s.bind(addr)
    print('Python: start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
