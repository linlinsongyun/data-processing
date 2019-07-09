import os
import  sys

wav_dir = sys.argv[1]
save_dir = sys.argv[2]
for f1 in os.listdir(wav_dir):
    f1_path = os.path.join(wav_dir, f1)

    os.system('python sr_var.py %s %s 16000'%(f1_path, save_dir))
