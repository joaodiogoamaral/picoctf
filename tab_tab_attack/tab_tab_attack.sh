#!/bin/bash
wget https://mercury.picoctf.net/static/72712e82413e78cc8aa8d553ffea42b0/Addadshashanammu.zip  
unzip Addadshashanammu.zip

#NOte: To find the directory names, I simply pressed tab in the command line. The grep expression is just to isolate the flag from the remaining of the strings output.

echo "\n\n\nHere is the flag \n\n"

strings Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet | grep picoCTF
