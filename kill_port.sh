#!/usr/bin/env bash

kill $(echo $PWD_BHAUGEN | sudo -S lsof -i -P -n | grep "\[\:\:1]:$1" | cut -c11-15)
