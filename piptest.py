import pip
from distutils.version import LooseVersion

if LooseVersion(pip.__version__) < LooseVersion('10'):
    # older pip version
    from pip.utils.appdirs import user_cache_dir
else:
    # newer pip version
    from pip._internal.utils.appdirs import user_cache_dir

print(user_cache_dir('pip'))
print(user_cache_dir('wheel'))
