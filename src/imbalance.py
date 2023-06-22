# import modules
import pandas as pd
from clean import clean_data
from imblearn.under_sampling import RandomUnderSampler, TomekLinks, NearMiss
from imblearn.over_sampling  import RandomOverSampler, SMOTE
from imblearn.combine        import SMOTEENN, SMOTETomek


def balance_data(X, y, method='RUS'):
    ''' fix class imbalance '''

    if (method == 'RUS'):
        return RandomUnderSampler().fit_resample(X, y), RandomUnderSampler()
    elif (method == 'Tomek'):
        return TomekLinks().fit_resample(X, y), TomekLinks()
    elif (method == 'NearMiss'):
        return NearMiss().fit_resample(X, y), NearMiss()
    elif (method == 'ROS'):
        return RandomOverSampler().fit_resample(X, y), RandomOverSampler()
    elif (method == 'SMOTE'):
        return SMOTE().fit_resample(X, y), SMOTE()
    elif (method == 'SMOTEENN'):
        return SMOTEENN().fit_resample(X, y), SMOTEENN()
    elif (method == 'SMOTETomek'):
        return SMOTETomek().fit_resample(X, y), SMOTETomek()


if __name__() == '__main__':
    data = pd.read_csv('../../data/ai4i2020.csv', index_col='UDI')

    data = clean_data(data)

    X = data.copy()
    y = X.pop('Machine failure')

    data_bal, _ = balance_data(X, y)
    X_b, y_b = data_bal

    y_b.value_counts().plot(kind='bar')