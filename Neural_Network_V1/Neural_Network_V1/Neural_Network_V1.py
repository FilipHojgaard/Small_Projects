import numpy as np

#  This dataset contains: number of people in household, money for rent, have children? (0 for no, 1 for yes)
dataset = [[1, 4000, 0], [1, 3000, 0], [2, 5700, 0], [2, 7000, 1], [1, 8000, 1], [2, 12000, 1], [1, 6000, 0], [1, 7040, 1], [2, 14000, 1], [2, 15000, 0]]


def sigmoid(value):
    if -value > np.log(np.finfo(type(value)).max):
        return 0.0    
    a = np.exp(-value)
    return 1.0/ (1.0 + a)

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

w_1 = np.random.normal()
w_2 = np.random.normal()
b = np.random.normal()


learning_rate = 0.2
iterations = 100

for i in range(0,iterations):
    picked = np.random.randint(0,len(dataset))

    z = dataset[picked][0]*w_1+dataset[picked][1]*w_2+b

    prediction = sigmoid(z)


    cost = np.square(prediction-dataset[picked][2])

    print(cost)
    # Back propagation started on cost function all the way to the weighs that needs to be changed.
    d_cost_dpred = 2*(prediction-dataset[picked][2])
    d_pred_dz = sigmoid_prime(z)
    d_z_dw1 = dataset[picked][0]
    d_z_dw2 = dataset[picked][1]
    d_z_b = 1

    d_cost_dw1 = d_cost_dpred * d_pred_dz * d_z_dw1
    d_cost_dw2 = d_cost_dpred * d_pred_dz * d_z_dw2
    d_cost_db = d_cost_dpred * d_pred_dz * d_z_b

    w_1 = w_1 - learning_rate * d_cost_dw1
    w_2 = w_2 - learning_rate * d_cost_dw2
    b = b - learning_rate * d_cost_db

mystic_family = [2, 30090]
z = w_1 * mystic_family[0] + w_2 * mystic_family[1] + b
pred = sigmoid(z)
if (pred < 0.5):
    print("Family WITHOUT children predicted")
else:
    print("Family WITH children predicted")