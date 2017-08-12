import importlib.machinery
import os

def main():
    path = 'csjis.py'
    ccode = importlib.machinery.SourceFileLoader(os.path.basename(path).split('.')[0], path).load_module()
    ccode.register()
    code_name = ccode.get_name()

    bs = '～XB木瀬\u0000間Sハル'.encode(code_name)
    str = bs.decode('shift-jis')
    str2 = bs.decode(code_name)
    print(str)
    print(str2)

if __name__ == "__main__":
    main()
