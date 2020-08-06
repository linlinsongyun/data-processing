import numpy as np
import scipy.io.wavfile
import os
import multiprocessing as mp
from tqdm import tqdm

ppgs_dir = '/media/mfs/cheh/voice_conversion/vc-asr/ppgs_40ms/multi_256_20ms/'
out_dir = '/media/mfs/cheh/voice_conversion/vc-asr/ppgs_40ms_energy/multi_256_20ms/'
input_dir='/media/mfs/cheh/ks_wav/noise16000/'

#os.makedirs(out_dir, exist_ok=True)

window_size_ = 0.025
shift_size_ = 0.01

def get_wav_filelist(wav_dir):
    wav_files = []
    for file in os.listdir(wav_dir):
        whole_filepath = os.path.join(wav_dir,file)
        if os.path.isfile(whole_filepath) and str(whole_filepath).endswith(".wav"):
            wav_files.append(whole_filepath)
        elif os.path.isdir(whole_filepath):
            wav_files += get_wav_filelist(whole_filepath)

    wav_files.sort()
    return wav_files


def exactor(wav_file):
    print(wav_file)
    wav_file = os.path.basename(wav_file).split("/")[-1]
    print(wav_file)
    sr, wav = scipy.io.wavfile.read(os.path.join(input_dir, wav_file))
    new_wav_file = wav_file.replace('wav','npy')
    print(new_wav_file)
    out_name = os.path.join(out_dir, new_wav_file)
    energy = []
    window_size = int(window_size_ * sr)
    shift_size = int(shift_size_ * sr)
    for j in range(0, len(wav) - window_size, shift_size):
        power = np.sum(np.absolute(wav[j: j + window_size])) / window_size
        power = np.clip(power, 1, np.inf)
        energy.append(np.log10(power))
        #print(np.log10(power))
    #np.save(out_name, np.array(energy))
    ppgs_name = os.path.join(ppgs_dir, new_wav_file)
    en = np.array(energy)
    if os.path.exists(ppgs_name) == False:
      return
    ppgs = np.load(ppgs_name)
    len1 = len(ppgs)
    len2 = len(en)
    if len1 > len2:
       ppgs = ppgs[:len2]
    else:
       en = en[:len1]
    en2 = en.reshape(len(en),1)
    
    new_ppg = np.concatenate((ppgs,en2),axis=1) 
    print(new_ppg.shape)
    np.save(out_name,new_ppg)

wav_files = get_wav_filelist(input_dir)
pool = mp.Pool(mp.cpu_count())
# pool.map(function, datalist)
pool.map(exactor, wav_files)
    

