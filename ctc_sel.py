# # -*- coding:utf8 -*-
from keras.utils import to_categorical
import sys
import os
import numpy as np
src_dir = sys.argv[1]
tar_dir = sys.argv[2]
# 首先看一下第0维最大时，第0维的数据分布
# ctc_sel(ctc_dir, save_npy)
def ctc_sel(src_dir, tar_dir):
    for fi in os.listdir(src_dir):
        ctc_path = os.path.join(src_dir, fi)
        ctc_npy = np.load(ctc_path)
        for i in range(len(ctc_npy)):
            if np.argmax(ctc_npy[i]) == 0:
                ctc_blank.append(ctc_npy[i][0])

    ctc_blank = np.array(ctc_blank)
    np.save(tar_dir, ctc_blank)

# 把ctc_phone的概率转成 max_index的数组
# 调用将数组转成one-hot形式
def ppgs_to_onehot(src_dir, tar_dir):
    for fi in os.listdir(src_dir):
        ctc_path = os.path.join(src_dir, fi)
        ctc_npy = np.load(ctc_path)
        index_arr = np.argmax(ctc_npy, axis=1)
        encoded=to_categorical(index_arr)
        save_path = os.path.join(tar_dir, fi)
        np.save(save_path, encoded)
        #print(encoded)
        print('saved', save_path)

def main():
    #ctc_sel(src_dir, tar_dir)
    ppgs_to_onehot(src_dir, tar_dir)

if __name__=='__main__':
    main()
