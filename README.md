# shopping-cart
With this application, store owners will be able to modernize and automate their checkout system.

## Prerequisites
  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](https://github.com/sshshana/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer. Choose a familiar download location such as Desktop.

Then navigate there from the command line (subsequent commands assume you downloaded the remote copy onto the Desktop):

```sh
cd ~/Desktop/shopping-cart
```

## environment set up - for advanced features
Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env" in order to utilize the third-party packages:
###### specify the third-party packages / features the user can activate

```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)


