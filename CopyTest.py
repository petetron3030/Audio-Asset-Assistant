#!/usr/bin/python3

import shutil
import os

def main():
    os.makedirs("Delivery/AAA/BBB/wav/AAA_BBB_0001")
    shutil.copy("Audio/AAA/BBB/wav/AAA_BBB_0001/AAA_BBB_0001_00101.wav",
                "Delivery/AAA/BBB/wav/AAA_BBB_0001")

if __name__ == "__main__" : main()
