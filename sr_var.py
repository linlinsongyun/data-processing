python sr_rate.py source_dir tar_dir tar_rate
#change sampling rate for wav files under srcdir and store new wav files in dstdir
import os
import sys
import sys
#dir="/home/zhangying09/corpus/BZNSYP"
src_dir = sys.argv[1]
#'LibriTTS/dev-clean-wav/emotional/'
des_dir = sys.argv[2]
#'emtional'
target_sr = int(sys.argv[3])
if not os.path.exists(des_dir):
    os.makedirs(des_dir)
def get_wavlist(dir, ext='.wav'):
    wav_list = []
    files = os.listdir(dir)
    for file in files:
        if not file.endswith(ext):
            continue
        wav_list.append(file)
    return  wav_list
    def sr_var(srcdir, dstdir, target_sr):
    if os.path.exists(srcdir):
        if not os.path.exists(dstdir):
            os.mkdir(dstdir)
        wavlist = get_wavlist(srcdir, '.wav')
        #target_sr = sys.argv[3]
        target_channel = 1
        for wav in wavlist:
            src = os.path.join(srcdir, wav)
            #print(src)
            dst = os.path.join(dstdir, wav.split('.')[0]+'.wav')
            os.system('/usr/bin/sox %s -r %d %s' %(src, target_sr, dst))
            #os.system("ffmpeg -y -i %s -ar %d -ac %d %s"%(
            #     src, target_sr, target_channel, dst))


#srcdir = sys.argv[1]
#dstdir = sys.argv[2]
sr_var(src_dir, des_dir, target_sr)
print("done")
