# -*- coding: utf-8 -*-
"""
CopyPkgs.py

Copy pkgs from Anaconda pkgs folder to a channel folder 
The input file is the result of a "conda list --explicit" after using Notepad++
to convert the output file to utf-8 encoding.

"""
import os, os.path, shutil

rootdir = os.path.join(os.environ['userprofile'],'Documents','Psychopy')
pkgdir = os.path.join(os.environ['userprofile'],'Anaconda3','pkgs')
infile = open(os.path.join(rootdir,'perceptionlab-pkgs.txt'))
channelpath = os.path.join(rootdir,'PerceptLabChannel')
for l in infile:
    if '@EXPLICIT' in l:
        break

for l in infile:
    l=l.strip()
    arch=os.path.basename(os.path.dirname(l))
    pkg=os.path.basename(l)
#    print('arch {}, pkg {}'.format(arch,pkg))
    if os.path.exists(os.path.join(pkgdir,pkg)):
        print('copying package {} to {} '.format(pkg, os.path.join(channelpath, arch)))
        shutil.copy2(os.path.join(pkgdir,pkg),
                     os.path.join(channelpath,arch,pkg))
infile.close()
