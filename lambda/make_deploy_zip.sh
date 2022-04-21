#!/usr/bin/env bash

rm deploy.zip
cd package
zip -r ../deploy.zip .
cd ..
zip -g deploy.zip comic.py
