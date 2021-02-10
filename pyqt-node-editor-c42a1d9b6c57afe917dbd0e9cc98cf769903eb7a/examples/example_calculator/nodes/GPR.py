from examples.example_calculator.calc_conf import *
from examples.example_calculator.calc_node_base import *
from examples.example_calculator.sklearn_node_base import SkLearnNode, SkLearnGraphicsNode
from sklearn.gaussian_process import GaussianProcessRegressor

from nodeeditor.node_content_widget import QDMNodeContentWidgetInnerLayout
from sklearn.gaussian_process.kernels import (RBF, Matern, RationalQuadratic,
                                              ExpSineSquared, DotProduct,
                                              ConstantKernel)

# kernel
# RBF
# RationalQuadratic
# ExpSineSquared
# ConstantKernel
# DotProduct
# Matern

kernelType = [
    "RBF",
    "RationalQuadratic",
    "ExpSineSquared",
    "ConstantKernel",
    "DotProduct",
    "Matern",
]


class GaussianProcessKernelsContent(QDMNodeContentWidgetInnerLayout):

    def initUI(self):
        self.cb_kernel = QComboBox()
        self.cb_kernel.addItems(kernelType)
        self.cb_kernel.setCurrentIndex(self.node.kernel_idx)
        self.cb_kernel.currentIndexChanged.connect(self.selectionchange)
        self.cb_kernel.setMaximumHeight(30)

        self.l_length_scale = QLabel("length_scale", self)
        self.l_length_scale_bounds = QLabel("length_scale_bounds", self)
        self.l_alpha = QLabel("alpha", self)
        self.l_periodicity = QLabel("periodicity", self)
        self.l_periodicity_bounds = QLabel("periodicity_bounds", self)
        self.l_constant_value = QLabel("constant_value", self)
        self.l_constant_value_bounds = QLabel("constant_value_bounds", self)
        self.l_sigma_0 = QLabel("sigma_0", self)
        self.l_sigma_0_bounds = QLabel("sigma_0_bounds", self)
        self.l_nu = QLabel("nu", self)

        self.configWidget(self.cb_kernel)

        self.configWidget(self.l_length_scale)
        self.configWidget(self.l_length_scale_bounds)
        self.configWidget(self.l_alpha)
        self.configWidget(self.l_periodicity)
        self.configWidget(self.l_periodicity_bounds)
        self.configWidget(self.l_constant_value)
        self.configWidget(self.l_constant_value_bounds)
        self.configWidget(self.l_sigma_0)
        self.configWidget(self.l_sigma_0_bounds)
        self.configWidget(self.l_nu)

        self.m_input_sockets[0] = self.l_length_scale
        self.m_input_sockets[1] = self.l_length_scale_bounds
        self.m_input_sockets[2] = self.l_alpha
        self.m_input_sockets[3] = self.l_periodicity
        self.m_input_sockets[4] = self.l_periodicity_bounds
        self.m_input_sockets[5] = self.l_constant_value
        self.m_input_sockets[6] = self.l_constant_value_bounds
        self.m_input_sockets[7] = self.l_sigma_0
        self.m_input_sockets[8] = self.l_sigma_0_bounds
        self.m_input_sockets[9] = self.l_nu



        self.m_output_sockets[0] = self.cb_kernel

    def selectionchange(self, i):
        self.node.kernel_idx = i


