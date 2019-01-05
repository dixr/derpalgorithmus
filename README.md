# DerPAlgorithmus

Kivy App to compute payments of an arbitrary number of persons under certain conditions.

## How to run?

After installing kivy >= 1.10.0 and its dependencies through pip, the app can be run using
```
python main.py
```
Precompiled APKs for Android can be found in `bin/`. 

## Compilation for Android

Compilation of the app for android is best done in a clean virtualenv. The right versions of the required packages can be installed with
```
pip install -r requirements.txt
```
After activating the virtualenv and installing the requirements, the app can be compiled with
```
buildozer android debug
```
The resulting APKs will be in `bin/`.
