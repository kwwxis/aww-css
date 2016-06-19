import os.path
import shutil
import glob
import time
import datetime
from csscompressor import compress

order       = [ 'etc.css',
                'forms.css',
                'header.css',
                'sidebar.css',
                'thing.css',
                'links.css',
                'comments.css',
                'search.css',
                'ext.css']
src_dir     = 'src'
dist_dir    = 'dist'
dist_file   = 'dist.css'

def top(build_ver):
    return ('/*\n' +
            '    CSS theme for /r/aww' + '\n' +
            '    Build: '    + str(build_ver) + '\n' +
            '    Author: '   + '/u/kwwxis' + '\n' +
            '    Modified: ' + datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-0' +
                               str(7 if time.localtime().tm_isdst else 8) + '00 (ISO-8601)') +
            '\n*/')

def run():
    with open(r'build.dat','r+') as build:
        build_ver = int(build.read())
        print('\nBUILD #' + str(build_ver))
        
        if not os.path.isdir(src_dir):
            print('\nFailed: the source directory, "' + src_dir + '" was not found')
            return
            
        # Combine files in specified order
        with open(dist_dir + '\\' + dist_file, 'wb') as outfile:
            for src_file in order:
                path = src_dir + '\\' + src_file
                
                if os.path.isfile(path):
                    with open(path, 'rb') as readfile:
                        shutil.copyfileobj(readfile, outfile)
                        print('  + ' + path)
                else:
                    print('\nFailed: target file not found: ' + path + ';\n' +
                    'if this file is no longer in use then you must remove it from the "order" variable in build.py')
                    return

        # Compress
        with open(dist_dir + '\\' + dist_file, 'r+') as outfile:
            raw  = outfile.read()
            mini = compress(raw)
            outfile.seek(0)
            outfile.write(top(build_ver) + '\n' + mini)
            outfile.truncate()
            
        # Increment build version in build.dat afterwards in case of failure
        build.seek(0)
        build.write(str(build_ver + 1))
        
        print('\nDone!')

if __name__ == '__main__':
    run()