# mlops
Simple ML application to practice MLOps

## 1. setting up the environment
- ``create remote repository``
- ``clone remote repository``
- ``conda activate <ENVIRONMENT>``
- ``pip install -r requirements.txt``
- ``python ml_cookiecutter.py``
- ``git init``

## 2. settting up DVC:
- ``dvc init``
- ``dvc add .\data_given\<DATA.csv>`` Need to do again when new data was added or updated
- ``dvc remote add -d storage gdrive://<REMOTE_ID>``
- ``dvc push`` pushes all tracked local files to remote storage
- ``dvc pull`` pulls the remote stored files
- ``dvc repro`` reproduces all stages defined in ``dvc.yaml``
- ``dvc remove <DATA.csv.dvc>`` stops tracking
- ``dvc gc -w`` remove data from its cache
- ``git checkout HEAD^1 .\data.dvc`` checkout to previous commited version of dvc
- ``dvc checkout``

## 3. setting up params.yaml config
- ``params.yaml`` holds information about the paths and model params

## 4. setting up dvc.yaml config
- ``dvc.yaml`` holds information about the stages which need to be tracked in order to reproduce them