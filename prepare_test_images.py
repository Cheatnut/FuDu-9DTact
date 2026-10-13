import os
import shutil
from PIL import Image

# 源图像路径
source_image = 'force_estimation/test.png'

# 目标目录
target_dir = 'Dataset/image/1/'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 复制图像10次
for i in range(1, 11):
    target_path = os.path.join(target_dir, f'{i}.png')
    # 使用shutil复制文件
    shutil.copy2(source_image, target_path)
    print(f'已复制图像到: {target_path}')

print('\n测试图像准备完成!')
print(f'已在 {target_dir} 目录中创建了10张测试图像')