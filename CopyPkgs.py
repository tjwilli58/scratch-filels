# -*- coding: utf-8 -*-
"""
CopyPkgs.py

Copy pkgs from Anaconda pkgs folder to a channel folder 
The input file is the result of a "conda list --explicit" after using Notepad++
to convert the output file to utf-8 encoding.

"""
import os, os.path, shutil

pkgdir = r'C:\Users\timothy.j.williams1\AppData\Local\conda\conda\pkgs'
infile = open(r'L:\Downloads\Anaconda\PsychoPy\anaconda-py3-pkgs.txt')
channelpath = r'L:\Downloads\Anaconda\PsychoPy\PerceptLabChannel'
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
