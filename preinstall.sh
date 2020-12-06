#!/bin/bash

read -p "Install Ruby and GCC?[yN] " -n 1 -r
echo    # (optional) move to a new line

if [[ $REPLY =~ ^[Yy]$ ]]    
then
    sudo apt-get install ruby-full build-essential zlib1g-dev 
fi

read -p "Update .jekyllrc?[yN] " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
echo '# Install Ruby Gems to ~/gems' >> ~/.jekyllrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.jekyllrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.jekyllrc
    source ~/.jekyllrc
fi

read -p "Initialize gems?[yN] " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    bundle install
    bundle update
fi
