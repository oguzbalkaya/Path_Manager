#! /bin/bash

printf "Write the path you want to install.\n"
while :
do
	read -p "(Default $HOME) : " prefix
	if [ -d $prefix ]
	then
		break
	else
		echo "There is no directory : $prefix"
	fi
done

if [ $prefix=="" ]
then
	prefix="$HOME"
fi

echo "Creating .pathList file to $prefix"
touch $prefix/.pathList
echo "Creating .pathManager.sh file to $prefix"
mv ./files/.pathManager.sh $prefix
echo "Editing .basrc file"
chmod +w $HOME/.bashrc 
echo "source $prefix/.pathManager.sh" >> $prefix/.bashrc	
chmod -w $HOME/.bashrc
read -p "Do you want to create a desktop shortcut? (yes|no) : "

if [ "$REPLY" == "yes" ]
then
	shortcut="[Desktop Entry]
    Version=1.0.0
    Type=Application
    Terminal=false
    Exec=python3 $PWD/main.py
    Name=Path Manager
    Icon=$PWD/ui/icon.png"
    echo "$shortcut" >> $HOME/Desktop/Path_Manager.desktop
fi

