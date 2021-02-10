import cProfile
from nameko.standalone.rpc import ClusterRpcProxy

config = {
    'AMQP_URI': "pyamqp://guest:guest@111.229.148.2"
}


def test():
    with ClusterRpcProxy(config) as cluster_rpc:
        rs = cluster_rpc.greeting_service.hello("world wwwwk")
        print(rs)
def test2():
    with ClusterRpcProxy(config) as cluster_rpc:
        rs = cluster_rpc.docnewcheckplan_service.find_list()
        print(rs)

if __name__ == '__main__':
    # cProfile.run('test()')
    # test2()
    test2()
