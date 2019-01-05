# DerPAlgorithmus

> Kivy App to compute payments of an arbitrary number of persons under certain conditions.

## How to run?

After installing kivy >= 1.10.0 and its dependencies through pip, the app can be run using
```
python main.py
```
The app was tested using pygame == 1.9.4.

A precompiled APK for Android can be found in `apk/`.

## Building Android APK

Building the app for android is best done in a clean virtualenv under Linux. The right versions of the required packages can be installed with
```
pip install -r requirements.txt
```
After activating the virtualenv and installing the requirements, the app can be built with
```
buildozer android debug
```
Note that buildozer takes a while to setup the environment if run for the first time. The resulting APKs will be in `apk/`.

##### Sequence of commands under Ubuntu 18.04
Since the build process is rather involved, there are many things that can go wrong. Here is a sequence of commands that worked for me to build the APK under Ubuntu 18.04:
```bash
# prepare the system
sudo apt install -y python-pip build-essential mercurial git python2 python2-dev python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev libgstreamer1.0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good
sudo dpkg --add-architecture i386
sudo apt install build-essential ccache libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python2.7 python2.7-dev openjdk-8-jdk unzip zlib1g-dev zlib1g:i386
sudo pip install --upgrade testresources virtualenv setuptools

# enter the virtualenv
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt

python main.py  # to run and test

buildozer android debug  # to create the APK

deactivate  # to leave the virtualenv
```
