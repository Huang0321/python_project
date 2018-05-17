import numpy as np


def file2matrix(filename):
    """
    函数说明: 打开并解析文件, 对数据进行分类： 1代表不喜欢, 2代表魅力一般, 3代表极具魅力

   Parameters:
        filename - 文件名

    Returns:
        returnMat - 特征矩阵
        classLabelVector - 分类Label向量
    """
    # 打开文件
    with open(filename, 'r') as fr:
        # 读取文件内容
        arrayOLines = fr.readlines()
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 返回的numpy矩阵, 解析完成的数据：numberOfLines行, 3列
    returnMat = np.zeros((numberOfLines, 3))
    # 返回分类标签的向量
    classLabelVector = []
    # 行的索引值
    index = 0
    for line in arrayOLines:
        # s,strip(rm), 当rm空时， 默认删除空白符(包括'\','\r', '\t')
        line.strip()
        # 使用s.spilt(str="", num=string, cout(str))将字符串根据'\t’分隔符进行切片
        listFromLine = line.split('\t')
        # 将数据前三列提取出来, 放到returnMat的Numpy矩阵中, 也就是特征矩阵
        returnMat[index, :] = listFromLine[0: 3]
        # 根据文中标记的喜欢程度进行分类， 1代表不喜欢, 2代表魄力一般, 3代表极具魅力
        if listFromLine[-1].strip('\n') == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1].strip('\n') == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1].strip('\n') == 'largeDoses':
            classLabelVector.append(3)
        print(classLabelVector)
        index += 1
    return returnMat, classLabelVector


if __name__ == '__main__':
    # 打开的文件名
    filename = 'datingTestSet.txt'
    # 打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    print(file2matrix(filename))
    print(datingDataMat)
    print(datingLabels)
