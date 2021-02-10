from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineOnlyReceiver
from twisted.internet import reactor
import random
import string
import pickle

from zhak_projects.agame.World import World
from zhak_projects.agame.zhgame import get_actor_list

test_list=get_actor_list()

class WorldService(World):
    def __init__(self):
        super(World,self).__init__()
    def create_actor(self,id):
        pass


class Game(LineOnlyReceiver):
    def lineReceived(self, line):
        print(line)
        # self.factory.sendAll("%s" % (line))
        self.factory.sendAllData(line)

    # def dataReceived(self, data):
    #     # self.transport.write(data)
    #     self.factory.sendAllData(data)

    def getId(self):
        return str(self.transport.getPeer())

    def connectionMade(self):
        print("New User Login:", self.getId())
        self.transport.write("欢迎来到MMO世界！\n".encode("utf8"))
        self.factory.addClient(self)

    def connectionLost(self, reason):
        self.factory.delClient(self)


class GameFactory(Factory):
    protocol = Game

    def __init__(self):
        self.clients = {}
        self.player = []
        self.msg = ''
        self.x = range(100, 700)
        self.y = range(100, 500)
        self.actiors={}
        self.id=0
        self.world=None
    def getPlayerId(self):
        return len(self.player)

    def addClient(self, newclient):
        # self.clients.append(newclient)
        actor=self.world.create_actor()
        self.clients[actor.id]=newclient

        self.sendAllData(actor.serialize())
        data=self.world.make_all_data()
        newclient.transport.write(data)


    def delClient(self, client):
        self.clients.remove(client)

    def sendAllData(self,data):
        print(data)
        for proto in self.clients:
            proto.transport.write("system Data {}".format(data).encode("utf8"))








reactor.listenTCP(8006, GameFactory())
reactor.run()