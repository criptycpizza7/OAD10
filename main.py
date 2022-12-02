from funcs import *

assert round(l1_norm(y_pred, y_ans), 1) == 1.1, 'Не верно реализован расчёт'

assert round(l2_norm(y_pred, y_ans), 3) == 0.43, 'Не верно реализован расчёт'


print("L1 = " + str(l1_norm(y_pred, y_ans)))
print("L2 = " + str(l2_norm(y_pred, y_ans)))

np.random.seed(777)
Z = np.random.randint(0, 5, (6, 5))
Z_eq = np.array((np.ones(5), np.zeros(5)))
Z = np.vstack((Z, Z_eq))
print(Z)

print("Equal items rows: \n", non_unique(Z))