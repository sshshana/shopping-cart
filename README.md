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

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```
In your new virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In your project repository, update sales_tax_rate variable in the ".env" file according to your city's sales tax rate. Please see the exmaple below (which assumes the tax rate is 8.75%):

```sh
sales_tax_rate=8.75
```
> NOTE: Do not include percentage sign (%) in the code
> NOTE: If you don't customize your tax rate, it will be use New York City's sales tax rate of 8.75%


## Usage
Run the program and follow the instructions the system prompts:

```py
python shopping-cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment
