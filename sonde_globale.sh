#!/bin/bash

echo "Sonde CPU"
python3 sonde1.py

echo "Sonde processus"
bash sonde2.sh

echo "Sonde disque"
bash sonde3.sh
