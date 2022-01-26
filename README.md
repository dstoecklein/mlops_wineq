# mlops
Simple ML application to practice MLOps

## 1. step - setting up the environment
- ``create remote repository``
- ``clone remote repository``
- ``conda activate <ENVIRONMENT>``
- ``pip install -r requirements.txt``
- ``python ml_cookiecutter.py``
- ``git init``
- ``dvc init``
- ``dvc add .\data_given\<DATA.csv>``
- ``git add 'data_given\.gitignore' 'data_given\winequality.csv.dvc'``
- ``dvc remote add -d storage gdrive://<REMOTE_ID>``
- ``git add .dvc/config || git commit -m "configure remote storage"``
- ``dvc push``
- <click on link> & allow permission to access gdrive & paste verification code