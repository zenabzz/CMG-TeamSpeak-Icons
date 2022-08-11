"""
This script was made by zenabz (Discord: zenabz#0646)
"""
print('-----------------------------------------------------')
print('This script was made by zenabz (Discord: zenabz#0646)')
print('-----------------------------------------------------', end = '\n\n')

import os, shutil

cmg_teamspeak_server = 'OWVWSEhsSnRKQ1QzamFyOFNDci9zQkdLNGRjPQ=='
default_cache_path = os.path.expandvars(f'%appdata%\TS3Client\cache\{cmg_teamspeak_server}') 

if not os.path.exists(default_cache_path):
    while not os.path.exists(default_cache_path):
        print('CMG Teamspeak cache not found!')
        default_cache_path = str(input('Enter Teamspeak cache path: '))

    if not cmg_teamspeak_server in default_cache_path:
        directory_file_names = os.listdir(default_cache_path)
        if not cmg_teamspeak_server in directory_file_names:
            print('CMG Teamspeak cache not found!')
            quit()
        else:
            default_cache_path = f'{default_cache_path}\{cmg_teamspeak_server}'

icons_path = default_cache_path
if not 'icons' in default_cache_path:
    icons_path = f'{default_cache_path}\icons'

    directory_files = os.listdir(default_cache_path)
    if not 'icons' in directory_files:
        print('Icons directory not found!, creating new directory...')
        os.makedirs(icons_path)
    else:
        icons_directory_files = os.listdir(icons_path)
        if icons_directory_files.__len__() > 0:
            for file_name in icons_directory_files:
                try:
                    os.remove(f'{icons_path}\{file_name}')
                except FileNotFoundError:
                    continue
    
for file_name in os.listdir('./icons'):
    shutil.copy(f'./icons/{file_name}', '{}\{}.'.format(icons_path, file_name[:file_name.index('.png')]))
    
print('Icons successfully transferred!')
input()