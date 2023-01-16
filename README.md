# Code to create all diagrams and statements for the visual diagrams study

## Installation instructions on Ubuntu

1. Create a virtual environment with

    ```bash
    python3 -m venv env
    ```

    then

    ```bash
    source env/bin/activate
    ```

2. Run

    ```bash
    pip3 install -r requirements.txt
    ```

3. To get the Arial font for the visual diagrams run

   ```bash
   sudo apt install msttcorefonts -qq
   ```

   then

   ```bash
   rm ~/.cache/matplotlib -rf
   ```

4. This includes in the [`./fonts`](./fonts/) folder a Source Code Pro font for showing SQL. If you want to download the whole font package, run:

    ```bash
    wget https://github.com/adobe-fonts/source-code-pro/archive/2.030R-ro/1.050R-it.zip
    ```

    then

    ```bash
    unzip 1.050R-it.zip -d /fonts
    ```

    The code expects the font is available at [`./fonts/OTF/SourceCodePro-Regular.otf`](./fonts/OTF/SourceCodePro-Regular.otf)

## Run instructions

1. Change options in [`./create_all_diagrams_and_statements.py`](./create_all_diagrams_and_statements.py) according to what you want to create.

2. The code loads the question data from [`./data/input.csv`](./data/input.csv). Execute this to create the SQL and visual diagrams:

    ```bash
    python3 ./create_all_diagrams_and_statements.py
    ```

3. The generated SQL and visual diagram stimuli will be in [`./figs/`](./figs/). The generated JSON for the study will be in [`./data/output.json`](./data/output.json)

