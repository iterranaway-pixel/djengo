import importlib, sys, traceback
sys.path.insert(0, r'C:\Users\Satyam KUmar\Desktop\djengo dibya\mysite')
print('sys.path[0]=', sys.path[0])
try:
    m = importlib.import_module('blog.views')
    print('Imported blog.views:', m)
    print('has post_list:', hasattr(m, 'post_list'))
    print('members:', [name for name in dir(m) if not name.startswith('_')])
except Exception:
    print('--- Exception while importing blog.views ---')
    traceback.print_exc()
