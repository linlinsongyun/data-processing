import numpy as np
import os
import tensorflow as tf
import sys

#e.g. python read_weghit.py train/model-112847 net2/cbhg_mel/embedding1/embedding_before_highway/kernel bfh-k-7.npy
model = sys.argv[1]
tensor = sys.argv[2]
name = sys.argv[3]
reader = tf.train.NewCheckpointReader(model)
all_variables = reader.get_variable_to_shape_map()


#ckpt = tf.train.get_checkpoint_state(model_dir)
#ckpt_path = ckpt.model_checkpoint_path

#reader = pywrap_tensorflow.NewCheckpointReader(ckpt_path)
#param_dict = reader.get_variable_to_shape_map()
'''
for key, val in all_variables.items():
    try:
        print key
        os.system('echo %s %s >> arc.txt'%(key, val))
        #, val
    except:
        pass
'''
w0 = reader.get_tensor(tensor)

np.save(name,w0)
print(type(w0))
print(w0.shape)
#print(w0[0])
