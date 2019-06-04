from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline

(X_train, y_train), (X_test, y_test) = mnist.load_data()

test_img = X_train[1]

plt.subplot(221)

plt.imshow(test_img, cmap=plt.get_cmap("gray"))

test_img[test_img>0] = 255

plt.imshow(test_img, cmap=plt.get_cmap("gray"))
y,x = np.nonzero(test_img)


x = x - np.mean(x)
y = y - np.mean(y)



coords = np.vstack([x,y])
#
cov_mat = np.cov(coords)
#
eval, evec = np.linalg.eig(cov_mat)
#
sort_indices = np.argsort(eval)[::-1]
#
x_v1, y_v1 = evec[:, sort_indices[0]]  # Eigenvector with largest eigenvalue
x_v2, y_v2 = evec[:, sort_indices[1]]



scale = 20
plt.imshow(test_img)
plt.show()
plt.plot([x_v1*-eval[sort_indices[0]], x_v1*eval[sort_indices[0]]],
         [y_v1*-eval[sort_indices[0]], y_v1*eval[sort_indices[0]]], color='red')
plt.plot([x_v2*-eval[sort_indices[1]], x_v2*eval[sort_indices[1]]],
         [y_v2*-eval[sort_indices[1]], y_v2*eval[sort_indices[1]]], color='blue')
# plt.plot(x, y, 'k.')
plt.axis('equal')
plt.gca().invert_yaxis()  # Match the image system with origin at top left
plt.show()

theta = np.tanh((x_v1)/(y_v1))
rotation_mat = np.matrix([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
transformed_mat = rotation_mat * coords
# plot the transformed blob
x_transformed, y_transformed = transformed_mat.A
plt.plot(x_transformed, y_transformed, 'g.')
