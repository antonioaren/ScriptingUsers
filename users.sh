#!/bin/bash
datos = `cat $1`
 nombre=`cut -d ":" -f2 $datos`
 DNI=`cut -d ":" -f2 $datos`
 email=`cut -d ":" -f2 $datos`
