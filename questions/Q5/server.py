import random
import numpy as np
import prairielearn as pl


def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(5, 10)
    b = random.randint(5, 10)

    # Put these two integers into data['params']
    data["params"]["a"] = a
    data["params"]["b"] = b

    # Compute the sum of these two integers
    c = a + b

    # Put the sum into data['correct_answers']
    mat = np.random.random((1,5))
    data["correct_answers"]["OutputList1"] = pl.to_json(mat)
