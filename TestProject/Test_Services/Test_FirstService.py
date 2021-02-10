from FirstService.FirstService import FirstService
from FirstService.First import First
import pytest
from Entity import Entity


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")

    request.addfinalizer(teardown_function)  # 此内嵌函数做teardown工作
    print('setup_function called.')
    # return "x"


@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")

    request.addfinalizer(teardown_module)
    print('setup_module called.')
    return "set module true"

# @pytest.mark.FirstSercice
def test_add(setup_module):
    first_service = FirstService()
    first = First(guid="testguid", address="xxx-xxx-xx")
    max_id = FirstService().find_id_max()
    assert first_service.create(first).id == max_id + 1


# @pytest.mark.FirstSercice
def test_find_id_max(setup_module):
    max_id = FirstService().find_id_max()
    assert max_id == max_id


# @pytest.mark.FirstSercice
def test_update(setup_module):
    first = First(id=988019, guid="testguid111")
    first = FirstService().update(first)
    assert first is None

    first = First(id=988019, version=25, guid="testguid111")
    first = FirstService().update(first)
    assert first is not None
    assert first.guid is "testguid111"


@pytest.mark.FirstSercice
def test_find_one(setup_module):
    query = {
        First.id == 988020,
        # First.version ==1,
        First.guid == "testguid",
    }
    entityone = FirstService().find_one(query)
    assert entityone is not None
    query = {
        First.id == 988020,
        First.version == 3,
        # First.guid == "testguid",
    }
    entityone = FirstService().find_one(query)
    assert entityone is  None

# first=Entity(id=987987,version=2,guid="testguid",)
# print(first)
# print(FirstService().find_list({}))
