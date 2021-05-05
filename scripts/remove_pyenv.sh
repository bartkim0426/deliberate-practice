#!/bin/bash
# remove all pyenv versions at once

# create pyenv-versions.txt
# pyenv versions > pyenv.txt
# edit file and remaining only versions to delete
input='./pyenv-versions.txt'
while IFS= read -r line
do
    # echo "$line"
    pyenv uninstall -f "$line"
done < "$input"
