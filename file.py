import numpy as np
from PIL import Image


def image_to_vector(src):
    img = Image.open(src).convert('RGB')to_vector('../testingData/img0.JPG
    arr = np.array(img)

    single_d_vector = arr.ravel()

    return single_d_vector


A = image_to_vector('../testingData/img0.JPG')
B = image_')
# A = np.array([10, 15, 3])
# B = np.array([10, 15, 3])

cos_sim = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
print(f"Cosine Similarity between A and B:{np.round(cos_sim, 2)}")
print(f"Cosine Distance between A and B:{np.round(1 - cos_sim, 2)}")

# convert it to a matrix
# vector = np.matrix(flat_arr)
#
# # do something to the vector
# vector[:, ::10] = 128
#
# # reform a numpy array of the original shape
# arr2 = np.asarray(vector).reshape(shape)
# print(arr2)
# # make a PIL image
# # img2 = Image.fromarray(arr2, 'RGBA')
# # img2.show()
