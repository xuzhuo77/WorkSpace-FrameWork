from twisted.internet import protocol, reactor
import heapq
import queue
import _thread

# global commend_queue
from twisted.protocols.basic import LineReceiver

from zhak_projects.agame.World import World

commend_queue=queue.Queue(20)
li = ["5", "7", "9", "1", "3"]
# [commend_queue.put(a)  for a in li]
# print(commend_queue.get())
HOST = "localhost"
PORT = 8006

class WorldClient(World):
    def __init__(self):
        super(World,self).__init__()
    def create_actor(self,id):
        pass
def commend(action):
    def sendData():
        w=action()
    return sendData


world=WorldClient()

@commend
def action():
    return "真的"
import time

import pickle
def make_data():
    # time.sleep(1)
    return commend_queue.get()
def t():
    for i in range(15):
        time.sleep(2)
        if commend_queue.full() is False:
            commend_queue.put(pickle.dumps({"a":"25222"}))



class TSClntProtocol(LineReceiver):
    def sendData(self):
        # data=make_data()
        data=input(">").encode("utf8")
        if data:
            print('...sending %s...' % data)
            self.sendLine(data)
            # self.transport.write(data)
        else:
            self.transport.loseConnection()


    def connectionMade(self):
        self.transport.write("i am in".encode("utf8"))
        self.world.create_actor()

    def dataReceived(self, data):
        print(data.decode("utf8"))

        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()
def f(s):
    print ("this will run 3.5 seconds after it was scheduled: %s" % s)

if __name__ == '__main__':
    # _thread.start_new_thread( t, ( ) )
    reactor.callLater(3.5, f, "hello, world")
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()

