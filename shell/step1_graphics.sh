#!/bin/bash
cd ./pierre_in_frame &&
python3 step1_preprocessing.py from_file=YES file_name=food_graphics &&
python3 step1_preprocessing.py from_file=YES file_name=yelp_graphics &&
python3 step1_preprocessing.py from_file=YES file_name=ml-20m_graphics &&
python3 step1_preprocessing.py from_file=YES file_name=lfm-2b-subset_graphics