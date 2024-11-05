#!/bin/bash

# Compter le nombre de fichiers dans chaque sous-dossier

echo "Compteur de fichiers dans chaque dossier :"

for dir in car-number-plat datasets; do
    echo "Dans le dossier '$dir' :"
    find "$dir" -type f | wc -l
    echo ""
done

echo "Détails par sous-dossier dans 'datasets' :"
for subdir in train valid test; do
    echo "Dans le sous-dossier 'datasets/images/$subdir' :"
    find "datasets/images/$subdir" -type f | wc -l
    echo "Dans le sous-dossier 'datasets/labels/$subdir' :"
    find "datasets/labels/$subdir" -type f | wc -l
    echo ""
done
