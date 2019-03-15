#!/bin/bash

import os

clear
echo "Instalação SDK Android"

ent = input("Digite S para continuar ou N para cancelar: ")

if(ent == s):
    os.system("sudo apt-get install libgl1-mesa-dev")
    os.system("wget http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz")
    os.system("tar -zxvf android-sdk_r24.4.1-linux.tgz")
    os.system("android-sdk-linux/tools/./android")
else:
    exit():