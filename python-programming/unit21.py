#모두의 데이터과학 unit 21
import numpy as np
numbers = np.array(range(1,11), copy=True)
numbers

ones = np.ones([2, 4], dtype=np.float64)
ones

zeros = np.zeros([2, 4], dtype=np.float64)
zeros

empty = np.empty([2, 4], dtype=np.float64)
empty

eye = np.eye(3)
eye

np_numbers = np.arange(2, 5, 0.25)
np_numbers

sap = np.array(["MMM", "ABT", "ABBV", "ACN", "ACE", "ATVI", "ADBE", "ADT"])
sap

sap2d = sap.reshape(2, 4)
sap2d

sap3d = sap.reshape(2, 2, 2)
sap3d