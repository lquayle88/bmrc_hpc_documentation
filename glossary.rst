
Glossary of HPC Terms
=====================

The worlds of scientific and high performance computing are full of technical jargon that can seem daunting to newcomers. This glossary attempts to explain some of the most common HPC terms.

.. glossary::

    Accelerator
        A specialised hardware component, such as a GPU (Graphics Processing Unit) or FPGA (Field-Programmable Gate Array), designed to perform specific computations faster than a CPU by executing parallel tasks.

    API
        Application Programming Interface; a set of protocols and tools that allows different software applications to communicate with each other, commonly used to enable access to HPC resources.

    Bash
        Bourne Again Shell; a popular Unix shell and command language often used in HPC environments for scripting and automating tasks. Bash is widely supported and provides a range of tools for file manipulation, job control, and process management.

    Batch Processing
        A method of processing where jobs are collected into groups (batches) and executed without manual intervention, commonly managed by a job scheduler.

    Benchmark
        A performance test to evaluate the speed, efficiency, or other aspects of HPC systems or applications, helping assess relative performance for various tasks.

    Checkpointing
        A process in which an application's state is saved at specific intervals, allowing a job to resume from the last checkpoint in case of a failure, essential in long-running HPC tasks.

    Cluster
        A collection of interconnected computers, or nodes, that work together as a single system to provide high performance, reliability, and scalability. Clusters are the backbone of most HPC environments.

    Cloud Computing
        The delivery of computational services, such as processing power and storage, over the internet, allowing users to access resources on demand without owning hardware.

    Compute Node
        An individual server or machine within a cluster that performs the primary computational tasks assigned to it.

    Container
        A lightweight, portable unit that packages an application and its dependencies, enabling it to run consistently across different environments, often used to simplify deployment in HPC.

    Core
        A single processing unit within a CPU, capable of executing tasks. Modern CPUs often contain multiple cores, which enable parallel task processing.

    CPU
        Central Processing Unit; the primary component in a computer that handles general-purpose computations and task management.

    Data Parallelism
        A form of parallel computing in which data is divided into parts and processed simultaneously across multiple processors, commonly used in machine learning and scientific simulations.

    Distributed Computing
        A computing approach in which a task is split and executed across multiple computers that communicate and collaborate to complete it faster and more efficiently.

    FPGA
        Field-Programmable Gate Array; a type of accelerator that can be configured by the user after manufacturing to perform specific tasks, often used in HPC for custom processing.

    GPU
        Graphics Processing Unit; initially developed for rendering graphics but now widely used in HPC for its ability to handle multiple calculations simultaneously, ideal for data-intensive applications.

    Heterogeneous Computing
        An approach that combines different types of processors (such as CPUs, GPUs, and FPGAs) in a single system to maximise performance by utilising each processor’s strengths.

    High Availability
        The ability of a system to operate continuously without failure for a long period, critical in HPC environments to prevent downtime during large computations.

    InfiniBand
        A high-speed communication protocol widely used in HPC clusters for its low latency and high bandwidth, making it ideal for data-intensive applications.

    Interconnect
        A high-speed network connecting nodes in a cluster to facilitate fast data transfer between them, often essential for high-performance tasks.

    I/O (Input/Output)
        Operations that transfer data between the computer’s memory and external systems or storage, crucial in HPC where large datasets need to be moved efficiently.

    Job Scheduler
        A system that manages the allocation of resources and orchestrates job execution within a cluster, often based on priority, dependencies, and resource requirements.

    Load Balancing
        The practice of distributing tasks across resources to ensure optimal performance and prevent any single component from being overloaded.

    Memory Bandwidth
        The rate at which data can be read from or written to memory by the processor, a crucial factor in HPC where large datasets need to be accessed quickly.

    MPI
        Message Passing Interface; a protocol that enables communication between processors, allowing them to coordinate and execute parallel computations across nodes.

    Node
        A single computer within an HPC cluster, usually tasked with performing a designated subset of computational work.

    OpenMP
        Open Multi-Processing; a programming interface that supports multi-platform shared memory multiprocessing, often used to create parallel applications for HPC environments.

    Parallel Processing
        The simultaneous execution of multiple tasks or calculations, either within a single processor or across multiple processors, to speed up computation.

    Queue
        A system that organises jobs waiting for execution based on resource availability, priority, and other scheduling policies.

    RDMA
        Remote Direct Memory Access; a technology that allows data to be transferred directly between the memory of different computers without CPU intervention, optimising speed in HPC networks.

    Resilience
        The ability of an HPC system to withstand faults and continue operating, especially vital in long computations that must manage component failures without losing progress.

    Scalability
        The capacity of a system to increase its performance and workload handling by adding more resources, such as nodes, processors, or memory.

    Scheduler
        A system that manages the allocation of resources and orchestrates job execution within a cluster, often based on priority, dependencies, and resource requirements.

    Scratch Storage
        Temporary storage space on an HPC system where users can keep data needed for a particular job, typically cleared after the job completes to free up space.

    Shared Memory
        A memory architecture where multiple processors access the same memory space, allowing faster data sharing but often requiring careful management to avoid conflicts.

    SLURM
        Simple Linux Utility for Resource Management; a job scheduler widely used in HPC environments for allocating resources and managing job queues.

    Supercomputer
        A high-performance computer capable of executing billions or trillions of calculations per second, typically used for advanced scientific simulations and research.

    Throughput
        The number of tasks or computations a system can process within a specific time period, an important metric in assessing HPC performance.

    Vectorisation
        The process of converting algorithms to use vector operations, allowing simultaneous processing of data elements, which is especially advantageous in scientific and engineering applications.

    Vector Processor
        A processor that handles multiple data points simultaneously, often used in scientific computations for its efficiency with data sets.

    Virtualisation
        The creation of virtual instances of computing resources, such as CPUs, storage, or networks, to enable flexible resource management and usage.

    Workflow
        A series of computational steps or tasks in an HPC environment, often automated to streamline complex computations that involve multiple stages or applications.

    Workload Manager
        Software that manages the distribution, scheduling, and monitoring of tasks in an HPC environment, optimising resource usage and ensuring job execution meets performance goals.

    Zsh
        Z Shell; an extended shell with more advanced features than Bash, such as improved scripting, enhanced customisation options, and powerful command-line completion. Zsh is used in some HPC settings for its flexibility and user-friendly features.
