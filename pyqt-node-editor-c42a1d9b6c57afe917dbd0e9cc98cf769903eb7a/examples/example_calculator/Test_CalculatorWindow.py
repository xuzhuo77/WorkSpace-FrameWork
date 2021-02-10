from examples.example_calculator.calc_window import CalculatorWindow






class Test_CalculatorWindow(CalculatorWindow):
    def addTestNodes(self):
        from examples.example_calculator.nodes.neighbors import  KNeighborsClassifierNode_Fit
        currentwidget=self.getCurrentNodeEditorWidget()
        node1 = KNeighborsClassifierNode_Fit(currentwidget.scene)

        node1.setPos(-350, -250)
