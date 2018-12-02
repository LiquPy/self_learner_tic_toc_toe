import pandas as pd
import pickle
from sklearn.neural_network import MLPRegressor

training_data = pd.read_csv('training_data.csv', header=None, nrows=10000)

x = training_data.iloc[:, :-1]
y = training_data.iloc[:, -1]


model = MLPRegressor(alpha=1e-5, solver= 'adam',
                      hidden_layer_sizes=(128, 128), random_state=1)

model.fit(x, y)
with open('pickled_model.pkl', 'wb') as file:
    pickle.dump(model, file)

import numpy as np
test_x = np.array([0,0,0,0,0,0,0,0,0,0,0]).reshape(1,-1)
print(model.predict(test_x))

test_x = np.array([0,0,0,0,2,0,0,2,0,0,0]).reshape(1,-1)
print(model.predict(test_x))

test_x = np.array([0,0,0,0,2,0,0,2,0,0,1]).reshape(1,-1)
print(model.predict(test_x))

test_x = np.array([0,1,1,2,2,1,2,0,0,0,0]).reshape(1,-1)
print(model.predict(test_x))
