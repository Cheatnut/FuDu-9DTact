import numpy as np
import os

# 创建图像路径列表
image_paths = []
wrench_paths = []
mixed_image_paths = []

for i in range(1, 11):
    image_path = os.path.abspath("Dataset/image/1/{}.png".format(i))
    image_paths.append(image_path)
    
    wrench_path = os.path.abspath("Dataset/wrench/1/{}_norm.npy".format(i))
    wrench_paths.append(wrench_path)
    
    mixed_image_path = os.path.abspath("Dataset/mixed_image/1/{}.png".format(i))
    mixed_image_paths.append(mixed_image_path)

# 保存路径列表
np.save("Dataset/test_images.npy", np.array(image_paths))
np.save("Dataset/test_wrench.npy", np.array(wrench_paths))
np.save("Dataset/test_mixed_images.npy", np.array(mixed_image_paths))