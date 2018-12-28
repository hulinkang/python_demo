

#!/usr/bin/python3

import os, sys
import time
import subprocess

necessary_result = ['./linux64/sys/lib/libssl.so.1.1', './linux64/sys/lib/libcrypto.so.1.1']

def getInfos(Dir):
    print('\n\n')
    infos = []
    for root, dirs, files in os.walk(Dir):
        for f in files:
            infos.append(os.path.join(root, f))
    print(infos)
    print('\n\n')


def main(argv):
    count = 0    
    notNecessary = []
    necessary = []

    for root, dirs, files in os.walk('.'):
        for f in files:
            if not 'bin' in root:
                continue     
                
            #ignore python2.7
            if 'python2.7' in root: 
                continue

            path_file = os.path.join(root, f)

            if not 'linux64/bin' in path_file:
                continue

            if path_file in new_file_result:
                continue
            count += 1


            #except itself
            if f == 'xxx-express':
                continue

            if f.endswith('-hlk'):
                continue

            print(count)

            #mv it by renaming
            if not path_file.endswith('-hlk'): 
                new_path_file = path_file + '-hlk'
                os.rename(path_file, new_path_file)

            #run
            os.chdir('mytest-SE-prj0')
            pid = subprocess.Popen(['./xxx-express', 'targets/zynqmp/zynqmp-vxworks-7.xxxx'])
            os.chdir('..')
            try:
                pid.wait(timeout = 2)
            except subprocess.TimeoutExpired: #is running
                print('run success!%s'%(path_file))
                notNecessary.append(path_file)
                pid.kill()
            else:
                print('%s is Necessary! \n**********************\n'%(path_file))
                necessary.append(path_file)
                os.rename(new_path_file, path_file)


    print('\nnecessary')
    print(necessary)

if __name__ == '__main__':
    main(sys.argv)
