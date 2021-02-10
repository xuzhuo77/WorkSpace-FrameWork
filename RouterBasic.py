# from user import bp as user_bp
# from auth import AuthMethodView
from ViewBasic import ViewBasic
router = [
    # user_bp, # 用户蓝图接口
    ViewBasic, # 权限自定义MethodView
]


