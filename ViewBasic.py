from flask.views import MethodView


class ViewBasic(MethodView):
    # 指定需要启用的请求方法
    __methods__ = ["GET", "POST", "PUT"]


    def get(self):

        return "测试自定义MethodView Get"

    def post(self):

        return "'Post User called'"

    def put(self):
        return "测试自定义MethodView"

    def delete(self):
        return "测试自定义MethodView"

    from flask import Flask, Blueprint
    from RouterBasic import router

# def create_app():
#         """
#         工厂模式创建APP
#         """
#         app = Flask(__name__)
#         # 注册接口
#         register_api(app, router)
#
#         return app

def register_api(app, routers):
        """
        注册蓝图和自定义MethodView
        """
        for router in routers:
            if isinstance(router, Blueprint):
                app.register_blueprint(router)
            else:
                try:
                    endpoint = router.__name__
                    view_func = router.as_view(endpoint)
                    # url默认为类名小写
                    url = '/{}/'.format(router.__name__.lower())
                    if 'GET' in router.__methods__:
                        app.add_url_rule(url, view_func=view_func, methods=['GET', ])
                        # app.add_url_rule(url, defaults={'keys': None}, view_func=view_func, methods=['GET', ])
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['GET', ])
                    if 'POST' in router.__methods__:
                        app.add_url_rule(url, view_func=view_func, methods=['POST', ])
                        list_ = '{}<string:key>'.format(url)
                        app.add_url_rule(list_, view_func=view_func, methods=['POST', ])

                    if 'PUT' in router.__methods__:
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['PUT', ])
                    if 'DELETE' in router.__methods__:
                        app.add_url_rule('{}<string:key>'.format(url), view_func=view_func, methods=['DELETE', ])
                except Exception as e:
                    raise ValueError(e)
