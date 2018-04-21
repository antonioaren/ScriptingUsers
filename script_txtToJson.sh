#!/bin/bash
ARCHIVOS=`find users/users -name '*.txt'`
NUMERO_ARCHIVOS=`find users/users -name '*.txt' | wc -l`
echo 'El número de arhivos .txt es '$NUMERO_ARCHIVOS
echo $ARCHIVOS
