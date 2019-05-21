from distutils.core import setup, Extension

MOD = 'mymath'  # 模块名
setup(name=MOD, ext_modules=[Extension(MOD, sources=['mymath_wrap.c', 'mymath.c'])])  # 源文件名
