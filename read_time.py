import os
import sys
wav_dir = sys.argv[1]

for i in os.listdir(wav_dir):
    if i.endswith('.wav'):
        wav = os.path.join(wav_dir, i)
        os.system('sox -V %s -n' %wav)
