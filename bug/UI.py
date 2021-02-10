class Button():
    name = ""
    trigger = None

    def __init__(self):
        pass

    def setFunc(self, func):
        self.trigger = func

    def button_own(self):
        self.trigger()


class Panel():
    _button_dict = {}
    name = ""
    target_animal = None

    def set_skill(self, button):
        self._button_dict[button] = len(self._button_dict) + 1

    def trigger(self, b1):
        if self.target_animal:
            self.target_animal.trigger_skill(self._button_dict[b1])

    def set_target(self, animal):
        self.target_animal = animal

    def return_skills(self):
        return self._button_dict.items()


class ButtonAddAnimal(Button):
    pass


class PanelAnimalCOntrol(Panel):
    def __init__(self, func):
        self.name = "animal_control"
        b = ButtonAddAnimal()
        b.setFunc(func)


class UI():
    _d1ict = {}
    i = 0

    def __init__(self):
        # p = PanelAnimalCOntrol()
        # self._add_panel(p)
        pass

    def _add_panel(self, panel):
        self._d1ict[panel.name] = panel
        self.i += 1


