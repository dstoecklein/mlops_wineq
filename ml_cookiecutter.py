import os


def create_folders():
    folders = [
        os.path.join(".github", "workflows"),
        "artifacts",
        os.path.join("data", "raw"),
        os.path.join("data", "processed"),
        "data_remote",
        "notebooks",
        "prediction_service",
        os.path.join("prediction_service", "model"),
        "reports",
        "saved_models",
        "src",
        "tests",
        os.path.join("webapp", "static"),
        os.path.join("webapp", "static", "css"),
        os.path.join("webapp", "static", "script"),
        os.path.join("webapp", "templates")
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, ".gitkeep"), "w") as f:
            pass


def create_files():
    files = [
        "dvc.yaml",
        "config.yaml",
        "requirements.txt",
        "setup.py",
        "app.py",
        os.path.join("prediction_service", "__init__.py"),
        os.path.join("src", "__init__.py"),
        os.path.join("tests", "__init__.py"),
        os.path.join("tests", "conftest.py"),
        os.path.join("tests", "test_config.py"),
        os.path.join("webapp", "static", "css", "main.css"),
        os.path.join("webapp", "templates", "index.html"),
        os.path.join("webapp", "templates", "404.html"),
        os.path.join("webapp", "templates", "base.html"),
        os.path.join(".github", "workflows", "ci-cd.yaml")
    ]

    for file in files:
        with open(file, "w") as f:
            pass


if __name__ == "__main__":
    create_folders()
    create_files()
