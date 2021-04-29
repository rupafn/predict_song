import os
import subprocess
import sys
from multiprocessing.dummy import Pool as ThreadPool

def extractFeatures(filename, outpath):
    print('Extracting')
    commands = []

    pool = ThreadPool(4)
    audio = filename
    filename = filename.split()[0]
    print(outpath)
    cmmnd = 'SMILExtract -C app/feature_config1.conf -I {input} -O {dest}'.format(input=audio, dest=outpath)
    # cmmnd = "SMILExtract -C feature_config1.conf -I " + audio + " -O output/{filename}.csv" 
    print(cmmnd)
    # pool.map(runcommand, [cmmnd])
    runcommand([cmmnd])

def runcommand(command):
    subprocess.call(command, shell=True)


