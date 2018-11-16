import numpy as np

# Dataset is defined as: 

# Mass (kg), 
# surface area (km^2), 
# number of moons, 
# rotationtime (approx. in days), 
# albedo (%), 
# min temperature (Celcius at surface), 
# max temperature (Celcius at surface), 
# gravitational acceleration at surface (m/s^2), 
# HAS ATMOSPHERE? (1 yes, 0 no)

dataset = [[3.302e+23, 7.5e+7, 0, 59, 10, -183, 427, 3.701, 0]          # Mercury
           ,[4.8685e+24, 4.6e+8, 0, 117, 65, -45, 500, 8.870, 1]        # Venus
           ,[5.97223e+24, 510e+6, 1, 1, 36.7, -89.2, 56.7, 9.82, 1]     # Earth
           ,[6.4185e+23, 1.45e+8, 2, 1, 15, -140, 20, 3.690, 1]         # Mars
           ,[1.899e+27, 6.14e+10, 79, 0.375, 52, -121, -121, 23.120, 1] # Jupiter
           ,[5.6846e+26, 4.27e+10, 62, 0.46, 47, -130, -130, 8.960, 1 ] # Saturn
           ,[1.0243e+26, 7.62e+9, 14, 0.66, 41, -220, -220, 11.150, 1]  # Neptun
           ,[8.6832e+25, 8.08e+9, 27, 0.7, 51, -205, -205, 8.690, 1]    # Uranus
           ]


def sigmoid(x):
    return 1.0/ (1.0 + np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

w_1 = np.random.normal()
w_2 = np.random.normal()
w_3 = np.random.normal()
w_4 = np.random.normal()
w_5 = np.random.normal()
w_6 = np.random.normal()
w_7 = np.random.normal()
w_8 = np.random.normal()
b = np.random.normal()


learning_rate = 0.2
iterations = 1000

for i in range(0,iterations):

    picked = np.random.randint(0,len(dataset))

    z = dataset[picked][0]*w_1+dataset[picked][1]*w_2+dataset[picked][2]*w_3+dataset[picked][3]*w_4+dataset[picked][4]*w_5+dataset[picked][5]*w_6+dataset[picked][6]*w_7+dataset[picked][7]*w_8+b
    print("z : " + str(z))
    prediction = sigmoid(z)


    cost = np.square(prediction-dataset[picked][8])
    #print(cost)

    # Back propagation started on cost function all the way to the weighs that needs to be changed.
    d_cost_dpred = 2*(prediction-dataset[picked][8])
    d_pred_dz = sigmoid_prime(z)
    print("partial deriviative of pred on z" + str(d_pred_dz))
    d_z_dw1 = dataset[picked][0]
    d_z_dw2 = dataset[picked][1]
    d_z_dw3 = dataset[picked][2]
    d_z_dw4 = dataset[picked][3]
    d_z_dw5 = dataset[picked][4]
    d_z_dw6 = dataset[picked][5]
    d_z_dw7 = dataset[picked][6]
    d_z_dw8 = dataset[picked][7]
    d_z_b = 1

    print("d_cost_dpred: " + str(d_cost_dpred) + " d_pred_dz: " + str(d_pred_dz) + " d_z_dw1: " + str(d_z_dw1))
    d_cost_dw1 = d_cost_dpred * d_pred_dz * d_z_dw1
    d_cost_dw2 = d_cost_dpred * d_pred_dz * d_z_dw2
    d_cost_dw3 = d_cost_dpred * d_pred_dz * d_z_dw3
    d_cost_dw4 = d_cost_dpred * d_pred_dz * d_z_dw4
    d_cost_dw5 = d_cost_dpred * d_pred_dz * d_z_dw5
    d_cost_dw6 = d_cost_dpred * d_pred_dz * d_z_dw6
    d_cost_dw7 = d_cost_dpred * d_pred_dz * d_z_dw7
    d_cost_dw8 = d_cost_dpred * d_pred_dz * d_z_dw8
    d_cost_db = d_cost_dpred * d_pred_dz * d_z_b

    #print("w1: " + str(w_1) + "d_cost_dw5: " + str(d_cost_dw1))
    w_1 = w_1 - learning_rate * d_cost_dw1
    #print("w1 after operation: " + str(w_1))
    w_2 = w_2 - learning_rate * d_cost_dw2
    w_3 = w_3 - learning_rate * d_cost_dw3
    w_4 = w_4 - learning_rate * d_cost_dw4
    w_5 = w_5 - learning_rate * d_cost_dw5
    w_6 = w_6 - learning_rate * d_cost_dw6
    w_7 = w_7 - learning_rate * d_cost_dw7
    w_8 = w_8 - learning_rate * d_cost_dw8
    b = b - learning_rate * d_cost_db


def atmosphereCheck(planet):
    z = w_1 * planet[0] + w_2 * planet[1] + w_3 * planet[2] + w_4 * planet[3] + w_5 * planet[4] + w_6 * planet[5] + w_7 * planet[6] + w_8 * planet[7]+ b
    pred = sigmoid(z)
    if (pred < 0.5):
        return "The planet is predicted to HAVE an atmosphere"
    else:
        return "The planet is predicted to not have an atmosphere"

#print(atmosphereCheck([7.349e+22, 3.39e+7, 0, 27, 0.12, -233, 123, 1.62]))
#print(atmosphereCheck([3.302e+23, 7.5e+7, 0, 59, 10, -183, 427, 3.701]))