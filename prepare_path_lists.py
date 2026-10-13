import os
import numpy as np

# 根目录
root_path = 'Dataset'

# 确保目录存在
os.makedirs(os.path.join(root_path, 'image', '1'), exist_ok=True)
os.makedirs(os.path.join(root_path, 'wrench', '1'), exist_ok=True)

# 创建图像路径列表
image_paths = []
wrench_paths = []

for i in range(1, 11):
    # 图像路径
    image_path = os.path.abspath(os.path.join(root_path, 'image', '1', f'{i}.png'))
    image_paths.append(image_path)
    
    # 力数据路径
    wrench_path = os.path.abspath(os.path.join(root_path, 'wrench', '1', f'{i}_norm.npy'))
    wrench_paths.append(wrench_path)

# 保存路径列表
np.save(os.path.join(root_path, 'test_images.npy'), np.array(image_paths))
np.save(os.path.join(root_path, 'test_wrench.npy'), np.array(wrench_paths))

print('路径列表文件创建完成！')
print(f'已创建 test_images.npy，包含 {len(image_paths)} 个图像路径')
print(f'已创建 test_wrench.npy，包含 {len(wrench_paths)} 个力数据路径')

# 打印生成的路径
print('\n生成的图像路径：')
for path in image_paths:
    print(path)

print('\n生成的力数据路径：')
for path in wrench_paths:
    print(path)