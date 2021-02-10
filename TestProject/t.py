# from ServiceBasic import  ServiceBasic
# test_instance = type('MyShinyClass', (ServiceBasic,), {})() # returns a class object
# print(test_instance.a)
#

# print(MyShinyClass()) # create an instance with the class
from FakeDataService.FakeDataService import FakeDataService

FakeDataService().add_randomValue_by_entity()