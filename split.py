import os
import argparse
import datetime
import csv
from shutil import copyfile


if __name__ == "__main__":
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--srcdir", default="", help="source video file directory")
    parser.add_argument("--outdir", default="", help="out video file directory")
    parser.add_argument("--infile", default="in.csv", help="csv file to calculate diff features.")    
    args = parser.parse_args()

    infile = args.infile
    srcdir = args.srcdir
    outdir = args.outdir
    '''
    infile = "D:/download/FSD50K.metadata/collection/collection_dev.csv"
    srcdir = "D:/download/FSD50K.dev_audio"
    outdir = "D:/download/cheering"

    brheader = False
    logcount = 0
    with open(infile, newline='') as csvfile:    
        rd = csv.reader(csvfile, delimiter=',')
        for row in rd:
            print( str(logcount) + "-----" + "start")
            logcount = logcount + 1            
            if brheader == False:
                brheader = True
            else:
                labels = row[1]
                if labels.find("Applause") != -1 & labels.find("Crowd") != -1 & labels.find("Cheering") != -1:
                    srcfile = srcdir + "/" + row[0] + ".wav"
                    str_output = '{:0>5}'.format(logcount)
                    outfile = outdir + "/"  + str_output + ".wav"
                    copyfile(srcfile, outfile)
