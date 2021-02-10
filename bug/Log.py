from SingleInstance import SingleInstance


@SingleInstance
class Log():
    logSwitch = 1

    @classmethod
    def show(self, abc):
        if self.logSwitch == 1:
            print(abc)

    def set_close(self):
        self.logSwitch = 0

    def set_open(self):
        self.logSwitch = 1

# @SingleInstance
# class TestLog():
#     logSwitch = 1
#
#     @classmethod
#     def show(self, abc):
#         if self.logSwitch == 1:
#             print(abc)
#
#     def set_close(self):
#         self.logSwitch = 0
#
#     def set_open(self):
#         self.logSwitch = 1