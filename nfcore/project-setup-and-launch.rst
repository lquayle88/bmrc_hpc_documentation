.. _project_setup_and_launch:

Project Setup and Launch
========================

Setup your Project Directories
------------------------------

The assumed project sub-directory structure within this guide is as follows:

.. code-block:: 

  /users/$USER/projects/yyyy_mm_dd_project_name/
  |-- data
  |   |-- raw
  |   |-- reference
  |   `-- sample_sheet
  |-- results
  `-- src
      |-- nf_config
      |-- nf_params
      `-- shell

This directory tree can be established by running the command shown below from within the ``/users/$USER`` directory.

.. code-block:: shell

  # setup the project directory tree
  mkdir -p ./projects/yyyy_mm_dd_project_name/{data/{raw,reference,sample_sheet},results,src/{nf_config,nf_params,shell}}

Run Configuration
-----------------

Many nf-core pipelines require a sample sheet detailing the files you wish to analyse. You can find nf-core pipelines by visiting `https://nf-co.re/pipelines <https://nf-co.re/pipelines>`_. Each pipeline page has more information on how to use the pipeline as well as a full description of sample sheet requirements and formatting.

Your sample sheet should be located inside your ``sample_sheet`` sub-directory.

There are two other things you will require to run an nf-core pipeline:

1. A pipeline launcher parameter configuration file
2. A submission script

The general launch command in the script template provided here assumes you have configured your specific run using an nf-core pipeline launcher. For example, the launcher for the nf-core/rnaseq pipeline that can be found `here <https://nf-co.re/launch?pipeline=rnaseq>`_. The parameters specified for your run using the launcher should be saved in a file named ``nf-params.json`` within the ``nf_params`` sub-directory.

To create your run script, navigate to the ``script`` sub-directory and run the following:

.. code-block:: shell

  emacs nf_run.sh

Paste the contents of the template file linked below into the editor ensuring to change the generic information for your own where indicated in the comment lines.

.. code-block:: shell

  #!/bin/bash

  ## scheduler flags

  # job name  >>> edit "pipeline_name" for the name of the pipeline you are running e.g. rnaseq <<<
  #SBATCH --job-name=pipeline_name

  # request resources for the nextflow driver job
  #SBATCH --cpus-per-task=1
  #SBATCH --mem=3G

  # send email >>> edit username <<<
  #SBATCH --mail-user=username@shu.ac.uk
  #SBATCH --mail-type=BEGIN,END,FAIL

  # output log file
  #SBATCH --output=nextflow.log


  ## load dependencies

  # system modules
  module purge
  module load apps/apptainer/1.3.4
  module load apps/miniconda/24.9.2

  # activate analysis environment
  source activate nf_env


  ## export variables

  # prevent java vm requesting too much memory and killing run
  export NXF_OPTS="-Xms1g -Xmx2g"

  # path to apptainer cache
  export NXF_APPTAINER_CACHEDIR="/users/$USER/.apptainer"

  # path to project directory >>> edit so that this points to your project root directory <<<
  NF_PROJECT="/path/to/project/yyyy_mm_dd_project_name"

  # project directories
  WORK_DIR="/tmp/users/$USER/nf_work"
  PARAM_DIR="${NF_PROJECT}/src/nf_params"

  # for custom configuration - can be ignored or deleted
  # CONF_DIR="${NF_PROJECT}/src/nf_config"


  ## run command  >>> edit "pipeline", "version" and "profile" <<<

  nextflow run nf-core/pipeline \
  -r version \
  -profile profile \
  -work-dir $WORK_DIR \
  -resume \
  -params-file ${PARAM_DIR}/nf-params.json  

  # for custom configuration - can be ignored or deleted
  # -c ${CONF_DIR}/custom.config

Now save and exit by typing "Ctrl + X" then "Ctrl + S" then "Ctrl + X" followed by "Ctrl + C".

Batch Job Submission
--------------------

Once you have fulfilled all of the requirements in the earlier steps in this guide, you should be ready to submit your batch job to the Slurm scheduler. From the project root, type the following:

.. code-block:: shell

  sbatch ./src/shell/nf_run.sh

Your pipeline run should start momentarily. Good Luck!
