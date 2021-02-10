from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)

CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}

@app.route('/hell1o', methods=['get'])
def hell1o():
    print(1)
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.greeting_service.hello(name="jerry")
        print(2)
    return result,"a"


app.run(host="0.0.0.0", port=5010, debug=True)
