#!/bin/bash

echo "cleaning.  Disk usage before:"

du -sh

find . -name '*.aux' | xargs -I {} -t rm -f {}

find . -name '*.log' | xargs -I {} -t rm -f {}

find . -name '*.out' | xargs -I {} -t rm -f {}

find . -name '.ipynb_checkpoints' -print | xargs -I {} -t rm -rf {}

find . -name '.DS_Store' -print | xargs -I {} -t rm -rf {}

echo "Disk usage after:"

du -sh

echo "Done!"
