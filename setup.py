from setuptools import setup
from Cython.Build import cythonize
__author__ = "Uğurkan Hoşgör"
__version__ = "1.0.0"
#Requires https://visualstudio.microsoft.com/visual-cpp-build-tools/
if __name__ == "__main__":
    setup(
        ext_modules=cythonize(
            ['question_c.pyx'],
            language_level="3", # 3 or "2" or "3str"
            annotate=True), # html annotation file
    )
