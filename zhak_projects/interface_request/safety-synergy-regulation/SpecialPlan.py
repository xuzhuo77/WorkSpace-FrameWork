from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IspecialPlanDetailListSave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialPlanDetailListSave")


class IspecialPlanDetailListLogicalDelete(InterfaceX):
    def __init__(self, parent, id):
        InterfaceX.__init__(self, parent)
        self.init("specialPlanDetailListLogicalDelete", param=id)


class IplanEvaluationRulesSave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("planEvaluationRulesSave")


class IplanEvaluationRulesList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("planEvaluationRulesList")


class IplanEvaluationScoreSave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("planEvaluationScoreSave")


class IplanEvaluationScoreList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("planEvaluationScoreList")


class IplanEvaluationScoreStatsList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("planEvaluationScoreStatsList")


class IspecialPlanDetailListRecover(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialPlanDetailListRecover")


class IspecialScreenDisplay(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialScreenDisplay")


class SpecialPlan(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def specialPlanDetailListSave(self):
        return IspecialPlanDetailListSave(self)

    def specialPlanDetailListLogicalDelete(self, id):
        return IspecialPlanDetailListLogicalDelete(self, id)

    def planEvaluationRulesSave(self):
        return IplanEvaluationRulesSave(self)

    def planEvaluationRulesList(self):
        return IplanEvaluationRulesList(self)

    def planEvaluationScoreSave(self):
        return IplanEvaluationScoreSave(self)

    def planEvaluationScoreList(self):
        return IplanEvaluationScoreList(self)

    def planEvaluationScoreStatsList(self):
        return IplanEvaluationScoreStatsList(self)

    def specialPlanDetailListRecover(self):
        return IspecialPlanDetailListRecover(self)

    def specialScreenDisplay(self):
        return IspecialScreenDisplay(self)


doc_type = "specialPlan"
factory = SpecialPlan(doc_type)


# guid = '551dc77f-9cac-43c6-a305-c2dabadce406'
# checkLogGuid = "DC70E9EB-F158-3DAB-04AF-18400A9533B2"
def test_list():
    ilist = factory.list()
    # ilist.payload = {"yearStart":"2021","yearEnd":"2023"}
    # ilist.payload = {"rectifyStartTime":"2018-07-01 00:00:00","rectifyEndTime":"2018-08-20 00:00:00"}
    ilist().print()


# test_list()


# ------------------------------------------------------------------specialPlanDetailList
def test_specialPlanDetailList_Save():
    specialPlanDetailListSave = factory.specialPlanDetailListSave()
    specialPlanDetailListSave.payload = {
        "specialPlan": {"name": 123},
        "specialPlanDetails": [{
            "name": "123tt"
        }]
    }
    specialPlanDetailListSave()


def test_specialPlanDetailList_Delete():
    specialPlanDetailListLogicalDelete = factory.specialPlanDetailListLogicalDelete(1291983385615638530)
    specialPlanDetailListLogicalDelete()


# test_list()

# test_specialPlanDetailList_Save()
# ----------------------------------------------------------------------------------------------planEvaluation

def test_planEvaluationRules_Save(param):
    planEvaluationRulesSave = factory.planEvaluationRulesSave()
    planEvaluationRulesSave.payload = {
        "weightPlanComplated": 3,
        "weightRectification": 2,
        "specialPlanEvaluations": param}
    planEvaluationRulesSave()


def test_planEvaluationRules_List():
    planEvaluationRulesList = factory.planEvaluationRulesList()
    planEvaluationRulesList.payload = {}
    data = planEvaluationRulesList()
    data.print()
    return data.pure()


def test_planEvaluationScore_Save(param):
    planEvaluationScoreSave = factory.planEvaluationScoreSave()
    planEvaluationScoreSave.payload = {
        "specialPlanEvaluations": param}
    planEvaluationScoreSave()


def test_planEvaluationScore_List():
    planEvaluationScoreList = factory.planEvaluationScoreList()
    planEvaluationScoreList.payload = {}
    data = planEvaluationScoreList()
    data.print()
    return data.pure()


def rule_score_show_save():
    data = test_planEvaluationRules_List()
    # test_planEvaluationRules_Save(data)


def score_show_save():
    data = test_planEvaluationScore_List()
    test_planEvaluationScore_Save(data)


def score_planEvaluationScoreStatsList():
    planEvaluationScoreStatsList = factory.planEvaluationScoreStatsList()
    planEvaluationScoreStatsList.payload = {
    }
    planEvaluationScoreStatsList().print()


# rule_score_show_save()
# score_show_save()
# score_planEvaluationScoreStatsList()


def test_planRecover():
    id = 1298082603680743425
    specialplanGet = factory.get()
    specialplanGet(id).print()

    specialPlanDetailListRecover = factory.specialPlanDetailListRecover()
    specialPlanDetailListRecover.payload = {
        "id": id,
        "deleteTime": "2020-08-25 10:19:43",
        # "deleteBy":""
    }
    specialPlanDetailListRecover().print()

    specialplanGet = factory.get()
    specialplanGet(id).print()


# print(2/3*0.6*30)
def test_specialScreenDisplay():
    specialScreenDisplay = factory.specialScreenDisplay()
    specialScreenDisplay.payload = {"year":2020}
    # ilist.payload = {"rectifyStartTime":"2018-07-01 00:00:00","rectifyEndTime":"2018-08-20 00:00:00"}
    specialScreenDisplay().print()


# test_planRecover()
test_specialScreenDisplay()
