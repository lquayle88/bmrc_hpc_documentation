.. _nfcore:

Running nf-core Pipelines
=========================

This guide describes the main steps required for setting up Nextflow and nf-core on the SHU BMRC Cluster

The simplest solution to running Nextflow and nfcore pipelines on the BMRC cluster while ensuring all dependencies are available and correctly managed is to install Nextflow and nf-core into a Conda environment. These processes are described as part of this guide.

.. toctree::
   :maxdepth: 2

   conda-nf-env
   project-setup-and-launch

A custom institutional configuration profile ``shu_bmrc`` has been provided for users of the SHU BMRC cluster which will automatically load pre-tested pipeline specific configurations to take care of resource requests for you.

For more information see `here <https://github.com/nf-core/configs/blob/master/docs/shu_bmrc.md>`_.
