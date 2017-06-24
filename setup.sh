#!/bin/sh

pacman -Syu

pacman -S python2 python2-pip git

pip2 install Pillow

git clone https://github.com/zsh-users/antigen.git $HOME/antigen

cp -r Xorg/* $HOME
cp -r i3/* $HOME
cp scripts/* /usr/local/bin
cp zsh/.z* $HOME
zsh -c exit
while [ ! -d $HOME/.antigen/bundles/robbyrussell/oh-my-zsh/themes ]
do
	sleep 2
done
cp zsh/kamakwazee.zsh-theme $HOME/.antigen/bundles/robbyrussell/oh-my-zsh/themes
