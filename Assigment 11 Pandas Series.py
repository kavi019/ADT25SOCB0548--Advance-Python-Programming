import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.randint(50, 100, 5)
s = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

print(s)