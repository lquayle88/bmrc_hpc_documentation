.. _connecting:

Connecting to the Cluster
=========================

In order to run commands and submit jobs on the HPC is to use a mechanism called `SSH <https://en.wikipedia.org/wiki/Secure_Shell>`_, which is a common way of remotely logging in to computers running the Unix-based and Linux operating system.

To connect to another machine using SSH you need to have a SSH *client* program installed on your machine. MacOS and Linux come with a command-line (text-only) SSH client pre-installed. On Windows there are various graphical SSH clients you can use, including *MobaXTerm*.

**Whether/how you can connect** to a University cluster using SSH (or the related protocols SCP and SFTP) **depends on**:

* Where you are connecting from:

  * on campus using wired ethernet
  * on campus using SHU-USS/SHU-USSL or SHU-TSS (Staff SHU managed machines only)
  * on campus using Eduroam *after* establishing a `VPN <https://www.shu.ac.uk/digital-skills/programs-and-applications/virtual-private-network-vpn>`_ connection (required)
  * off campus *after* establishing a `VPN <https://www.shu.ac.uk/digital-skills/programs-and-applications/virtual-private-network-vpn>`_ connection (required)

.. warning::

    Eduroam does not grant access to the clusters. If using Eduroam, you must keep the `VPN <https://www.shu.ac.uk/digital-skills/programs-and-applications/virtual-private-network-vpn>`_ connected at all times while using the cluster.


SSH Client Software on Windows
------------------------------

Modern Windows versions come with built-in OpenSSH capabilities integrated into PowerShell, allowing users to use ``ssh`` commands natively. However, for those that do not have powershell, popular alternatives are:

1. **PuTTY**
   
   `PuTTY <https://www.putty.org/>`_ is one of the most popular and widely used SSH clients for Windows. It is lightweight, open-source, and offers features for secure remote access and file transfers.

2. **MobaXterm**
   
   `MobaXterm <https://mobaxterm.mobatek.net/>`_ is a comprehensive all-in-one tool that provides not only SSH capabilities but also features such as a built-in X11 server, remote session management, and support for various network protocols.

Running commands from a terminal (command-line) may initially be unfamiliar to Windows users but this is the recommended approach for interfacing with the Linux operating system of the cluster.


SSH Client Software on MacOS and Linux
--------------------------------------

Linux and MacOS both typically come with a command-line SSH client pre-installed that can be used through the terminal (e.g. *Gnome Terminal* on Linux or *Terminal* on macOS).

If you are a Mac user and want to be able to run graphical applications on the clusters then you need to install the latest version of the `XQuartz <https://www.xquartz.org/>`_.


Establishing a SSH connection
-----------------------------

Once you have a terminal open run the following command: ``ssh username@bmrc-hpc.shu.ac.uk`` ensuring that you replace *username* with your own.

After typing in this command hit enter to start connecting at which point you will be prompted for your username and password; this will not be visible during typing.

This should give you a prompt resembling the one below: 

.. code-block:: console

    [username@login1 [bmrc-hpc] ~]$

At this prompt type: 

.. code-block:: console

    srun --pty bash -i

Like this: 

.. code-block:: console

    [username@login1 [bmrc-hpc] ~]$ srun --pty bash -i

Which will start an interactive session preventing you running any tasks on the login nodes.

.. note::

    When you login to a cluster you reach a login node. You **should not** run applications on login nodes. Running the interactive job command gives you an interactive terminal on one of the many worker nodes in the clusters.


Connection Tips
===============

Here are some techniques you can use to reduce the number of times that you need to re-authenticate to the HPC system.  


Reuse SSH Connections
---------------------

Many SSH clients can reuse existing SSH sessions for new connections without the need to reconnect.  Some clients also allow sessions to persist temporarily after you have closed all your terminal windows to allow you to easily reconnect for a short time without having to reauthenticate.

SSH Clients
^^^^^^^^^^^

SSH has a built in functionality to reuse existing connections for new sessions. You can enable this feature by adding the following config to your `~/.ssh/config` file on your local PC:

.. code-block:: console

   Host bmrc-hpc.shu.ac.uk
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 600

You will need to create the directory ``~/.ssh/sockets`` before running ssh.  The ``ControlPersist`` option allows you to specify how long (in seconds) your SSH connection should perist after you have closed all your existing sessions.  During this time you can start a new session without reauthenticating.

.. warning::

    If you configure your SSH client to maintain connections ensure that your client PC is kept locked whenever you leave it unattended.  

.. warning::

    If you are temporarily disconnected from the network you may find that your SSH session does not immediately detect the failure.  You can delete the control socket created in `~/.ssh/sockets` in order to clear the session and reconnect.  You should not use this option when running SSH commands on remote systems.

Putty
^^^^^
You can configure Putty to ``Share SSH connections if possible`` via the ``SSH`` option in the ``Connection Catagory`` when configuring a new connection.

As long as your existing connection remains active you can start new sessions without reautenticating by using ``Duplicate Session`` command to start new sessions.

Other applications which use Putty for SSH connections can also re-use your existing connection without needing to reauthenticate.

.. note::

    If you perform a large file transfer over a shared session you may find that other sessions sharing the same connection become less responsive.


TMUX/screen
-----------

`TMUX <https://github.com/tmux/tmux/wiki>`_ and `screen <https://www.gnu.org/software/screen/manual/screen.html>`_ can be used to run multiple shell sessions within a single SSH session.

For examples of using TMUX to manage mutiple sessions see the following blog post: `tmux: remote terminal management and multiplexing <https://rse.shef.ac.uk/blog/tmux-intro/>`_.
