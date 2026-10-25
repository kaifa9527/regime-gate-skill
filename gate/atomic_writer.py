import pathlib, tempfile, os
def atomic_write(p,c):
 p=pathlib.Path(p); f=tempfile.NamedTemporaryFile(mode='w',delete=False,dir=str(p.parent)); f.write(c); f.close(); os.replace(f.name,p)
