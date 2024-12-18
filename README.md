# Pierre-in-Frame  

## This is the code for the paper "Considering Time and Feature Entropy in Calibrated Recommendations" authored by Diego Corrêa da Silva, Dietmar Jannach and Frederico Araújo Durão.   

## You can download the dataset and results to reproduce the experiment and compare at: https://doi.org/10.5281/zenodo.14228378

[Pre-Print](https://readthedocs.io/) | [Paper](https://doi.org/xx.xxx/xxxxx.xxxxxx)  

[![Version](https://img.shields.io/badge/version-v0.2-green)](https://github.com/project-pierre/pierre-in-frame) ![PyPI - Python Version](https://img.shields.io/badge/python-3.8-blue)  

[![logo](MethodologyWorkflow.svg)](https://project-pierre.github.io/project-pierre)  

Pierre-in-Frame is a recommendation system framework focused on multiple objectives. The framework combines other recommendation systems and machine learning libraries, such as Scikit-Surprise, Scikit-Pierre, and Scikit-learn.
It is constructed to be focused on providing a way to create recommendation systems with more than one objective, such as calibration, diversity, etc.
In version 0.1, the framework implements seven collaborative filtering algorithms for processing and the concept of calibration for post-processing.
Pierre-in-Frame is composed of **seven steps**, implementing the concept of automatic recommender systems.  

## Preparing  
1. Update and upgrade the OS: `sudo apt update && sudo apt upgrade -y && sudo apt install curl`  
2. Download Anaconda: `curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh`   
3. Install Anaconda: `bash Anaconda3-2023.09-0-Linux-x86_64.sh`  
 
## The code
1. Download the framework: `https://github.com/DiegoCorrea/Considering_Time_and_Feature_Entropy_in_Calibrated_Recommendations`  
2. Go to the framework path: `cd Considering_Time_and_Feature_Entropy_in_Calibrated_Recommendations/`  
3. The framework structure: `ls .`  
3.1. `pierre_in_frame/`: Where all python code is. It is the kernel of the framework code.  
3.2. `data/`: Where all data are saved as raw and clean datasets, candidate items, recommendation lists, execution time, etc.  
3.3. `docs/`: The documentation directory to be used on the readthedocs. **TODO: It is a future work**.  
3.4. `environment/`: It is used to save all framework environment files. 
3.5. `logs/`: This directory is generated after the first run. The log path is used to save the code status.  
3.6. `metadata/`: Metadata about the framework.  
3.7. `results/`: The result files will be saved inside this diretory, as well as tables, figures, etc.  
3.8. `shell/`: Examples of how-to-run experiments in a Linux shell.  

## Conda Environment
1. Load the conda environment: `conda env create -f environment.yml`    
2. Start the conda environment: `conda activate pierre-in-frame`  
   3.1. It is also possible to install it through pip requirements  
3. Download, compile, and install the `Project Pierre` libraries  
   3.1. Download Scikit-Pierre, compile, and install it: `https://github.com/project-pierre/scikit_pierre`  
   3.2. Download Recommender-Pierre, compile, and install it: `https://github.com/project-pierre/recommender-pierre`  
4. By default, we provide in this repository the compiled library wheel
   4.1. To install Scikit-Pierre: `pip install scikit_pierre-0.0.1-cp38-cp38-linux_x86_64.whl`  
   4.2. To install Recommender-Pierre: `pip install recommender_pierre-0.0.1-cp38-cp38-linux_x86_64.whl`  
   4.3. If version conflict happens, you may try:  
      4.3.1. To install Scikit-Pierre: `pip install scikit_pierre-0.0.1-cp38-cp38-linux_x86_64.whl --force-reinstall --no-dependencies`  
      4.3.2. To install Recommender-Pierre: `pip install recommender_pierre-0.0.1-cp38-cp38-linux_x86_64.whl --force-reinstall --no-dependencies`  

## Using the framework
To run the framework it is necessary to go to the following directory: `cd pierre_in_frame/`. 
Inside this directory are seven Python scripts. Each script has a set of parameters that are necessary to run.    

### Step 1: Pre-processing
The pre-processing step is implemented to clean, filter, and model the data.
The framework pre-processes the dataset to provide a structure to be used in all the next steps.
It applies data partitioning of your choice. We have implemented four pre-processing validation methods.
The pre-processing script provides three functionality to configure the experiment:  
1. Pre-process based on validation method  
   1.1. MovieLens 20M: `python3 step1_preprocessing.py from_file=YES file_name=ml-20m`  
   1.2. Food.com: `python3 step1_preprocessing.py from_file=YES file_name=food`  
   1.3. Last.fm 2B: `python3 step1_preprocessing.py from_file=YES file_name=lfm-2b-subset`  
   1.3. Yelp: `python3 step1_preprocessing.py from_file=YES file_name=yelp`  
2. Pre-Compute Distribution. This improves the execution time. **We strongly indicate running this optimization**  
   2.1. MovieLens 20M: `python3 step1_preprocessing.py from_file=YES file_name=ml-20m_distribution`  
   2.2. Food.com: `python3 step1_preprocessing.py from_file=YES file_name=food_distribution`  
   2.3. Last.fm 2B: `python3 step1_preprocessing.py from_file=YES file_name=lfm-2b-subset_distribution`  
   2.4. Yelp: `python3 step1_preprocessing.py from_file=YES file_name=yelp_distribution`  
3. Pre-Compute One-Hot-Encoding. This improves the execution time. **We strongly indicate running this optimization**  
   3.1. MovieLens 20M: `python3 step1_preprocessing.py from_file=YES file_name=ml-20m_ohe`  
   3.2. Food.com: `python3 step1_preprocessing.py from_file=YES file_name=food_ohe`  
   3.3. Last.fm 2B: `python3 step1_preprocessing.py from_file=YES file_name=lfm-2b-subset_ohe`  
   3.4. Yelp: `python3 step1_preprocessing.py from_file=YES file_name=yelp_ohe`  

You can find the environment files from step 1 in the `environment/step1/` directory.  

#### Run Examples
In the directory `shell`, there are examples of scripts to run step 1 for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step1.sh > ./logs/step1.log 2>&1 & disown`.
It will run all step 1 commands shown above.  

### Step 2: Best Parameter Search
This step applies the Random Search method to find the best set of hyperparameters.
The best set of parameter values is saved inside the path `data/experiment/hyperparameters/<dataset_name>/`.  

#### Run Examples
1. MovieLens 20M   
   1.1. CVTT + BPR + ALS: `python3 step2_searches.py from_file=YES file_name=ml-20m`    
   1.2. CVTT + DeepAE: `python3 step2_searches.py from_file=YES file_name=deep_ae_ml-20m`    
2. Food.com Recipes    
   1.1. CVTT + BPR + ALS: `python3 step2_searches.py from_file=YES file_name=food`    
   1.2. CVTT + DeepAE: `python3 step2_searches.py from_file=YES file_name=deep_ae_food`     
3. Last.fm    
   1.1. CVTT + BPR + ALS: `python3 step2_searches.py from_file=YES file_name=lfm-2b-subset`    
   1.2. CVTT + DeepAE: `python3 step2_searches.py from_file=YES file_name=deep_ae_lfm-2b-subset` 
4. Yelp    
   1.1. CVTT + BPR + ALS: `python3 step2_searches.py from_file=YES file_name=yelp`    
   1.2. CVTT + DeepAE: `python3 step2_searches.py from_file=YES file_name=deep_ae_yelp`    

In the directory `shell`, there are examples of scripts to run step 2 for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step2.sh > ./logs/step2.log 2>&1 & disown`.
It will run all step 2 commands shown above.  

### Step 3: Processing
The processing step uses the pre-processed data and the hyperparameters to train the chosen recommender algorithm.
The prediction generates a set of candidate items to be used in the post-processing step.
All candidate items set are saved inside `data/experiment/{dataset}/candidate_items/{recommender}/trial-{trial}/fold-{fold}/candidate_items.csv`.  

#### Run Examples

1. MovieLens 20M   
   1.1. BPR + ALS: `python3 step3_processing.py from_file=YES file_name=ml-20m`    
   1.2. DeepAE: `python3 step3_processing.py from_file=YES file_name=deep_ae_ml-20m`    
2. Food.com Recipes    
   1.1. BPR + ALS: `python3 step3_processing.py from_file=YES file_name=food`    
   1.2. DeepAE: `python3 step3_processing.py from_file=YES file_name=deep_ae_food`     
3. Last.fm    
   1.1. BPR + ALS: `python3 step3_processing.py from_file=YES file_name=lfm-2b-subset`    
   1.2. DeepAE: `python3 step3_processing.py from_file=YES file_name=deep_ae_lfm-2b-subset`       
4. Yelp    
   1.1. BPR + ALS: `python3 step3_processing.py from_file=YES file_name=yelp`    
   1.2. DeepAE: `python3 step3_processing.py from_file=YES file_name=deep_ae_yelp`  

In the directory `shell`, there are examples of scripts to run step 3 for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step3.sh > ./logs/step3.log 2>&1 & disown`.
It will run all step 3 commands shown above.  

### Step 4: Post-processing
Post-processing is the focus of this framework. We use the Scikit-Pierre library to post-process the candidate items given by the recommender algorithms provided by Scikit-Surprise or other recommender libraries.
The parameters given from the command line are used to create one or more recommendation systems. Using the same candidate items set as entries to different post-processing formulations is possible.
The recommendations produced by this step are saved in `data/experiment/<dataset_name>/recommendation_lists/`.  

#### Run Examples
1. MovieLens 20M: `python3 step4_postprocessing.py from_file=YES file_name=ml-20m`    
2. Food.com Recipes: `python3 step4_postprocessing.py from_file=YES file_name=food`     
3. Last.fm: `python3 step4_postprocessing.py from_file=YES file_name=lfm-2b-subset`  
4. Yelp: `python3 step4_postprocessing.py from_file=YES file_name=yelp`  

In the directory `shell`, there are examples of scripts to run the **step 4** for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step4.sh > ./logs/step4.log 2>&1 & disown`.
It will run all step 4 commands shown above.  

### Step 5: Metric
In the Metric step, the recommendation lists produced by the post-processing procedure are evaluated.
In version 0.1, the framework provides five metrics: **TIME**, **MAP**, **MRR**, **MACE** and **MRMC**.
In version 0.2, the framework provides new metrics: **ILS**, **COVERAGE**, **UNEXPECTED**, **SERENDIPITY** and **MAMC**.
Scikit-Pierre provides all metrics. Scikit-Surprise provides other metrics, so it is possible to call these, too.
The system you want to evaluate is given the same parameters as in the post-processing step.  

#### Run Examples
1. MovieLens 20M: `python3 step5_metrics.py from_file=YES file_name=ml-20m`    
2. Food.com Recipes: `python3 step5_metrics.py from_file=YES file_name=food`     
3. Last.fm: `python3 step5_metrics.py from_file=YES file_name=lfm-2b-subset`   
4. Yelp: `python3 step5_metrics.py from_file=YES file_name=yelp`  

In the directory `shell`, there are examples of scripts to run **step 5** for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step5.sh > ./logs/step5.log 2>&1 & disown`.
It will run all step 5 commands shown above.  

### Step 6: Protocol
The protocol step compiles all metrics results, applying an average along the trials and folds.
The final values are the system's performance in each metric.
Coefficients are applied as a new metric. We inherit the coefficients from Scikit-Pierre.
The final file is saved inside: `results/decision/{dataset}/decision.csv`.  

#### Run Examples
1. MovieLens 20M: `python3 step6_protocol.py from_file=YES file_name=ml-20m`    
2. Food.com Recipes: `python3 step6_protocol.py from_file=YES file_name=food`     
3. Last.fm: `python3 step6_protocol.py from_file=YES file_name=lfm-2b-subset`  
4. Yelp: `python3 step6_protocol.py from_file=YES file_name=yelp`  

In the directory `shell`, there are examples of scripts to run the **step 6** for the three datasets cited above.
You can run the command from the main project directory: `sh shell/step6.sh > ./logs/step6.log 2>&1 & disown`.
It will run all step 6 commands shown above.  

### Step 7: Charts
The Chart step uses the compiled raw results from the Protocol step to produce figures, tables, comparisons, and research questions.
It is the last step in the framework. The result files are saved inside: `results/graphics/results/{dataset}/{filename}`.  

#### Run Examples
1. MovieLens 20M: `python3 step7_charts_tables.py from_file=YES file_name=ml-20m`    
2. Food.com Recipes: `python3 step7_charts_tables.py from_file=YES file_name=food`     
3. Last.fm: `python3 step7_charts_tables.py from_file=YES file_name=lfm-2b-subset`
4. Yelp: `python3 step7_charts_tables.py from_file=YES file_name=yelp`  
