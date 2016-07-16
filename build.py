# This is just the python file that puts all the CSS files
# together and minifies the output to make my life easier

import os.path
import shutil
import glob
import time
import datetime
from csscompressor import compress

# -------------- FILE NAME ------ PURPOSE --------------
               
order       = [ 'etc.css',       # general layout, common margins, and whatever can't be categorized into the other files
                'forms.css',     # forms other than the submit post form
                'submit.css',    # submit post form
                'header.css',    # subreddit header
                'sidebar.css',   # subreddit sidebar
                'sidemd.css',    # sidebar usertext md
                'titlebox.css',  # sidebar titlebox except for the usertext md
                'thing.css',     # style for .thing elements (links and comments alike)
                'links.css',     # links within linklisting and linklisting page
                'linkbtn.css',   # link buttons
                'cpage.css',     # comments page page layout & top area (panestack-title, menuarea)
                'ctable.css',    # sitetable and comments in comments page
                'usertext.css',  # usertext editor input
                'search.css',    # search page (does not include search input in sidebar, which is in sidebar.css)
                'footer.css',    # subreddit footer
                'wiki.css',      # subreddit wiki
                'modpages.css',  # any moderator pages that required additional CSS
                'ext.css',       # misc. styles for extensions (RES, Mod Toolbox, etc.) that can't be categorized into the other files
                'temp.css',      # temporary
                'nightmode.css', # nightmode
                'media.css'      # extra media queries for small screens and such
              ]      
                
# input/output variables
src_dir     = 'src'
dist_dir    = 'dist'
dist_file   = 'dist.css'

def top(build_ver):
    return ('/*\n' +
            '    CSS theme for /r/aww' + '\n' +
            '    Build: '    + str(build_ver) + '\n' +
            '    Author: '   + '/u/kwwxis' + '\n' +
            '    Modified: ' + datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-0' +
                               str(7 if time.localtime().tm_isdst else 8) + '00 (ISO-8601)') + '\n' +
            '    Source: '   + 'github.com/matthew0x40/aww-css/' + '\n' +
            '*/')

def run():
    with open(r'build.dat','r+') as build:
        build_ver = int(build.read()) + 1
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
        build.write(str(build_ver))
        
        print('\nDone!')

if __name__ == '__main__':
    run()