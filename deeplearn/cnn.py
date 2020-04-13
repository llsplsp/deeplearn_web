import numpy as np
import tensorflow as tf
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

graph = tf.Graph()


# 写深度学习的代码
class deeper_model:
    with graph.as_default():
        # 定义占位符
        x = tf.placeholder(tf.float32, [None, 784])  # 保存的数据类型，保存数据的结构，比如要保存一个1×2的矩阵，则struct=[1,2]

        # 创建神经网络中间层
        W = tf.Variable(tf.zeros([784, 10]))  # 定义权重
        b = tf.Variable(tf.zeros([10]))  # 定义偏置

        # y=x*w+b 10分类

    # 权重函数，用于初始化
    def weight_variable(self, shape):
        initial = tf.truncated_normal(shape, stddev=0.1)  # 标准差 stddev用于设置正态分布被截断前的标准差，设置为0.1后，训练精度就达到达到 99.2% 以上
        return tf.Variable(initial)

    # 偏置，用于初始化
    def bias_variable(self, shape):
        initial = tf.constant(0.1, shape=shape)  # 创建常量initial，可设定形状。
        return tf.Variable(initial)

    # 卷积操作，步长为1，大小为1*1
    def conv2d(self, x, W):
        return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')  # 前后必须为1

    # 池化操作 tf.nn.max_pool()和tf.nn.avg_pool()
    def max_pool_2x2(self, x):
        return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # 槽函数--开始识别
    def startRecognize(self, new_img):
        with graph.as_default():
            # 读取图片
            or_img = cv2.imdecode(np.fromfile(new_img, dtype=np.uint8), 0)  # 解决中文路径问题
            img = cv2.resize(or_img, (28, 28))
            # print(img.shape)

            one_map = img.flatten()  # 将矩阵拉伸成一维的数组。
            tva = [(255 - x) * 1.0 / 255.0 for x in one_map]  # 将像素正常化为0和1

            # 1.y=relu(wx+b) 第一次卷积池化
            x_image = tf.reshape(self.x, [-1, 28, 28, 1])  # tf.reshape():解决输入图像的维数不符合的情况，-1表示根据实际情况定

            W_conv1 = self.weight_variable([5, 5, 1, 32])  # 卷积核5*5，通道数为1，对应输出32张图
            b_conv1 = self.bias_variable([32])

            h_conv1 = tf.nn.relu(self.conv2d(x_image, W_conv1) + b_conv1)  # 图片变为：（28-1）/1+1=28*28
            h_pool1 = self.max_pool_2x2(h_conv1)  # 池化后变为28/2=14*14


            # 2.y=relu(wx+b) 第二次卷积池化
            W_conv2 = self.weight_variable([5, 5, 32, 64])  # 卷积核5*5，通道数为32，对应输出64
            b_conv2 = self.bias_variable([64])
            h_conv2 = tf.nn.relu(self.conv2d(h_pool1, W_conv2) + b_conv2)  # 图片变为（14-1）/1+1=14*14
            h_pool2 = self.max_pool_2x2(h_conv2)  # 池化后变为14/2=7*7
            """经过两次卷积和池化操作后，图片大小变为7*7，共64个卷积核"""

            # 3.全连接层
            W_fc1 = self.weight_variable([7 * 7 * 64, 1024])  # 加入1024个神经元
            b_fc1 = self.bias_variable([1024])

            # 把刚才池化后输出的张量reshape成一个一维向量
            h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
            h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

            # 4.dropout防止过拟合的方法
            keep_prob = tf.placeholder(tf.float32)
            h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

            # 4.类别预测与输出
            W_fc2 = self.weight_variable([1024, 10])
            b_fc2 = self.bias_variable([10])

            # 应用softmax实现分类
            y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

            # 在 2017年3月2号以后；用 tf.global_variables_initializer() 替代 tf.initialize_all_variables()
            init_op = tf.global_variables_initializer()  # 变量初始化

            saver = tf.train.Saver()  # 实例化对象，保存所有的checkpoint 文件
            module_file = tf.train.latest_checkpoint('E:\pythonpackage\PyQt_model\model.ckpt')
            with tf.Session() as sess:
                sess.run(init_op)
                if module_file is not None:
                    # 重载模型的图及权重参数
                    saver.restore(sess, module_file)  # 这里使用了之前保存的模型参数

                prediction = tf.argmax(y_conv, 1)
                predint = prediction.eval(feed_dict={self.x: [tva], keep_prob: 1.0}, session=sess)

                # print('recognize result:')
                # print(predint[0])

            return predint[0]

if __name__ == '__main__':
    cnn_model = deeper_model()  # 实例化
    new_img='E:\\桌面\\3.jpg'
    reslut = cnn_model.startRecognize(new_img)  # 调用模型，输出识别结果
    print("这结果：", reslut)
