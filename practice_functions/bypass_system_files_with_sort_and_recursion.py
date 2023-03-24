def bypass_files(path, depth=1):
    import os
    print('-'*depth+' [', path, f'({len(os.listdir(path))} Elements)', ']' )
    dir_lst = []
    files_lst = []
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            dir_lst.append(i)
        elif os.path.isfile(path + '/' + i):
            files_lst.append(i)
    if dir_lst:
        print('Directory:', *[f'{"-"*depth}/ {i}' for i in dir_lst], sep='\n')
    if files_lst:
        print('Files:', *[f'{"-"*depth} {i}' for i in files_lst], sep='\n')
    if len(dir_lst + files_lst) < 1:
        print('Empty directory')
    print()
    for i in dir_lst:
        bypass_files(path+'/'+i, depth+1)


learn_path = r'C:\Users\akram\YandexDisk\[Антон]\-- Книги\Эзотерика Психология Философия'
bypass_files(learn_path)
