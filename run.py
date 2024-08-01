
import os,sys,platform
print(' • Checking updates');os.system('git pull -q');print('')
bit = platform.architecture()[0]
if bit == '32bit':
    print(" • This tool doesn't support 32bit devices");exit()
elif bit == '64bit':
    import MFBC64
else: print(" • Your device doesn't support this tool ");exit()
