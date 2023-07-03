import joblib


def save_model(model, filename):
    ''' save model '''
    joblib.dump(model, filename)


def load_model(filename):
    ''' load model '''
    joblib.load(filename)