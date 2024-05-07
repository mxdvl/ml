import numpy as np

# one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
# print(one_dimensional_array)

# two_dimensional_array = np.array([[6,5],[11,7], [4,8]])
# print(two_dimensional_array)

# print(np.zeros((12, 3)))

# print(np.arange(5, 12))

# print(np.random.randint(low=50, high=101, size=(6,)))

# print(np.random.random(6))
# print(np.random.random((6,3)))
# print(np.random.random(size=(6,)) + 9)

# -------- #
# Task 1
# -------- #

feature = np.arange(6,20+1)
print(feature)
label = (feature * 3) + 4
print(label)
noise = np.random.random(label.size) * 4 - 2
print(noise)
noisy = label + noise
print(noisy)
