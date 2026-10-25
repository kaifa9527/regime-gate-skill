import pathlib, tempfile, os
def atomic_write(target, content):
    target=pathlib.Path(target); fd,tmp=tempfile.mkstemp(dir=target.parent); os.fdopen(fd,'w').write(content); os.replace(tmp,target)
