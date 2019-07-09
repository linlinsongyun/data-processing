import os

dir = 'VCTK'
#sort into diff folder
'''
for fi in os.listdir(dir):
    if fi.endswith('.wav'):
        folder = fi[:4]
        if not os.path.exists(folder):
            os.makedirs(folder)
        if fi.startswith(folder):
            os.system('mv %s %s' %(fi, folder))
'''

for fi in os.listdir(dir):
    print("start")
    if fi.startswith('p'):
        print(fi)
        folder = os.path.join(dir, fi)
        new = os.path.join(dir, '%s_16k'%fi)
        if not os.path.exists(new):
            os.makedirs(new)
        for fi in os.listdir(folder):
            new_name = os.path.join(new, fi)
            wav_name = os.path.join(folder, fi)
            print('wav_name', wav_name)
            os.system('/usr/bin/sox %s -r 16000 %s' %(wav_name, new_name))
        print("%s is ok" %folder)
print('done')
