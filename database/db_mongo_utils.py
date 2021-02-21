import json
import pandas as pd


def dataframe2dict(df):
    return json.loads(df.T.to_json()).values()


def dict2dataframe(data):
    return pd.DataFrame(list(data))


if __name__ == '__main__':
    left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                         'key2': ['K0', 'K1', 'K0', 'K1'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
    print(dataframe2dict(left))
    test_dict={"name":3,"age":4}
    print(dict2dataframe(test_dict))

