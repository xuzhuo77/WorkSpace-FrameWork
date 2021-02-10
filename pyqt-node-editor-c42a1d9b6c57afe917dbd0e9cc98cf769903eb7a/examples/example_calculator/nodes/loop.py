
from examples.example_calculator.calc_conf import *
from examples.example_calculator.calc_node_base import *

times=10
import asyncio  # 引入 asyncio 库
import asyncio

from nodeeditor.utils import dumpException



import threading, time


def implementRunner():
    for x in range(3):
        time.sleep(111)
        print('a.x', x)


# 定义
# 连接进来的节点循环
# 有节点1后启动循环

# 控件
# 1,总循环次数显示输入控件
# 2,当前循环次数显示控件
# 3 功能接入
#
# 输入节点
# 1 总次数输入点
# 2 功能输入点
# 问题
# input node 能让以后节点全部执行
#





class LOOPContent(QDMNodeContentWidget):
    def initUI(self):

        self.inner_layout = QVBoxLayout()
        self.setLayout(self.inner_layout)
        self.L_mainloop = QLineEdit("0", self)
        self.L_current_i = QLabel("now_times:0", self)
        self.L_function = QLabel("pre node", self)

        self.L_mainloop.setAlignment(Qt.AlignLeft)
        self.L_mainloop.setObjectName(self.node.content_label_objname)

        self.configWidget(self.L_mainloop)
        self.configWidget(self.L_current_i)
        self.configWidget(self.L_function)


    def getInnerWidgetPos(self,idx):
        posHeight=60
        for i in range(idx):
           posHeight+=self.inner_layout.itemAt(i).geometry().height()+self.inner_layout.spacing()
        return posHeight

    def configWidget(self,widget):
        # setcolor
        if self.inner_layout.count()%2==0:
            widget.setStyleSheet("background-color:#4B4B4B;")
        else:
            widget.setStyleSheet("background-color:#242424;")
        height=widget.geometry().height()
        self.height_pp +=height
        self.inner_layout.addWidget(widget)

    def selectionchange(self, i):
        self.node.id_matric=i

@register_node(OP_LOOP)
class LOOP_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_LOOP
    op_title = "OP_LOOP"
    content_label_objname = "OP_LOOP"
    loop_times=1
    start=False
    def __init__(self, scene):
        super().__init__(scene, inputs=[1,1], outputs=[])

    def initInnerClasses(self):
        self.content = LOOPContent(self)
        self.grNode = CalcGraphicsNode(self)
    def tesInplemetn(self,inpu):
        print("start")
        i=0
        for x in range(self.loop_times):
            time.sleep(1)
            i+=1
            self.content.L_current_i.setText("%d" % i)
        self.start=False
        print("end")



    def eval(self,param={}):
        if not self.isDirty() and not self.isInvalid():
            print(" _> returning cached %s value:" % self.__class__.__name__, self.value)
            return self.value

        try:
            val = self.evalImplementation(param)
            return val
        except ValueError as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            self.markDescendantsDirty()
        except Exception as e:
            self.markInvalid()
            self.grNode.setToolTip(str(e))
            dumpException(e)



    def evalImplementation(self,inpu):

        loop_value = self.getInput(0)
        function_run = self.getInput(1)

        socket1 = self.getInputSocket(0)
        socket2 = self.getInputSocket(1)


        if loop_value:
            val=loop_value.eval({})
            self.content.L_mainloop.setText("loop_times:"+str(val))
            self.loop_times=val


        self.content.L_mainloop.setText(str(val))
        self.loop_times=int(self.content.L_mainloop.text())


        if function_run is None:
            self.grNode.setToolTip("Function is not connected")
            self.markInvalid()
            return

        if not self.start:
            threading.Thread(target=self.tesInplemetn,args=([],)).start()


        self.content.L_mainloop.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val




