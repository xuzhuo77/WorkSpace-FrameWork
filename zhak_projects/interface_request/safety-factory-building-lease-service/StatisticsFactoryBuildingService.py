from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IapprovalStats(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("approvalStats")


class IareaStatsDrill(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("areaStatsDrill")


class IindustyDistributionLessor(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("industyDistributionLessor")


class IindustyDistributionLessee(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("industyDistributionLessee")


class IregionDistributionDrill(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("regionDistributionDrill")


class IindustyDistributionLesseeDrilling(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("industyDistributionLesseeDrilling")


class StatisticsFactoryBuilding(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def approvalStats(self):
        return IapprovalStats(self)

    def industyDistributionLessor(self):
        return IindustyDistributionLessor(self)

    def industyDistributionLessee(self):
        return IindustyDistributionLessee(self)

    def areaStatsDrill(self):
        return IareaStatsDrill(self)

    def regionDistributionDrill(self):
        return IregionDistributionDrill(self)

    def industyDistributionLesseeDrilling(self):
        return IindustyDistributionLesseeDrilling(self)


doc_type = "statisticsFactoryBuilding"
factory = StatisticsFactoryBuilding(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


def test_approvalStats():
    ilist = factory.approvalStats()
    ilist.payload = {"regionIds":-1}
    ilist().print()


def test_industyDistributionLessor():
    ilist = factory.industyDistributionLessor()
    # ilist.payload = {"regionIds":320509102000}
    ilist().print()


def test_industyDistributionLessee():
    ilist = factory.industyDistributionLessee()
    # ilist.payload = {"regionIds":320509102000}
    ilist().print()


def test_areaStatsDrill():
    ilist = factory.areaStatsDrill()
    ilist.payload = {"regionIds": 320509103000}
    ilist().print()


def test_regionDistributionDrill():
    ilist = factory.regionDistributionDrill()
    ilist.payload = {"regionIds": -1}
    ilist().print()


def test_industyDistributionLesseeDrilling():
    ilist = factory.industyDistributionLesseeDrilling()
    ilist.payload = {"regionIds": -1}
    ilist().print()

# test_list()
test_approvalStats()
# test_industyDistributionLessor()
# test_industyDistributionLessee()
# test_areaStatsDrill()
# test_regionDistributionDrill()
# test_industyDistributionLesseeDrilling()
