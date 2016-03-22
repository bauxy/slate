#!/usr/bin/env bash

rm -rf ./cache/*
touch ./cache/.gitkeep
bundle exec middleman build --clean