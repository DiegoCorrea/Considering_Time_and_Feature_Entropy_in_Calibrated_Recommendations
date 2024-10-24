#!/bin/bash
cd ./pierre_in_frame &&
python3 step1_preprocessing.py from_file=YES file_name=yelp &&
python3 step1_preprocessing.py from_file=YES file_name=yelp_distribution &&
python3 step1_preprocessing.py from_file=YES file_name=yelp_analyze &&

python3 step2_searches.py from_file=YES file_name=yelp &&

python3 step3_processing.py from_file=YES file_name=yelp > ../logs/step3_yelp.log &&
python3 step4_postprocessing.py from_file=YES file_name=yelp > ../logs/step4_yelp.log &&
python3 step5_metrics.py from_file=YES file_name=yelp > ../logs/step5_yelp.log