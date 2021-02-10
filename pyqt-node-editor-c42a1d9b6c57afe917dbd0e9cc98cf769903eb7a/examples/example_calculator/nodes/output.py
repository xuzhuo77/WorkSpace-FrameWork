from PyQt5.QtCore import *
from examples.example_calculator.calc_conf import *
from examples.example_calculator.calc_node_base import *
from nodeeditor.node_content_widget import QDMNodeContentWidgetInnerLayout
from nodeeditor.utils import dumpException
import numpy as np

class CalcOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.lbl = QLabel("42", self)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_NODE_OUTPUT)
class CalcNode_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_OUTPUT
    op_title = "Output"
    content_label_objname = "calc_node_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = CalcOutputContent(self)
        self.grNode = CalcGraphicsNode(self)

    def evalImplementation(self):





        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return

        val = input_node.eval()

        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        self.content.lbl.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val


class DataseOutputContent(QDMNodeContentWidget):
    def initUI(self):
        self.lbl = QTextEdit("42", self)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setObjectName(self.node.content_label_objname)

@register_node(OP_NODE_DATASAT_OUTPUT)
class DatasetNode_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_DATASAT_OUTPUT
    op_title = "Dataset_Output"
    content_label_objname = "calc_node_dataset_output"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        self.content = DataseOutputContent(self)
        self.grNode = CalcGraphicsNode(self)



    def eval(self,param):
        # input_node = self.getInput(0)
        # self.outputs
        socket =self. getInputSocket(0)
        input_node=socket.node
        val=input_node.eval({"a":socket})

        self.content.lbl.setText(str(val))



    def evalImplementation(self):
        input_node = self.getInput(0)
        if not input_node:
            self.grNode.setToolTip("Input is not connected")
            self.markInvalid()
            return
        outputs=input_node.getOutputs()

        val = input_node.eval()
        # val=val[str(idx)]

        if val is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        self.content.lbl.setText( str(val))
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return val


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class OutputPlotContent(QDMNodeContentWidget):
    def initUI(self):
        self.figure = plt.figure(facecolor='#FFD7C4')
        self.canvas=FigureCanvas( self.figure)
        self.lbl = QVBoxLayout(self)
        self.lbl.setAlignment(Qt.AlignLeft)
        self.lbl.addWidget(self.canvas)
        self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_NODE_OUTPUT_PLOT)
class CalcNode_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OP_NODE_OUTPUT_PLOT
    op_title = "OUTPUT_PLOT"
    content_label_objname = "OP_NODE_OUTPUT_PLOT"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1,1], outputs=[])

    def initInnerClasses(self):
        self.content = OutputPlotContent(self)
        self.grNode = CalcGraphicsNode(self)

    def evalImplementation(self,param):
        x_input = self.getInput(0)
        y_input = self.getInput(1)

        # if not input_node:
        #     self.grNode.setToolTip("Input is not connected")
        #     self.markInvalid()
        #     return
        #
        # x = x_input.eval({})
        socket2 =self. getInputSocket(1)

        y = y_input.eval({"a":socket2})


        if  y is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        ax =self.content.figure.add_subplot(111)
        x = np.linspace(0, 100, y.shape[0])
        # y = np.random.random(40)
        ax.cla()  # TODO:删除原图，让画布上只有新的一次的图
        ax.plot(x, y)
        self.content.canvas.draw()  # TODO:这里开始绘制

        # self.content.lbl.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return 0

class OutputPlotGPContent(QDMNodeContentWidgetInnerLayout):
    def initUI(self):
        self.figure = plt.figure(facecolor='#FFD7C4')
        self.canvas=FigureCanvas( self.figure)

        self.lbl = QLabel("42", self)
        self.configWidget(self.lbl)
        self.configWidget(self.canvas)


@register_node(OUTPUT_PLOT_GP)
class GP_plot_Output(CalcNode):
    icon = "icons/out.png"
    op_code = OUTPUT_PLOT_GP
    op_title = "OUTPUT_PLOT_GP"
    content_label_objname = "OUTPUT_PLOT_GP"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1,1], outputs=[])

    def initInnerClasses(self):
        self.content = OutputPlotGPContent(self)
        self.grNode = MatplotlibGraphicsNode(self)

    def add_newaxis(self,array):
        if len(array.shape)<=1:
            return array[:, np.newaxis]
        return array


    def evalImplementation(self,param):
        x_input = self.getInput(0)
        y_input = self.getInput(1)

        # if not input_node:
        #     self.grNode.setToolTip("Input is not connected")
        #     self.markInvalid()
        #     return
        #
        # x = x_input.eval({})
        socket2 =self. getInputSocket(1)

        y = y_input.eval({"a":socket2})





        if  y is None:
            self.grNode.setToolTip("Input is NaN")
            self.markInvalid()
            return

        rng = np.random.RandomState(6)
        X = rng.uniform(0, 50, 12)
        X=self.add_newaxis(X)

        X_ = np.linspace(0, 50, 100)
        X_=self.add_newaxis(X_)
        model=

        y_mean, y_std = model.predict(X_[:, np.newaxis], return_std=True)

        plt.plot(X_, y_mean, 'k', lw=3, zorder=9)
        plt.fill_between(X_, y_mean - y_std, y_mean + y_std,
                         alpha=0.2, color='k')

        y_samples = model.sample_y(X_[:, np.newaxis], 10)

        plt.plot(X_, y_samples, lw=1)
        plt.scatter(X[:, 0], y, c='r', s=50, zorder=10, edgecolors=(0, 0, 0))
        plt.xlim(0, 50)
        plt.ylim(-6, 6)
        plt.title("Posterior (kernel: %s)\n Log-Likelihood: %.3f"
                  % (model.kernel_, model.log_marginal_likelihood(model.kernel_.theta)),
                  fontsize=12)









        ax =self.content.figure.add_subplot(111)
        x = np.linspace(0, 100, y.shape[0])
        # y = np.random.random(40)
        ax.cla()  # TODO:删除原图，让画布上只有新的一次的图
        ax.plot(x, y)
        self.content.canvas.draw()  # TODO:这里开始绘制

        # self.content.lbl.setText("%d" % val)
        self.markInvalid(False)
        self.markDirty(False)
        self.grNode.setToolTip("")

        return 0