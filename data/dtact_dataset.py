import cv2
import numpy as np
from torch.utils.data import Dataset


class DTactDataset(Dataset): # 定义DTact数据集类
    def __init__(self, mode='train', root_path='../Dataset', image_type='RGB',
                 test_object=False, mixed_image=True) -> None: # 初始化数据集
        super().__init__() # 调用父类的初始化方法
        self.mode = mode # 数据集模式，train或test
        self.image_type = image_type # 图像类型，RGB或GRAY
        self.mixed_image = mixed_image # 是否使用混合图像
        if mode == 'train': # 如果是训练集
            if test_object: 
                if mixed_image:
                    self.images = np.load(root_path + '/train_mixed_images_object.npy')
                else:
                    self.images = np.load(root_path + '/train_images_object.npy')
                self.wrenches = np.load(root_path + '/train_wrench_object.npy')
            else:
                if mixed_image:
                    self.images = np.load(root_path + '/train_mixed_images.npy')
                else:
                    self.images = np.load(root_path + '/train_images.npy')
                self.wrenches = np.load(root_path + '/train_wrench.npy')
        else:
            if test_object:
                if mixed_image:
                    self.images = np.load(root_path + '/test_mixed_images_object.npy')
                else:
                    self.images = np.load(root_path + '/test_images_object.npy')
                self.wrenches = np.load(root_path + '/test_wrench_object.npy')
            else:
                if mixed_image:
                    self.images = np.load(root_path + '/test_mixed_images.npy')
                else:
                    self.images = np.load(root_path + '/test_images.npy')
                self.wrenches = np.load(root_path + '/test_wrench.npy')

    def __len__(self): # 返回数据集的长度
        return len(self.images)

    def __getitem__(self, index):   # 获取单个数据样本
        image_path = self.images[index]  # 获取图像路径
        image = cv2.imread(image_path).astype('float32') # 读取图像并转换为浮点数
        if self.image_type != 'RGB': # 如果图像类型不是RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 转换为灰度图像
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR) # 转换为3通道图像
        image = image.transpose([2, 0, 1]) # 转换为CHW格式
        force_path = self.wrenches[index] # 获取力路径
        force = np.load(force_path) # 读取力
        if self.mode == 'train': # 如果是训练集
            return image, force
        else:
            return image, force, image_path # 如果是测试集，返回图像、力和图像路径


if __name__ == '__main__': # 主函数
    dataset_path = '../Dataset' # 数据集路径
    dataset = DTactDataset(mode='train', root_path=dataset_path) # 创建训练集数据集
    print(dataset.__len__()) # 打印训练集数据集的长度
    for i in range(dataset.__len__()): # 遍历训练集数据集
        print(dataset.__getitem__(i)[0]) # 打印第i个数据样本的图像
        print(dataset.__getitem__(i)[1]) # 打印第i个数据样本的力
       
