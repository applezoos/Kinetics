#
# 2023-07-06 kang
#

import PIL
# import skimage.io
# from skimage.transform import resize, pyramid_reduce
import math, random
import numpy as np
import os
import argparse
import subprocess
from natsort import natsorted

from pathlib import Path

def run_ffmpeg(vid_path:Path):
    
    print(vid_path)
    exit()
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        print("Command output:")
        print(result.stdout)
    else:
        print("Error running the command:")
        print(result.stderr)
    
def make_setfile(rootdir, phase, sample_r, set_n, setpath_fmt='k400_{:d}per{:02d}.txt'):
    for set_i in range(1, set_n + 1):
        selected = []
        
        class_dirs = list((rootdir/phase).glob('*'))
        class_n = len(class_dirs)
        for class_i, class_dir in enumerate(class_dirs, 1):
            vid_files = list(class_dir.glob('*'))
            
            vid_n = len(vid_files)
            sel_n = int(math.ceil(vid_n * sample_r))
            if vid_n > 1:
                print(f"[set {set_i} of {set_n}][cls {class_i} of {class_n}] {class_dir} ({sel_n}/{vid_n})")
                
                # selected files
                sel_files = random.sample(vid_files, sel_n)
                selected += natsorted(sel_files)  # sort

        # write file
        setfile = setpath_fmt.format(int(sample_r*100), set_i)
        print(f"    --> setfile: {setfile} (n={len(selected)}))")
        with open(setfile, 'w') as fp:
            for path in selected:
                fp.write(str(Path(*path.parts[-2:])))
                fp.write('\n')
            

def main(setfile, datadir, outdir, phase, sample_r=0.5, set_n=2):
    
    pass
    

if __name__ == '__main__':
    
    # <rootdir>/<phase>/<class>/<video.mp4>
    dsroot = Path('/mnt/d/Data/Kinetics/k400/videos')
    phase = 'train'
    
    # make_setfile(dsroot, phase, sample_r, set_n, setpath_fmt='k400_{:d}per{:d}.txt')
    main_run_ffmpeg('k400_50per2.txt', outroot)