#!/usr/bin/env bash

DIR1="/opt/091224-ptm/Zashalovskiy/dir1"
DIR2="/opt/091224-ptm/Zashalovskiy/dir2"

mkdir -p "$DIR1"
mkdir -p "$DIR2"

for i in {1..100}; do
  file_name="$DIR1/$RANDOM"
  touch "$file_name"
done

for file in "$DIR1"/*; do
  filename=$(basename "$file")
  if ((filename % 2 == 0)); then
    mv "$file" "$DIR2/"
  fi
done
