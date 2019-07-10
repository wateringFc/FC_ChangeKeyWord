#!/usr/bin/env python\
# -*- coding: utf-8 -*-

import os


for dirpath, _, filenames in os.walk('.'):
    for filename in filenames:
        if filename.startswith('KXH'):
            oldFile = os.path.join(dirpath, filename)
            newFile = os.path.join(dirpath, filename.replace('KXH', 'Change_', 2))
            print newFile
            inFile = open(oldFile)
            outFile = open(newFile, 'w')
            replacements = {'KXH':'Change_'}
            for line in inFile:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                outFile.write(line)
            inFile.close()
            outFile.close()
            os.remove(oldFile)