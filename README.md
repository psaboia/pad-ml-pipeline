# PADs ML Pipeline

This is a machine learning pipeline for the PADs project. 
This repository contains a machine learning pipeline for the PADs project. The pipeline includes instructions and examples on how to download a dataset, perform analyses of PAD project samples using the PADs API, and set up a machine learning pipeline using DVC (Data Version Control).

## Requirements:
- Python 3.10
- PDM (*For instructions on how to install PDM, please refer to the [PDM documentation](https://pdm-project.org/latest/#recommended-installation-method).*)

## Setup

This is a git template repository. To use this template, click on the **"Use this template"** button at the top of the repository page. This will create a new repository with the same directory structure and files as this template. 

1. Start by cloning the new repository:
    ```bash
    git clone  git@github.com:<your-github-place>/pad-ml-pipeline.git
    cd pad-ml-pipeline
    ``` 

2. Install the dependencies by running the pdm command:
    ```bash
    pdm update
    ```

3. Now you can activate the virtual environment by running:
    ```bash
    source .venv/bin/activate
    ```

    For Windows(Power Shell):
    ```bash
    .venv/Scripts/activate.ps1
    ```
5. *(optional)* If you need to add more dependencies to your project, you can do so by running:
    ```bash
    pdm add <package-name>
    ```

Now you are ready to start using the PADs ML Pipeline.

## PADs Datasets

To list, import, and download the datasets used in the PADs Projects we use a DVC based data registry repository [https://github.com/PaperAnalyticalDeviceND/pad_dataset_registry](https://github.com/PaperAnalyticalDeviceND/pad_dataset_registry) to. See examples in the next sections.


### **Listing**

To explore the currently available datasets of this DVC data registry repository, you can run the `dvc list` command over the folder `datasets` as follows:

```bash
dvc list  https://github.com/PaperAnalyticalDeviceND/pad_dataset_registry datasets

```

### **Downloading**
You can download a specific dataset from the registry by running the `dvc get` command. It uses the same syntax as the `dvc import` command but doesn't save the dependency information.

To obtain the initial small example `CRSTest_dataset` dataset, execute the following command for downloading:

```bash
dvc get  https://github.com/PaperAnalyticalDeviceND/pad_dataset_registry datasets/CRSTest_dataset
```

## Project Data Analysis using PADs API

[todo]

## ML experiments using DVC
[todo]
