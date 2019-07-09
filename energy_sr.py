import os
import sys
import librosa
import random
import soundfile as sf

# energy decay
wav_dir = sys.argv[1]
save_dir = sys.argv[2]
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for fi in os.listdir(wav_dir):
    wav_file = os.path.join(wav_dir, fi)
    wav, sr = sf.read(wav_file)
    X = random.randint(5,20)
    print('x', X)
    alpha = 10**( -X/20)
    new_wave =  wav * alpha
    save_path = os.path.join(save_dir, fi)
    sf.write(save_path, new_wave, 16000)
    print('saved',save_path)

print('all end')
