# import modules
import pandas as pd


def clean_data(data, drop_type=True, encode_mf=False, multi=False):
    ''' clean the data '''

    data = data.copy()

    # drop column
    if drop_type:
        data.drop(columns='Type', inplace=True)

    # drop duplicates
    data.drop_duplicates(inplace=True)

    if encode_mf:
        # needs improvement because of multiple failure modes
        # from itertools import combinations, permutations
        # failures = ['TWF', 'HDF', 'PWF', 'OSF', 'RNF']
        # list(permutations(failures, 2))
        data['Machine failure'] = 0
        data['Machine failure'][data['TWF'] == 1] = 1
        data['Machine failure'][data['HDF'] == 1] = 2
        data['Machine failure'][data['PWF'] == 1] = 3
        data['Machine failure'][data['OSF'] == 1] = 4
        data['Machine failure'][data['RNF'] == 1] = 5

    if multi:
        data.drop(columns=['Product ID', 'Machine failure'], inplace=True)
    else:
        data.drop(columns=['Product ID', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'], inplace=True)

    return data


if __name__ == '__main__':
    data = pd.read_csv('../../data/ai4i2020.csv', index_col='UDI')

    print(clean_data(data, drop_type=True, encode_mf=False))