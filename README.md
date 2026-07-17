# Mining Volve's Data Village

## About

This is an academic project that aims to explore and analyze the well data provided by Equinor ASA in their Volve Data Village. The project is structured as a Jupyter Notebook, allowing for interactive data analysis and visualization.

## Running the project

### 1. Download well data

If you already have the well data downloaded, you can skip this step.

> The scripts are written for Windows, but they can be easily adapted to other operating systems. To execute these steps you will need to have 7-Zip installed on your machine. You can download it from [here](https://www.7-zip.org/download.html).

1. Go to [Volve Data Village](https://marketplace.databricks.com/details/5c3558ef-315c-44dd-baef-7062ac301f22/Equinor-ASA_Volve-Data-Village) on Databricks Marketplace and click "Get Data" to download the well data. You will need to create a Databricks account if you don't have one already.
2. Go to `volve\Well_logs\01.MUD_LOG` and batch download the folders. Each folder is a well, and the folders will be downloaded as zip files with a `.zip` suffix.
3. Go to `volve\Well_logs\01.MWD_EWL` and batch download the folders. The folders will be downloaded as zip files with a `(1).zip` suffix (it is important to leave the number suffix, as the following scripts will use this to merge the data).
4. Move all the downloaded folders and zip files to a directory.
5. Copy the script `scripts/extract.bat` to that directory.
6. Run the `extract` script to unzip the directories. For each well, both folders will be merged into a single folder with the contents of both folders.
7. Copy the script `scripts/delete.bat` to that directory.
8. Run the `delete` script to remove the unnecessary files.
9. If all the steps were executed correctly, you can delete the original downloaded folders and zip files. You should be left with a single folder for each well.
10. Create a `wells` directory in the project root if it doesn't exist.
11. Finally, move all the well folders to the `wells` directory in the project root.

### 2. Install dependencies

It is recommended to use [Astral's uv][https://docs.astral.sh/uv/getting-started/installation/] to run this project. You can install it by following the instructions on the Astral website. Once you have uv installed, you can install the dependencies for this project by running the following command:

```bash
uv sync
```

If you prefer to use pip, you can install the dependencies by running the following command after activating your virtual environment:

```bash
pip install -r requirements.txt
```

### 3. Run migration

```bash
python db/migrate.py
```

### 4. Run the application

This is a Jupyter Notebook project. You can run the application by executing the following command:

```bash
uv run --with jupyter jupyter lab
```

or, if not using uv, you can run the following command:

```bash
jupyter lab
```

#### Using an IDE

If you prefer to use an IDE, you can open the project in your favorite IDE and run the Jupyter Notebook from there. Make sure to set the working directory to the project root and adjust your Python interpreter to the virtual environment where you installed the dependencies.

## LLM Usage

LLMs were used to assist in the development of this project. They were used to generate code snippets, provide suggestions for code improvements, and help with debugging. However, all code was reviewed and tested by the authors to ensure its correctness and functionality.