@register_node(GAUSSIANPROCESS_KERNELS)
class GaussianProcessKernels(SkLearnNode):
    icon = "icons/divide.png"
    op_code = GAUSSIANPROCESS_KERNELS
    op_title = "GaussianProcessKernel"
    content_label = "/"
    content_label_objname = "GaussianProcessKernel"

    length_scale = 1.0
    length_scale_bounds = (1e-1, 10.0)
    alpha = 0.1
    periodicity = 3.0
    periodicity_bounds = (1.0, 10.0)
    constant_value = 0.1
    constant_value_bounds = (0.01, 10.0)
    sigma_0 = 1.0
    sigma_0_bounds = (0.1, 10.0)
    nu = 1.5
    kernel_idx = 0

    def __init__(self, scene):
        super().__init__(scene, inputs=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], outputs=[2])

    def initInnerClasses(self):
        self.content = GaussianProcessKernelsContent(self)
        self.grNode = SkLearnGraphicsNode(self)

    def train(self, n_neighbors, x_data, y_data):
        if n_neighbors != self.n_neighbors:
            self.model = GaussianProcessRegressor(kernel=self.kernel)
            self.n_neighbors = n_neighbors
        self.model.fit(x_data, y_data)
        return self.model

    def _kernels(self, i):
        kernels = [1.0 * RBF(length_scale=self.length_scale, length_scale_bounds=self.length_scale_bounds),
                   1.0 * RationalQuadratic(length_scale=self.length_scale, alpha=self.alpha),
                   1.0 * ExpSineSquared(length_scale=self.length_scale, periodicity=self.periodicity,
                                        length_scale_bounds=self.length_scale_bounds,
                                        periodicity_bounds=self.periodicity_bounds),
                   ConstantKernel(constant_value=self.constant_value,
                                  constant_value_bounds=self.constant_value_bounds) * (
                               DotProduct(sigma_0=1.0, sigma_0_bounds=(0.1, 10.0)) ** 2),
                   1.0 * Matern(length_scale=self.length_scale, length_scale_bounds=self.length_scale_bounds,
                                nu=self.nu)]

        return kernels[i]

    def evalImplementation(self, param):

        length_scale_input = self.getInput(0)
        length_scale_bounds_input = self.getInput(1)
        alpha_input = self.getInput(2)
        periodicity_input = self.getInput(3)
        periodicity_bounds_input = self.getInput(4)
        constant_value_input = self.getInput(5)
        constant_value_bounds_input = self.getInput(6)
        sigma_0_input = self.getInput(7)
        sigma_0_bounds_input = self.getInput(8)
        nu_input = self.getInput(9)

        if length_scale_input is not None:
            self.length_scale = length_scale_input.eval({})
        if length_scale_bounds_input is not None:
            self.length_scale_bounds = length_scale_bounds_input
        if alpha_input is not None:
            self.alpha = alpha_input.eval({})
        if periodicity_input is not None:
            self.periodicity = periodicity_input.eval({})
        if periodicity_bounds_input is not None:
            self.periodicity_bounds = periodicity_bounds_input.eval({})
        if constant_value_input is not None:
            self.constant_value = constant_value_input.eval({})
        if constant_value_bounds_input is not None:
            self.constant_value_bounds = constant_value_bounds_input.eval({})
        if sigma_0_input is not None:
            self.sigma_0 = sigma_0_input.eval({})
        if sigma_0_bounds_input is not None:
            self.sigma_0_bounds = sigma_0_bounds_input.eval({})
        if nu_input is not None:
            self.nu = nu_input.eval({})

        x_Input = self.getInput(0)
        y_Input = self.getInput(1)

        socket1 = self.getInputSocket(0)
        socket2 = self.getInputSocket(1)
        # socket3 = self.getInputSocket(2)

        # val1=input_node1.eval({"a":socket1})
        # val2=input_node2.eval({"a":socket2})
        # if n_neighbors_Input is not None:
        #     self.n_neighbors=n_neighbors_Input.eval({})
        #     self.content.lbl.setText(str(self.n_neighbors))

        if x_Input is None or y_Input is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self._kernels(self.kernel_idx)
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val


class GaussianProcessRegressorContent(QDMNodeContentWidgetInnerLayout):

    def initUI(self):
        self.kernellbl = QLabel("keranl", self)

        self.xdatalbl = QLabel("X_data", self)
        self.ydatalbl = QLabel("Y_data", self)
        self.modellbl = QLabel("model", self)
        self.modellbl.setAlignment(Qt.AlignRight)

        self.configWidget(self.kernellbl)
        self.configWidget(self.xdatalbl)
        self.configWidget(self.ydatalbl)
        self.configWidget(self.modellbl)

        self.m_input_sockets[0] = self.kernellbl
        self.m_input_sockets[1] = self.xdatalbl
        self.m_input_sockets[2] = self.ydatalbl
        self.m_output_sockets[0] = self.modellbl


