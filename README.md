# MLOps
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
- ``dvc repro`` to run all stages. It will create a ``dvc.lock`` file - it will track the defined dependencies on which the stage depend on. If ``dvc repro`` ran again, it will recognize that there are no changes.
- ``dvc metrics show`` shows the metrics stored in files as defined in ``dvc.yaml``
- ``dvc metric diff`` shows different from the past experiments
- ``dvc params diff`` shows the different parameters used and tracked by dvc defined in ``dvc.yaml``

## 5. setting up testing part
- ``tox`` creates a virtual environment to check if all packages are installed correctly etc. ``PyTest`` basically unit testing for python. Utilize both for automated testing
- ``tox.ini`` holds information about the virtual environments
- - ``skipsdist = True`` skips ``setup.py``
- ``conftest.py``
- ``test_config.py`` holds the acutal tests
- - ``def test_XXX`` is the name convention
- ``tox`` command will run the defined testenv and its commands (for example ``pytest -v``).
- ``tox -r`` will rebuild the virtual environment


## 6. setting up setup file
- ``setup.py`` makes the project a package
- ``pip install -e .`` installs local package (own defined project)
- - ``-e .`` can also be mentioned in ``requirements.txt``
- ``pip freeze`` will now show own project in installed packages
- ``import <PROJECT>`` can now import the project in any other project

# DVC stages:

## Stage 1
- Retrieving data from remote storage, which is dvc tracked
- Load data into data/raw

## Stage 2
- Train, test split from data/raw
- save splitted data in data/processed

## Stage 3
- Model training
- Evaluation
- Save metrics (as json) and model itself (as joblib)
- ``dvc metrics show`` shows the metrics as defined in dvc.yaml
- ``dvc metrics diff`` shows difference of previous experiments. ``HEAD`` is the previous experiment, ``workspace`` the current

| Path | Metric | HEAD | workspace |Change |
|-|-|-|-|-|
|reports\metrics.json | mae      |   0.65656 | 0.64716  | -0.00939 |
|reports\metrics.json | r2       |   0.01971 | 0.03934  |  0.01962 |
|reports\metrics.json | rmse     |   0.78837 | 0.78044  | -0.00793 |
|reports\params.json  | alpha    |   0.88    | 0.5      | -0.38 |
|reports\params.json  | l1_ratio |   0.89    | 0.68     | -0.21 |


# What is covered?
- Load remote data
- Track changes on data, model (dvc) and code (git)