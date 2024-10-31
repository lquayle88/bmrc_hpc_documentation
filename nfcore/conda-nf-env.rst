.. _conda_nf_env:

Conda Environment
=================

Installing Nextflow and nf-core within a Conda environment using the system-wide miniconda module is currently the easiest way of making this software available for general use. The steps required to setup your conda environment are described below.

Login to BMRC HPC
-----------------

Connect via SSH after activating your VPN and login to a worker node via an interactive session:

.. code-block:: shell

  # login - substitute "username" with your own username
  ssh username@bmrc-hpc.shu.ac.uk

  # activate the modules flight env
  flight env deactivate
  flight env activate modules

  # request interactive session - prevents hanging while building conda env later
  srun --cpus-per-task=2 --mem=8G --pty bash -i

Create a nf-core Conda Environment
----------------------------------

This approach works with the most recent versions of nextflow (v23.10.1 at time of writing) and nf-core (v2.13.1 at time of writing).

Run the following commands in order and follow any prompts as appropriate:

.. code-block:: shell

  # load conda module
  module load apps/miniconda/24.9.2

  # make the "nf_env" environment
  conda create --name nf_env nextflow nf-core

Test the Conda Environment
--------------------------

You can now test the install has worked by running the following:

.. code-block:: shell

  # activate the environment
  source activate nf_env

  # test the environment is working
  nextflow info

  # test functionality
  nextflow run hello

You will notice if you run ``ls -al`` wherever you executed these commands (e.g., your ``$HOME`` directory) that a directory called ``work`` and a file ``nextflow.log`` have been created. You can remove these.

Create an Apptainer Image Cache
-------------------------------

Finally, you should create a specific cache for our apptainer containers to be pulled to which we can specify later in any pipeline driver job run script. Run the following command:

.. code-block:: shell

  mkdir $HOME/.apptainer

When you are finished, you can deactivate your conda environment using the command ``conda deactivate``.

Should you wish to unload the miniconda module you can do so by running ``module unload apps/miniconda/24.9.2``.
