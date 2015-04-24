import cvxpy as cvx
import numpy as np

def foo(a):
    """ A simple optimization problem.

    Parameters
    ----------
    a : float
        The bound on the ``x`` values

    Returns
    -------
    numpy.array
        The value of x


    """

    x = cvx.Variable(4)
    p = cvx.Problem(cvx.Maximize(sum(x)), [x <= 1])
    p.solve()

    return np.array(x.value).flatten()
