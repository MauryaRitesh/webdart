# WebDart
Project for DevJam 2022

## Setup Project locally

1. Install [Python](https://www.python.org/).
2. Run the following commands in Terminal/CMD:
      ```bash
    git clone https://github.com/MauryaRitesh/webdart.git
    cd webdart
    ```
3. Create and activate a virtual environment.(can skip this step if you want to install the required dependencies gloabally).
   ### Ubuntu
    ```bash
    virtualenv myenv
    source myenv/bin/activate
    ```
    ### Windows
    ```bash
    python -m venv myenv
    myenv\Scripts\activate.bat  #CMD
    myenv\Scripts\Activate.ps1  #PowerShell
    ```
5. Using [pip](https://pip.pypa.io/en/stable/), install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Finally, start the django server: 
    ```bash
    python manage.py runserver
    ```
Now, go to http://127.0.0.1:8000/ in the browser!
