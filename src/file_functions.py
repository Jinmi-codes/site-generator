import os, shutil

def file_copy(src, dst):
    src = os.path.normpath(src)
    dst = os.path.normpath(dst)
    if not os.path.exists(src):
        raise Exception("source filepath doesn't exists.")
    if not os.path.exists(dst):
        os.mkdir(dst)
    content = os.listdir(src)
    for file in content:
        if os.path.isfile(os.path.join(src, file)):
            shutil.copy(os.path.join(src, file),os.path.join(dst, file))
        else:
            file_copy(os.path.join(src, file), os.path.join(dst,file))
        
file_copy("./static","./public")