import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[17.76],[18.22],[18.97],[19.55],[22.89],[23.0],[23.49],[24.10]])
y = np.array([0,0,0,0,1,1,1,1])

model = LinearRegression()
model.fit(x, y)

print("Done")
