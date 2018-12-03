import pandas as pd
import pickle
from sklearn.neural_network import MLPRegressor

training_data = pd.read_csv('training_data.csv', header=None)

x = training_data.iloc[:, :-1]
y = training_data.iloc[:, -1]


model = MLPRegressor(hidden_layer_sizes=(15, 15), random_state=1)

model.fit(x, y)
with open('pickled_model.pkl', 'wb') as file:
    pickle.dump(model, file)

import numpy as np
# expected score = lowest
test_x = np.array([0,0,0,0,0,0,0,0,0,0,0]).reshape(1,-1)
print(model.predict(test_x))

# expected score = low
test_x = np.array([0,0,0,0,2,0,0,2,0,0,0]).reshape(1,-1)
print(model.predict(test_x))

# expected score = high
test_x = np.array([0,0,0,0,2,0,1,2,0,0,1]).reshape(1,-1)
print(model.predict(test_x))

# expected score = highest
test_x = np.array([0,1,1,2,2,1,2,0,0,0,0]).reshape(1,-1)
print(model.predict(test_x))
