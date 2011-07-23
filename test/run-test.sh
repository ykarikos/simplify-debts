#!/bin/sh

for f in `cd input; ls -1`; do ../src/simplify.py <input/$f 2>&1| diff -u output/$f -; done
