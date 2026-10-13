import os
import numpy as np

# 目标目录
target_dir = 'Dataset/wrench/1/'

# 确保目标目录存在
os.makedirs(target_dir, exist_ok=True)

# 力数据范围（从项目代码中获取）
wrench_range = [[-3, 3], [-3, 3], [-12, 0], [-0.2, 0.2], [-0.2, 0.2], [-0.05, 0.05]]
min_wrench = np.array([r[0] for r in wrench_range])
max_wrench = np.array([r[1] for r in wrench_range])
wrench_span = max_wrench - min_wrench

# 生成10个力数据文件
for i in range(1, 11):
    # 生成示例力数据（可以根据需要修改）
    # 这里使用固定值，实际应用中可能需要不同的值
    wrench = np.array([0.0, 0.0, -5.0, 0.0, 0.0, 0.0])
    
    # 保存原始力数据
    raw_path = os.path.join(target_dir, f'{i}.npy')
    np.save(raw_path, wrench)
    
    # 计算归一化力数据
    normalized_wrench = (wrench - min_wrench) / wrench_span
    
    # 保存归一化力数据
    norm_path = os.path.join(target_dir, f'{i}_norm.npy')
    np.save(norm_path, normalized_wrench)
    
    print(f'已创建力数据文件: {raw_path}')
    print(f'已创建归一化力数据文件: {norm_path}')

print('\n力数据文件准备完成！')
print(f'已在 {target_dir} 目录中创建了10组力数据文件')