# MLOps
Simple ML application to practice MLOps

# Development

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
- create custom ``exceptions`` if needed (see 7)


## 6. setting up setup file
- ``setup.py`` makes the project a package
- ``pip install -e .`` installs local package (own defined project)
- - ``-e .`` can also be mentioned in ``requirements.txt``
- ``pip freeze`` will now show own project in installed packages
- ``import <PROJECT>`` can now import the project in any other project

## 7. setting up schema & exceptions
- In notebooks, create a schema for ``min-max`` values. This will be important for the frontend. Preferably as json
- Create custom ``Exceptions`` for frontend

## 8. setting up linting
- checks if python files follows style and naming convention
- mention ``flake8 . --count --selectE9, F63, F7, F82 --show-source --statistics`` and ``flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics`` in ``tox.ini``

## 9. setting up prediction service
- create a simple web frontend using ``flask``
- ``app.py`` hold flask application
- ``model.joblib`` has to have the saved model to use
- TODO SAVE MODEL IN PREDICTION SERVICE

# Deployment

## 1. create ci/cd workflow (Github actions)
- create ``.github/workflows/`` folder
- create ``ci-cd.yaml`` file
- Reminder: Now we can use ``tox`` in development for testing and production testing will be done by github actions

## 2. deployment to Heroku
- Create heroku app and link to github repo
- Go to Github ``secrets`` and add ``HEROKU_API_NAME`` and ``HEROKU_API_TOKEN``
- Create ``Procfile``: Heroku will search for this file and run app 
- - specify which server and which app it needs to run


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
- Simple feature engineering
- Load remote data
- Track changes on data, model (dvc) and code (git)
- Model training and evaluation
- Save models and metrics
- Testing (flake8, pytest, tox)
- CI/CD (Github actions)
- Deployment (Heroku)
- Advanced tracking (MLFlow)

# What is not covered?
- Data analysis
- Feature selection
- Containerizing (Docker)
- Monitoring / Drifts
- Automated retraining (Continuous training)