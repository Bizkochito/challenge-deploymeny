from joblib import  load


def load_model():
    return load('model/linreg_model.joblib')

if __name__=='__main__':
    print(load_model().coef_)