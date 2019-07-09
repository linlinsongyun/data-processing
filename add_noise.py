import sys
import os
import random
#rirs_dir = sys.argv[2]
wav_dir = sys.argv[1]
save_dir = sys.argv[2]
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

#rirs_noise = os.listdir(rirs_dir)
snr_list = [5.0, 7.5, 10.0, 12.5]
for fi in os.listdir(wav_dir):
    source_wav = os.path.join(wav_dir, fi)
    print(source_wav)
    snr = random.choice(snr_list)
    #for noise in os.listdir(rirs_dir):
    name = fi.split('.wav')[0]
    save_name = name+'_white.wav'
    save_wav = os.path.join(save_dir, save_name)
    #rirs_wav = random.choice(rirs_noise)
    #rirs_wav = os.path.join(rirs_dir, rirs_wav)
    #print("rirs_wav", rirs_wav)
    #os.system("/opt/kaldi/src/featbin/wav-reverberate --shift-output=true --impulse-response='sox %s -r 16000 -t wav - |' --start-times='0' --snrs='0.0' %s %s" %(rirs_wav, source_wav, save_wav))
    os.system("../kaldi-master/src/featbin/wav-reverberate --shift-output=true --additive-signals='sox ../kaldi-master/simulated_rirs/white.wav -r 16000 -t wav - |' --start-times='0' --snrs='%f' %s %s" %(snr, source_wav, save_wav))
