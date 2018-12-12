import pandas as pd
import pickle
import numpy as np

# ******* IF this is the first time learning: *******
from sklearn.neural_network import MLPRegressor

##training_data = pd.read_csv('training_data_1.csv', header=None)
##
##x = training_data.iloc[:, :-1]
##y = training_data.iloc[:, -1]

model = MLPRegressor(hidden_layer_sizes=(15, 15), random_state=1, verbose=100)


# ******* Otherwise (re-learning) *********
# load pickeled model
##with open('pickled_model.pkl', 'rb') as file:
##    model = pickle.load(file)

for i in range(1, 81):
    # load training data
    training_data = pd.read_csv('training_datasets/training_data_{}.csv'.format(i), header=None)
    x = training_data.iloc[:, :-1]
    y = training_data.iloc[:, -1]

    # (re)train model
    model.partial_fit(x, y)

    # see how results are changing with more learning
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
    print('------------------------')



# dump pickled model
with open('pickled_model.pkl', 'wb') as file:
    pickle.dump(model, file)


