import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import cv2
import yaml
import numpy as np
from estimator import Estimator

if __name__ == '__main__':
    # 加载配置
    current_dir = os.path.dirname(os.path.abspath(__file__))
    force_config_path = os.path.join(current_dir, "force_config.yaml")
    force_file = open(force_config_path, 'r+', encoding='utf-8')
    force_config = yaml.load(force_file, Loader=yaml.FullLoader)
    estimator = Estimator(force_config)
    
    # 加载测试图像路径
    test_images_path = os.path.join(current_dir, "../Dataset/test_images.npy")
    test_images = np.load(test_images_path)
    
    # 对每张图像进行推理
    print("="*50)
    print("Batch Inference Start!")
    print("="*50)
    for i, image_path in enumerate(test_images):
        
        print(f"Processing image {i+1}/{len(test_images)}: {image_path}")
        
        # 读取图像
        image = cv2.imread(image_path)
        
        # 转换为灰度图并创建表示
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 创建与传感器输出格式相同的表示
        representation = np.zeros_like(image)
        representation[::, ::, 0] = gray_image
        
        # 进行力估计
        force = estimator.predict_force(representation)
        
        # 打印结果
        print(f"Estimated force: {force}")
        print("-" * 50)


