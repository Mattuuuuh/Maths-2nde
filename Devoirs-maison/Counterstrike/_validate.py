from capytale.autoeval import (
        ValidateVariables,
        ValidateFunction,
        ValidateFunctionPretty,
)

import numpy as np

def sin(x):
    return np.sin(np.deg2rad(x))

def cos(x):
    return np.cos(np.deg2rad(x))

def arctan(x):
    return np.rad2deg(np.arctan(x))

def true_function(OA, OB):
    return lambda x: arctan(OB*sin(x)/(OA-OB*cos(x)))

x_pas_10 = np.arange(0,90,10)
x_pas_5 = np.arange(0,90,5)
x_pas_1 = np.arange(0,90,1)
x = np.arange(0,90,.1)

test_x_pas_10 = ValidateVariables({"x_pas_10":x_pas_10})
test_x_pas_5 = ValidateVariables({"x_pas_5":x_pas_5})
test_x_pas_1 = ValidateVariables({"x_pas_1":x_pas_1})
test_x = ValidateVariables({"x":x})

test_fonction_sinus = ValidateFunctionPretty(
    "sin", x_pas_10, valid_function=sin
)
test_fonction_f = ValidateFunctionPretty(
    "difference", x_pas_10, valid_function=lambda x:0
)
