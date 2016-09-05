import numpy.linalg as la
import numpy as np


def assertLinEq(a, b, c):
    print a,b
    print la.solve(a, b)
    assert np.allclose(la.solve(a, b), c)


def assertRaises(a, b):
    try:
        la.solve(a, b)
    except la.linalg.LinAlgError as e:
        print e
        assert True
    else:
        assert False

# A.1.6
print("a")
a = np.array([[1,1,2], [-1,-2,3], [3,-7,4]])
b = np.array([8,1,10])
assertLinEq(a,b,(3,1,2))

print("b")           
a = [[2,-3, 0], [2,1,0], [3,2,0]]
b = [-2,1,1]
assertRaises(a,b)
#print la.solve(a,b)

print("c")
a = np.array([[2,2,2], [-2,5,2], [8,1,4]])
b = np.array([0,1,-1])
assertRaises(a,b)