@register_node(GAUSSIANPROCESSREGRESSOR_FIT)
class GaussianProcessRegressor_Fit(SkLearnNode):
    icon = "icons/divide.png"
    op_code = GAUSSIANPROCESSREGRESSOR_FIT
    op_title = "GaussianProcessRegressor_fit"
    content_label = "/"
    content_label_objname = "GaussianProcessRegressor_node_fit"
    kernel = 1.0 * ExpSineSquared(length_scale=1.0, periodicity=3.0,
                                  length_scale_bounds=(0.2, 10.0),
                                  periodicity_bounds=(3.0, 6.0))
    model = GaussianProcessRegressor(kernel=kernel)

    def __init__(self, scene):
        super().__init__(scene, inputs=[1, 1, 1], outputs=[2])

    def initInnerClasses(self):
        self.content = GaussianProcessRegressorContent(self)
        self.grNode = SkLearnGraphicsNode(self)

    def train(self, x_data, y_data):
        if n_neighbors != self.n_neighbors:
            self.model = GaussianProcessRegressor(kernel=self.kernel)
        self.model.fit(x_data, y_data)
        return self.model

    def evalImplementation(self, param):

        x_Input = self.getInput(0)
        y_Input = self.getInput(1)

        socket1 = self.getInputSocket(0)
        socket2 = self.getInputSocket(1)
        # socket3 = self.getInputSocket(2)

        # val1=input_node1.eval({"a":socket1})
        # val2=input_node2.eval({"a":socket2})
        # if n_neighbors_Input is not None:
        #     self.n_neighbors=n_neighbors_Input.eval({})
        #     self.content.lbl.setText(str(self.n_neighbors))

        if x_Input is None or y_Input is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.train(x_Input.eval({"a": socket1}), y_Input.eval({"a": socket2}))
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val


@register_node(GAUSSIANPROCESSREGRESSOR_PREDICT)
class GP_Predict(SkLearnNode):
    icon = "icons/divide.png"
    op_code = GAUSSIANPROCESSREGRESSOR_PREDICT
    op_title = "GaussianProcessRegressor_predict"
    content_label = "/"
    content_label_objname = "GaussianProcessRegressor_node_predict"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1, 1], outputs=[2])

    def evalOperation(self, model, x_data):
        y_ = model.predict(x_data)
        return y_

    def predict(self, model, x_data):
        y_ = model.predict(x_data)
        return y_

    def evalImplementation(self, param):

        model_Input = self.getInput(0)
        x_data = self.getInput(1)

        socket1 = self.getInputSocket(0)
        socket2 = self.getInputSocket(1)

        # val1=input_node1.eval({"a":socket1})
        # val2=input_node2.eval({"a":socket2})

        if model_Input is None or x_data is None:
            self.markInvalid()
            self.markDescendantsDirty()
            self.grNode.setToolTip("Connect all inputs")
            return None

        else:
            val = self.predict(model_Input.eval({}), x_data.eval({"a": socket2}))
            self.value = val
            self.markDirty(False)
            self.markInvalid(False)
            self.grNode.setToolTip("")

            self.markDescendantsDirty()
            self.evalChildren()

            return val

# @register_node(KNEIGHBORSCLASSIFIER_NODE_SCORE)
# class KNeighborsClassifierNode_Score(SkLearnNode):
#     icon = "icons/divide.png"
#     op_code = KNEIGHBORSCLASSIFIER_NODE_SCORE
#     op_title = "KNN_score"
#     content_label = "/"
#     content_label_objname = "KNeighborsClassifier_node_score"
#     n_neighbors = 1
#
#     def __init__(self, scene):
#         super().__init__(scene, inputs=[1, 1, 1], outputs=[])
#
#     def evalOperation(self, model, y_data1, y_data2):
#         y_ = model.score(y_data1, y_data2)
#         return y_
#
#     def evalImplementation(self, param):
#         model_Input = self.getInput(0)
#         x_data = self.getInput(1)
#         y_data = self.getInput(2)
#
#         socket1 = self.getInputSocket(0)
#         socket2 = self.getInputSocket(1)
#         socket3 = self.getInputSocket(2)
#
#         # val1=input_node1.eval({"a":socket1})
#         # val2=input_node2.eval({"a":socket2})
#
#         if model_Input is None or x_data is None or y_data is None:
#             self.markInvalid()
#             self.markDescendantsDirty()
#             self.grNode.setToolTip("Connect all inputs")
#             return None
#
#         else:
#             val = self.evalOperation(model_Input.eval({}), x_data.eval({"a": socket2}), y_data.eval({"a": socket3}))
#             self.content.lbl.setText(str(val))
#             self.value = val
#             self.markDirty(False)
#             self.markInvalid(False)
#             self.grNode.setToolTip("")
#
#             self.markDescendantsDirty()
#             self.evalChildren()
#
#             return val
