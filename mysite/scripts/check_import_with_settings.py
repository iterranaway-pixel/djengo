import os, sys, importlib, traceback
# Ensure project package is first on sys.path
sys.path.insert(0, r'C:\Users\Satyam KUmar\Desktop\djengo dibya\mysite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
print('DJANGO_SETTINGS_MODULE=', os.environ.get('DJANGO_SETTINGS_MODULE'))
try:
    import django
    django.setup()
    m = importlib.import_module('blog.views')
    print('Imported blog.views:', m)
    print('has post_list:', hasattr(m, 'post_list'))
    print('has post_detail:', hasattr(m, 'post_detail'))
    print('members sample:', [name for name in dir(m) if not name.startswith('_')][:50])
except Exception:
    traceback.print_exc()
