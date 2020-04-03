# encoding:utf-8

def filetype(filename,has_dot=False):
    idx = filename.rfind('.')
    if 0 < idx < len(filename)- 1:
        rlt = idx if has_dot else idx + 1
        return filename[rlt:]
    else:
        return ''

if __name__ == '__main__':
    print(filetype('abc.doc',True))
    print(filetype('abc.doc'))
