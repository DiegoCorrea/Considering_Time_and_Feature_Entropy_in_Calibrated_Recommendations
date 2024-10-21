python3 step3_processing.py from_file=YES file_name=yelp > ../logs/step3_yelp.log &&
python3 step4_postprocessing.py from_file=YES file_name=yelp > ../logs/step4_yelp.log &&
python3 step5_metrics.py from_file=YES file_name=yelp > ../logs/step5_yelp.log