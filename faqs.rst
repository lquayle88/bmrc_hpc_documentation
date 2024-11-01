.. _faqs:

Frequently Asked Questions
==========================

In this section, we'll discuss solutions to common problems. Please work through these suggestions before reaching out for assistance.


Login and Connection Issues
---------------------------

Unable to Log In
^^^^^^^^^^^^^^^^

If you’re sure there’s no issue with your password or remote-access client but you still cannot log in, you may have exceeded your filestore quota on the cluster. If your ``$HOME`` area is full, critical system files may become corrupted, affecting login.

To resolve this:

1. Attempt to reset your environment with the following command, replacing variables as needed:

.. code-block:: shell

   ssh -t $USER@bmrc-hpc.shu.ac.uk 'resetenv -f'

2. If this doesn’t work, and you suspect your ``$HOME`` area is full, please contact `l.quayle@shu.ac.uk <mailto:l.quayle@shu.ac.uk>`_.

**Problems Connecting with WinSCP**

If you experience connection issues with WinSCP, try disabling ``Optimize Connection Buffer Size``:

1. Open WinSCP and go to ``Session -> Sites -> SiteManager``.
2. Select your site and click ``Edit``.
3. In the Advanced Site Settings, under ``Connection``, untick ``Optimize Connection Buffer Size``.


File and Disk Space Issues
--------------------------

Exceeding Disk Space Quota
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each user has a fixed disk space quota in their home directory. Exceeding this quota can cause problems, such as being unable to start applications or submit jobs.

To check if you’ve exceeded your quota, run:

.. code-block:: shell

   [user@node01 [bmrc-hpc] ~]$ quota -s

If you’ve reached your quota, delete files to free up space. If you can’t log in due to a full quota, contact `l.quayle@shu.ac.uk <mailto:l.quayle@shu.ac.uk>`_.

Windows-Style Line Endings
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prepare text files (e.g., job scripts) on Windows, they may not work on Unix due to line-ending differences. To convert Windows line endings to Unix, use ``dos2unix your_file``.

Terminal Issues
^^^^^^^^^^^^^^^

If commands aren’t working and only ``bash-4.1$`` appears instead of your username, you may have deleted your ``.bashrc`` or ``.bash_profile`` files, which are hidden files in your home directory.

To restore these files, use ``resetenv``.


Job Submission and Resource Issues
----------------------------------

Batch Job Terminates Without Messages or Warnings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a batch job started with ``sbatch`` terminates without messages, it may have exceeded its memory or runtime limits. Ensure you allocate sufficient resources when submitting the job.

Job Stuck in Queue or Pending (`PD`) for a Long Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To check why a job is pending, use ``squeue --reason``.

Common reasons include insufficient resources or dependencies on other jobs. Check if you have specified a constraint that limits available nodes.

Interactive Session Memory Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, an interactive session provides 2GB of RAM. To request more memory, use the ``srun`` command with a memory flag, e.g.:

.. code-block:: shell

   srun --cpus-per-task=2 --mem=8G --pty bash -i

This requests 8GB of RAM (real memory).

Failed Jobs Due to `OUT_OF_MEMORY` or `NODE_FAIL`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If jobs fail due to memory issues, ensure the requested memory is sufficient. Use Slurm's ``--mem`` flag to allocate memory explicitly.


Software Installation
---------------------

Using 'sudo' to Install Software on Clusters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users lack privileges to use ``sudo`` to install software. You can install applications in your ``$HOME`` directory or a sub-directory thereof. A guide for installation of user software and requesting installation will be provided in due course.
