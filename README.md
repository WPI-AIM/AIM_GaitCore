# About 
This is a core library for Vicon and GaitAnalysisToolkit.

# Installation
This library will be automatically installed when installing either Vicon or GaitAnalysisToolkit.
It can also be manually installed via pip:
```bash
pip install git+https://github.com/WPI-AIM/AIM_GaitCore.git
```

## Development Environment

Here is a suggested way to develop Python modules, specifically the AIM-Vicon module. For this section, I will be using the project's GitHub URL, but this should be replaced with your personal URL if you are forking and creating a pull request.

1. Clone the repository you will be working on.
``` bash
git clone git@github.com:WPI-AIM/AIM_GaitCore.git
```
**Note**: It is recommended to use a virtual environment. You can use `venv`, `pipenv`, `conda`, or anything else. This will keep the development environment separate from your main Python environment. Any new development won't affect the stable version of the module. For the sake of this tutorial, `conda` will be used, but you should be able to switch out the commands as you wish. If you are developing multiple VICON modules, you only need one environment. If you do not want to use a virtual environment, please skip to **Step 3**

2. Set up your virtual environment. If you are using Conda, you can use this command:
``` bash
conda create --name [environment_name] python=3.8
```
Alternatively, you can use the environment file in the repository:
``` bash
conda env create -f environment.yml
```
Make sure you enable the environment in every terminal you run code in by using the following command:
``` bash
conda activate aim-vicon-dev # Replace [aim-vicon-dev] with the name of your environment
```

3. Perform a Pip development install. This will create a `.egg-info` directory both in your pip install location and the root of your python module. Essentially this is a symbolic link pointing between your development environment and the Python module install directory, so that any changes you make to the module are immediately reflected in the installed module. Run this command to 'development install' the module

``` bash
pip install -e [location_of_module_setup.py]
pip install -e /home/user/development/AIM_GaitCore/. # An example
```

4. Time to write some code!