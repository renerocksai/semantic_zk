#!/usr/bin/env python3

version = '0.4'
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

# for bash scripts
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == '--version':
            print(version)
        elif sys.argv[1].lower() == '--prefix':
            print(prefix)
        elif sys.argv[1].lower() == '--release-notes':
            print(release_notes)
    else:
        print(version, prefix)
