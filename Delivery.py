#!/usr/bin/python3

import shutil
import os

def main():
    delivery = open('Delivery.txt')
    for line in delivery:
        line = line.strip()
        fixation = line.split("_")
        label = fixation[0]
        subLabel = fixation[1]
        albumCode = fixation[2]
        trackCode = fixation[3]

        if not os.path.exists("Audio/{0}/{1}/wav/{0}_{1}_{2}/{0}_{1}_{2}_{3}.wav".format(label, subLabel, albumCode, trackCode)):
            print("{0}_{1}_{2}_{3}.wav missing".format(label, subLabel, albumCode, trackCode))

    print("\nStarting Copy")

    delivery = open('Delivery.txt')
    for line in delivery:
        line = line.strip()
        fixation = line.split("_")
        label = fixation[0]
        subLabel = fixation[1]
        albumCode = fixation[2]
        trackCode = fixation[3]
        
        if os.path.exists("Audio/{0}/{1}/wav/{0}_{1}_{2}/{0}_{1}_{2}_{3}.wav".format(label, subLabel, albumCode, trackCode)):
            if not os.path.exists("Delivery/{0}/{1}/wav/{0}_{1}_{2}".format(label, subLabel, albumCode, trackCode)):
                os.makedirs("Delivery/{0}/{1}/wav/{0}_{1}_{2}".format(label, subLabel, albumCode, trackCode))
            shutil.copy("Audio/{0}/{1}/wav/{0}_{1}_{2}/{0}_{1}_{2}_{3}.wav".format(label, subLabel, albumCode, trackCode),
                            "Delivery/{0}/{1}/wav/{0}_{1}_{2}".format(label, subLabel, albumCode, trackCode))
            print("{0}_{1}_{2}_{3}.wav".format(label, subLabel, albumCode, trackCode))
        else:
            print("{0}_{1}_{2}_{3}.wav does not exist".format(label, subLabel, albumCode, trackCode))
            continue
        
    print("Done")
                
if __name__ == "__main__" : main()
