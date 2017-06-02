#!/bin/sh

cp -r Xorg/* $HOME
cp -r i3/* $HOME
cp scripts/* /usr/local/bin
cp zsh/.z* $HOME
zsh
while [ ! -d $HOME/.antigen/bundles/robbyrussell/oh-my-zsh/themes ]
do
	sleep 2
done
cp zsh/kamakwazee.zsh-theme $HOME/.antigen/bundles/robbyrussell/oh-my-zsh/themes
