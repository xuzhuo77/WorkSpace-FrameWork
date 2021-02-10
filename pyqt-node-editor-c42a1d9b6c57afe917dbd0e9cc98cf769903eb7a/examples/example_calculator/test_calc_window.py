from examples.example_calculator.calc_window import CalculatorWindow
class Test_CalculatorWindow(CalculatorWindow):

    def addTestNodes(self):
        from examples.example_calculator.nodes.neighbors import  KNeighborsClassifierNode_Fit
        currentwidget=self.getCurrentNodeEditorWidget()
        node1 = KNeighborsClassifierNode_Fit(currentwidget.scene)

        from examples.example_calculator.nodes.loop import LOOP_Output
        node2 = LOOP_Output(currentwidget.scene)

        from examples.example_calculator.nodes.GPR import GaussianProcessRegressor_Fit
        node3=GaussianProcessRegressor_Fit(currentwidget.scene)

        from examples.example_calculator.nodes.GPR import GaussianProcessKernels
        node4 = GaussianProcessKernels(currentwidget.scene)

        from examples.example_calculator.nodes.output import GP_plot_Output
        node5 = GP_plot_Output(currentwidget.scene)

        node1.setPos(-350, -250)
        node2.setPos(-150, -200)
        node3.setPos(50, -200)
        node4.setPos(150, -200)
        node5.setPos(250,-200)