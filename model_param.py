import joblib
import numpy as np


# defing model to predict based on our saved model


def model_load_cancer(variables):

    if variables[-1] == 'hidden':
        return "Please Enter the Zip Code of Patient's First!!!!"
    # loading model
    elif (variables[0] == '') or (variables[3] == '') or (variables[5] == ''):
        return "Please First Enter the Zip Code And All Above Information !!!!"
    else:
        final_variables = [variables]
        trained_model = joblib.load('model_cancer.pkl')
        prediction = trained_model.predict(final_variables)
        if prediction == [0]:
            return "There is very low chance of having cancer"
        elif prediction == [1]:
            return "There is medium chance of having cancer"
        else:
            return "There is very high chance of having cancer"


def model_load_asthma(variables):
    # using standardscaler for transformation
    if variables[1] == 'hidden':
        return "Please Enter the Zip Code of Patient's First!!!"
    else:
        scaler = joblib.load('scaler_asthma.pkl')
        X_scaler = scaler.transform([variables])

        test_data = scaler.transform(X_scaler)
        trained_model = joblib.load('model_asthma.pkl')
        prediction = trained_model.predict(test_data)
        prediction = round(prediction[0], 2)
        return f'Emergency department visit rate: {prediction}'
