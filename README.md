# shopping-cart

With this application, store owners will be able to modernize and automate their checkout system.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Clone or download [remote repository](https://github.com/sshshana/shopping-cart). Choose a familiar download location such as Desktop.

Then navigate into the project repository:

```sh
cd ~/Desktop/shopping-cart
```

## Environment set up

It is possible to complete this project using the "base" Anaconda environment, because the basic requirements don't require any third-party packages. However if you eventually end up tackling bonus challenges that require third-party packages, then you'll want to create and activate a new Anaconda virtual environment, and use a "requirements.txt" file approach to installing your packages:

```sh
# IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt # the requirements.txt should have packages you want to install
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env" in order to utilize the third-party packages:
###### specify the third-party packages / features the user can activate

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Usage

Run the program and follow the instructions the system prompts:

```py
python shopping-cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment
