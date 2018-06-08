#! /bin/bash

echo " Enter file name:"
read name

makefile () {
  make rv64ui-p-$name
}
makefile

spikef () {
 spike -l --isa=rv64g rv64ui-p-$name
}
spikef


logr () {
spike -l --isa=rv64g rv64ui-p-$name &> ~/log
gvim ~/log
}
logr


