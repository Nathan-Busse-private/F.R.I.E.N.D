import platform
from setuptools import setup


# Ubuntu: sudo apt install espeak ffmpeg
install_requires = [
    'comtypes; platform_system == "Windows"',
    'pypiwin32; platform_system == "Windows"',
    'pywin32; platform_system == "Windows"',
    'pyobjc>=2.4; platform_system == "Darwin"'
]


with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='Speech_engine',
    packages=['Speech_engine', 'Speech_engine.drivers'],
    version='2.91',
   description='Text to Speech (TTS) library for Python 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.',
    long_description=long_description,
    summary='Offline Text to Speech library with multi-engine support',
    install_requires=install_requires ,
    keywords=['Speech_engine' , 'ivona','Speech_engine for python3' , 'TTS for python3' , 'Speech_engine' ,'text to speech for python','tts','text to speech','speech','speech synthesis','offline text to speech','offline tts','gtts'],
    classifiers = [
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
    ],
)
