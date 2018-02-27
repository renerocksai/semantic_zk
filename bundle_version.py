#!/usr/bin/env python3
DEPLOY_DIR = '_deploy'

version = '0.5'
prefix = 'pre'
release_notes = '''
This release contains:

* command line tool `zk2setevi`
* graphical tool `semantic_zk`

**New features:**

* 

See the [README](https://github.com/renerocksai/semantic_zk#zk2setevi---the-semantic-text-view-for-your-zettelkasten) for intstructions.

**Released files:**

* macOS:
    * `semantic_zk-{prefix}-{version}-macOS.zip` containing
        * `command_line/zk2setevi` (command line tool)
        * `semantic_zk-{version}.app` (graphical tool)

* Windows 10:
    * `semantic_zk-{prefix}-{version}-win10.zip` containing
        * `zk2setevi.exe` (command line tool)
        * `semantic_zk.exe` (graphical tool)
'''.format(version=version, prefix=prefix)

# for bash scripts and windows .cmd
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == '--version':
            print(version)
        elif sys.argv[1].lower() == '--prefix':
            print(prefix)
        elif sys.argv[1].lower() == '--release-notes':
            print(release_notes)
        elif sys.argv[1].lower() == '--tag':
            print('semantic_zk-{}-{}'.format(prefix, version))
        elif sys.argv[1].lower() == '--init':
            import os
            import shutil
            if os.path.exists(DEPLOY_DIR):
                shutil.rmtree(DEPLOY_DIR)
            os.makedirs(DEPLOY_DIR)
        elif sys.argv[1].lower() == '--deploy-dir':
            print(DEPLOY_DIR)
        elif sys.argv[1].lower() == '--rename-dist':
            import os
            # effing windows is sloooow
            import time
            time.sleep(3)
            src = 'dist'
            dest = 'semantic_zk-{prefix}-{version}-win10'.format(version=version, prefix=prefix)
            os.rename(src, os.path.join(DEPLOY_DIR, dest))
    else:
        print(version, prefix)
