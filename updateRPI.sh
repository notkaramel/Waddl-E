#!/usr/bin/bash

echo "make sure you're on SummerRain branch"
echo "and connected to dpm-18 wifi"

git add -A
echo "Your update message: "
read -r message
git commit -m "$message"

git checkout rpi && git merge SummerRain
git push origin && git checkout SummerRain
echo "Closing window in 3s"
sleep 3s


