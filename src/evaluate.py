# import modules
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score, r2_score, recall_score, precision_score, f1_score, matthews_corrcoef


def evaluate_model(y_test, y_predictions):

    accuracy = accuracy_score(y_test, y_predictions)
    recall = recall_score(y_test, y_predictions, average='weighted')
    precision = precision_score(y_test, y_predictions, average='weighted')
    f1s = f1_score(y_test, y_predictions, average='weighted')
    # MCC = matthews_corrcoef(y_test, y_predictions)
    roc = roc_auc_score(y_test, y_predictions)

    return accuracy, recall, precision, f1s, roc # MCC, roc