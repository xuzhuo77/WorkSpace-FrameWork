from twisted.internet import protocol, reactor
from time import ctime
import pickle

from twisted.internet.protocol import Protocol

PORT = 21567


class TSServProtocol(Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):
        print(pickle.loads(data))
        # self.transport.write("[%s] %s".encode("utf8") % (ctime(), b"2333"))
        # data="data{}".format(data).encode("utf8")
        self.transport.write(data)
        print(dir(self.factory))


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()



