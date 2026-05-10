from capytale.autoeval import (
        ValidateVariables,
        ValidateFunction,
        ValidateFunctionPretty,
)

import numpy as np


test_fonction_f = ValidateFunctionPretty(
    "difference", x_pas_10, valid_function=lambda x:0
)
