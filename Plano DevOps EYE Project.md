# **Enhanced Yardstick Engine** **EYE Project Fact Sheet** **Alfa Version**

**EYE Project** (Enhanced Yardstick Engine) is an industrial-grade state of the art Artificial Intelligence in Medicine (AIM) solution designed for high-fidelity clinical semantic extraction from legacy medical records. 

The **project architecture** is built upon a **deterministic, hermetic environment** (Docker and uv), ensuring **absolute portability and reproducibility**. **Orchestration** via Docker Compose **decouples** the application from LLM inference, while the **Model Context Protocol (MCP)** provides a standardized interoperability layer that securely bridges siloed local clinical data with LLM reasoning in real-time. By utilizing a **declarative manifest** as the **Single Source of Truth (SSOT)**, the system ensures that all clinical processing is **immutable**, **auditable**, and strictly compliant with **data sovereignty standards**.

**Author: Dr. Fausto Stangler CRMRS 24730 RQE 17742**

**Critical Analysis:** The EYE Project represents a sophisticated Cloud-Native Progressive architecture. The design successfully implements a Clean Host \+ Container as SSOT strategy, treating the host OS merely as a hardware-resource hypervisor. By decoupling clinical logic from LLM inference using the Model Context Protocol (MCP) and Docker Compose, the system achieves high portability and avoids the "dependency drift" common in AI environments.

# 

# 1\. Key Features {#1.-key-features}

**NLP/LLM/RAG:** Combines language models with context retrieval (RAG) to interpret text with clinical precision, avoiding generic responses and hallucinations.

**Dual-Role MCP Architecture:** Operates both as an MCP Host, aggregating data from fragmented clinical silos, and as an MCP Server, exposing high-precision clinical extraction tools to the broader medical ecosystem. 

**Rigid separation of responsibilities:** The application and LLM inference run in isolation. This prevents coupling, facilitates auditing, and allows model swapping without systemic impact.

**Deterministic environment:** The use of Docker and uv.lock ensures that dependencies, versions, and behavior are identical across any environment.

**Type-Safe Extraction:** Uses Instructor and Pydantic to enforce rigorous data schemas, ensuring that unstructured clinical text is transformed into validated, machine-readable JSON.

**Privacy-First Local Inference:** Orchestration via Ollama/NVIDIA-Docker enables high-performance inference within a private perimeter, ensuring data sovereignty and compliance.

**Absolute reproducibility:** The same input generates the same output under the same conditions, a critical requirement for healthcare, compliance, and scientific validation.

# 2\. Index {#2.-index}

[1\. Key Features	2](#1.-key-features)

[2\. Index	3](#2.-index)

[3\. Main Concepts	5](#3.-main-concepts)

[4\. Environment Readiness	5](#4.-environment-readiness)

[4.1. Machine Setup	5](#4.1.-machine-setup)

[4.1.1. Firmware Sanitization	5](#4.1.1.-firmware-sanitization)

[4.1.2. Strategic Partitioning	6](#4.1.2.-strategic-partitioning)

[4.2. OS Provisioning	6](#4.2.-os-provisioning)

[4.2.1. Linux	6](#4.2.1.-linux)

[4.3. File System Configuration	6](#4.3.-file-system-configuration)

[4.3.1. NTFS Disk D:	6](#4.3.1.-ntfs-disk-d:)

[4.3.2. NTFS Protection against corruption	6](#4.3.2.-ntfs-protection-against-corruption)

[4.3.3. Fixed Drives Mountpoints	7](#4.3.3.-fixed-drives-mountpoints)

[4.3.4. GRUB Optimization	8](#4.3.4.-grub-optimization)

[4.3.5. Swap File Tuning	9](#4.3.5.-swap-file-tuning)

[4.4. Extra Config	10](#4.4.-extra-config)

[4.4.1. Free up Space	10](#4.4.1.-free-up-space)

[4.4.2. Move cache	10](#4.4.2.-move-cache)

[4.5. Hipervisor Clean Host Setup	11](#4.5.-hipervisor-clean-host-setup)

[4.5.1. cURL	11](#4.5.1.-curl)

[4.5.2. NVIDIA Drivers	11](#4.5.2.-nvidia-drivers)

[4.5.3. NVIDIA Container Toolkit	11](#4.5.3.-nvidia-container-toolkit)

[4.5.4. Docker Engine	12](#4.5.4.-docker-engine)

[4.5.5. Docker Data Root	12](#4.5.5.-docker-data-root)

[5\. Software Runtime Architecture	13](#5.-software-runtime-architecture)

[5.1. Dependency Management (SSOT)	13](#5.1.-dependency-management-\(ssot\))

[5.1.1. pyproject.toml	13](#5.1.1.-pyproject.toml)

[5.1.2. uv.lock and Deterministic Resolution	18](#5.1.2.-uv.lock-and-deterministic-resolution)

[5.2. Configuration & Secrets	19](#5.2.-configuration-&-secrets)

[5.2.1. Secret Management & Environment Variables	19](#5.2.1.-secret-management-&-environment-variables)

[5.3. Codebase and Project Scaffolding	19](#5.3.-codebase-and-project-scaffolding)

[5.3.1. Repository Layout	19](#5.3.1.-repository-layout)

[5.3.2. Source vs Persistent Data Separation	20](#5.3.2.-source-vs-persistent-data-separation)

[5.4. Container Image Specification	20](#5.4.-container-image-specification)

[5.4.1. Dockerfile: Blueprint	20](#5.4.1.-dockerfile:-blueprint)

[5.4.2. Runtime Orchestration (SSOT)	22](#5.4.2.-runtime-orchestration-\(ssot\))

[5.4.3. Build-Time vs Runtime Concerns	22](#5.4.3.-build-time-vs-runtime-concerns)

[5.4.4. docker-compose.yml (Base / Prod-like)	23](#5.4.4.-docker-compose.yml-\(base-/-prod-like\))

[5.4.5. docker-compose.dev.yml (Development Override)	25](#5.4.5.-docker-compose.dev.yml-\(development-override\))

[5.4.6. IDE VSCode or Antigravity launch.json	28](#5.4.6.-ide-vscode-or-antigravity-launch.json)

[6\. Application Entry Point and Lifecycle	29](#6.-application-entry-point-and-lifecycle)

[6.1. Definition	29](#6.1.-definition)

[6.2. Application Entry Point Contract	29](#6.2.-application-entry-point-contract)

[6.2.1. Run containers	29](#6.2.1.-run-containers)

[6.2.2. Entry Point Responsibilities (main.py)	30](#6.2.2.-entry-point-responsibilities-\(main.py\))

[6.2.3. main.py	30](#6.2.3.-main.py)

[Logging	31](#logging)

[6.3. Startup sequence	31](#6.3.-startup-sequence)

[6.3.1. Start Server (Via Terminal)	31](#6.3.1.-start-server-\(via-terminal\))

[6.3.2. Connect Debugger (via IDE (antigravity, vs code) or F5 or debug with launch.json)	31](#6.3.2.-connect-debugger-\(via-ide-\(antigravity,-vs-code\)-or-f5-or-debug-with-launch.json\))

[6.3.3. Run code	32](#6.3.3.-run-code)

[6.4. Health semantics	32](#6.4.-health-semantics)

[6.5. Application Lifecycle Semantics	32](#6.5.-application-lifecycle-semantics)

[6.5.1. Lifecycle States	33](#6.5.1.-lifecycle-states)

[6.5.2. Startup Failure Policy	33](#6.5.2.-startup-failure-policy)

[6.5.3. Graceful Shutdown	33](#6.5.3.-graceful-shutdown)

[6.6. Shutdown e sinais inexistentes	34](#6.6.-shutdown-e-sinais-inexistentes)

[7\. Clinical Data Flow and Validation	35](#7.-clinical-data-flow-and-validation)

[8\. Operations and Runbook	35](#8.-operations-and-runbook)

[8.1. Debugging	35](#8.1.-debugging)

[8.1.1. ECONNREFUSED error	35](#8.1.1.-econnrefused-error)

# **Infra Structure**

# 3\. Main Concepts {#3.-main-concepts}

A Hardware-Software Bridge that maintains a Clean Host while enabling high-performance GPU acceleration. Host solely as a Kernel \+ Driver \+ Container Runtime provider to avoid dependency drift,  moving all logic, libraries, and even AI runtimes into isolated, version-controlled container layers.

# **Host Provisioning** **Machine-specific**

# 4\. Environment Readiness {#4.-environment-readiness}

## 4.1. Machine Setup {#4.1.-machine-setup}

This may vary. Actual machine is Legion Y540 notebook with a hybrid storage setup (128 Gb SSD \+ 1 Tb HDD) and an RTX 2060\. Optimization regarding the IO bottleneck of mechanical drive while leveraging the GPU. 

### **4.1.1. Firmware Sanitization** {#4.1.1.-firmware-sanitization}

UEFI for linux GRUB. 

### **4.1.2. Strategic Partitioning** {#4.1.2.-strategic-partitioning}

The SSD is dual boot with original windows in NTFS and Linux in ext4. The HDD disk has main legacy NTFS windows partition with code, accessed by Linux, and another ext4 partition for large models and images and containers. 

The system is in ssd ext partition ‘/’ mount point. The swap file is in the fast SSD. The shared-with-NTFS files are in /mnt/gamer\_d, and the EYE-only data are in /mnt/linux\_d. 

## 4.2. OS Provisioning {#4.2.-os-provisioning}

### **4.2.1. Linux** {#4.2.1.-linux}

Pendrive Ventoy or similar and Ubuntu 22.04 LTS ((Jammy Jellyfish) ubuntu-22.04.5-desktop-amd64.iso in a dual boot with minimal installation. 

Use the partitioning objectives as needed above

## 4.3. File System Configuration {#4.3.-file-system-configuration}

### **4.3.1. NTFS Disk D:** {#4.3.1.-ntfs-disk-d:}

Avoid suspend

## *sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target*

To revert:

## *sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target*

### **4.3.2. NTFS Protection against corruption** {#4.3.2.-ntfs-protection-against-corruption}

In windows, via PowerShell admin

## *powercfg /h off*

## *shutdown /s /t 0*

If there is a persistent error, run on windows as administrator. It may take some time depending on the disk size:

## *chkdsk D: /f*

## *chkdsk D: /f /r /x*

## *shutdown /s /t 0*

On Windows, always shut down completely. 

### **4.3.3. Fixed Drives Mountpoints** {#4.3.3.-fixed-drives-mountpoints}

Create the fixed mountpoint with a shortcut in the home directory.

## *sudo mkdir \-p /mnt/gamer\_d*

## *ln \-s /mnt/gamer\_d \~/gamer\_d*

## *sudo mkdir \-p /mnt/linux\_d*

## *ln \-s /mnt/linux\_d \~/linux\_d*

## *sudo mkdir \-p /mnt/windows\_c*

## *ln \-s /mnt/windows\_c \~/windows\_c*

Locate the drive's UUID (e.g., sda1 UUID=01DBC9A17CCF2730, sda2=91dd96f9-c77f-4cfd-9685-2ec19a0448ca).

UUID is a 128-bit Universally Unique Identifier for disks used in the /etc/fstab configuration file to ensure the correct partitions are mounted during system boot. Sda are standard Linux device names (sd refers to "SCSI disk," or for most types of other drives, ‘a’indicates the first recognized disk (e.g., sdb would be the second, and 1 and 2 indicate the partition number on that disk. So, sda1 is the first partition on the first disk, and sda2 is the second partition.

## *lsblk \-f*

Identify user id (uid=1000, gid=1000) and/or ollama id (in this case, uid=997, gid=984). 

## *id*

Edit fstab file

## *sudo nano /etc/fstab*

Add the lines for each mounted partition as a disk/folder

## *~~UUID=01DBC9A17CCF2730 /mnt/gamer\_d ntfs defaults,uid=1000,gid=1000,umask=000,windows\_names 0 0~~*

## *UUID=01DBC9A17CCF2730 /mnt/gamer\_d ntfs defaults,uid=1000,gid=1000,umask=022,windows\_names,nofail 0 0*

## *UUID=132a50dd-9852-486b-a531-68081a0118c4 /mnt/linux\_d ext4 defaults 0 0*

## *UUID=E6FC0948FC091509 /mnt/windows\_c ntfs defaults,uid=1000,gid=1000,umask=022,windows\_names,nofail 0 0*

Outside fstab: change user and update systemctl

## *sudo chown \-R stangler:stangler /mnt/linux\_d*

## *sudo systemctl daemon-reload*

Find mountpoint (checking)

## *mount | grep sda*

Unmount and mount via fstab

## *sudo umount /media/stangler/gamer\_D 2\>/dev/null*

## *sudo umount /media/stangler/linux\_D 2\>/dev/null*

## *sudo umount /media/stangler/windows\_C 2\>/dev/null*

## *sudo mount \-a*

## *sudo chown \-R stangler:stangler /mnt/linux\_d*

### **4.3.4. GRUB Optimization** {#4.3.4.-grub-optimization}

Keep entries in /etc/grub.d/

## *00\_header*

## *10\_linux*

## *30\_os-prober*

## *30\_uefi-firmware*

## *40\_custom*

## *41\_custom*

Remove access to entries in /etc/grub.d/

## *sudo chmod \-x /etc/grub.d/05\_debian\_theme*

## *sudo chmod \-x /etc/grub.d/10\_linux\_zfs*

## *sudo chmod \-x /etc/grub.d/20\_linux\_xen*

## *sudo chmod \-x /etc/grub.d/20\_memtest86+*

## *sudo chmod \-x /etc/grub.d/25\_bli*

## *sudo chmod \-x /etc/grub.d/35\_fwupd*

## *sudo update-grub*

Choose Boot Default in grub

## *sudo nano /etc/default/grub*

Set item (2 \= third element in list)

## *GRUB\_DEFAULT=2*

## *GRUB\_TIMEOUT\_STYLE=menu*

## *GRUB\_TIMEOUT=3*

Update Grub

## *sudo update-grub*

### **4.3.5. Swap File Tuning** {#4.3.5.-swap-file-tuning}

Swap File Size (to 12 GB \= 12288\)

## *sudo swapoff /swap.img*

## *sudo dd if=/dev/zero of=/swap.img bs=1M count=12288* 

## *sudo mkswap /swap.img* 

## *sudo swapon /swap.img* 

Assure persistence

## *sudo nano /etc/fstab*

Check if exists

## */swap.img none swap sw 0 0*

Control system usage (swappiness 0 minimum to 100 maximum)

## *echo "vm.swappiness=10" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Filesystem Cache (\<100, 100, \>100, lower \= older)

## *echo "vm.vfs\_cache\_pressure=50" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Aggressive OOM-killer reduction

## *echo "vm.oom\_kill\_allocating\_task=0" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Network performance Increase buffer

## *echo "net.core.rmem\_max=26214400" | sudo tee \-a /etc/sysctl.conf*

## *echo "net.core.wmem\_max=26214400" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Increase connections backlog

## *echo "net.core.somaxconn=4096" | sudo tee \-a /etc/sysctl.conf*

## *echo "net.ipv4.tcp\_max\_syn\_backlog=8192" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Avoid excessive TIME\_WAIT

## *echo "net.ipv4.tcp\_tw\_reuse=1" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

More SSD efficient I/O

## *echo "vm.dirty\_ratio=10" | sudo tee \-a /etc/sysctl.conf*

## *echo "vm.dirty\_background\_ratio=5" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

Large apps file Caching

## *echo "vm.vfs\_cache\_pressure=30" | sudo tee \-a /etc/sysctl.conf*

## *sudo sysctl \-p*

## 4.4. Extra Config {#4.4.-extra-config}

### **4.4.1. Free up Space** {#4.4.1.-free-up-space}

Clean apt

## *sudo apt clean*

## *sudo apt autoremove \--purge \-y*

Clean uv cache

## *rm \-rf \~/.cache/uv*

Clean pip cache

## *rm \-rf \~/.cache/pip*

Clean build Python cache

## *find \~ \-type d \-name "\_\_pycache\_\_" \-prune \-exec rm \-rf {} \+*

Deep Clean Docker

## *docker system prune \-af*

## *docker builder prune \-af*

### **4.4.2. Move cache** {#4.4.2.-move-cache}

Move cache to another disk

## *mkdir \-p /mnt/gamer\_d/uv-cache*

## *rm \-rf \~/.cache/uv*

## *ln \-s /mnt/gamer\_d/uv-cache \~/.cache/uv*

Use UV\_CACHE\_DIR

## *export UV\_CACHE\_DIR=/mnt/gamer\_d/uv-cache*

## 4.5. Hipervisor Clean Host Setup {#4.5.-hipervisor-clean-host-setup}

The Host OS acts strictly as a Hypervisor (the manager). It should not be cluttered with development tools, libraries, or specific AI frameworks. Its only job is to provide the hardware resources (CPU, RAM, GPU) to the containers.

### **4.5.1. cURL** {#4.5.1.-curl}

Basic tools to fetch resources. 

## *sudo apt update*

## *sudo apt install \-y curl wget*

### **4.5.2. NVIDIA Drivers** {#4.5.2.-nvidia-drivers}

The host needs the kernel drivers to communicate with the RTX 2060\. We use the production-ready branch.

## *sudo apt install \-y nvidia-driver-550-server nvidia-utils-550-server*

## *ubuntu-drivers list*

## *ubuntu-drivers devices*

## *sudo ubuntu-drivers autoinstall*

## *sudo reboot*

Verification

## *nvidia-smi*

### **4.5.3. NVIDIA Container Toolkit** {#4.5.3.-nvidia-container-toolkit}

The "Bridge" that allows Docker to "see" and use the GPU

Install Repository Keys and Sources

## *sudo apt update*

## *sudo mkdir \-p /etc/apt/keyrings*

## *curl \-fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg \--dearmor \-o /etc/apt/keyrings/nvidia-container-toolkit.gpg \\*

##   *&& curl \-s \-L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \\*

##     *sed 's\#deb https://\#deb \[signed-by=/etc/apt/keyrings/nvidia-container-toolkit.gpg\] https://\#g' | \\*

##     *sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list*

Install the Toolkit

## *sudo apt update && sudo apt install \-y nvidia-container-toolkit*

## *sudo systemctl restart docker*

### **4.5.4. Docker Engine** {#4.5.4.-docker-engine}

The container runtime that will orchestrate our isolated environments.

Remove older versions if exits

## *sudo apt-get remove \-y docker docker.io containerd runc*

Install Docker and Compose and add user

## *sudo apt install \-y docker.io docker-compose-v2*

## *sudo systemctl enable \--now docker*

## *sudo usermod \-aG docker $USER*

## *newgrp docker*

### **4.5.5. Docker Data Root** {#4.5.5.-docker-data-root}

We redirect Docker's storage to the HDD to save SSD space and register the NVIDIA runtime.

## *sudo systemctl stop docker*

## *sudo tee /etc/docker/daemon.json \> /dev/null \<\<EOF*

## *{*

##   *"data-root": "/mnt/linux\_d/docker",*

##   *"runtimes": {*

##     *"nvidia": {*

##       *"path": "nvidia-container-runtime",*

##       *"args": \[\]*

##     *}*

##   *}*

## *}*

## *EOF*

## 

## *sudo systemctl start docker*

# **EYE Runtime Architecture** **Project-specific**

# 5\. Software Runtime Architecture {#5.-software-runtime-architecture}

## 5.1. Dependency Management (SSOT) {#5.1.-dependency-management-(ssot)}

### **5.1.1. pyproject.toml** {#5.1.1.-pyproject.toml}

The pyproject.toml replaces the fragmented legacy mess of project files with a single, declarative, and human-readable archive as is the Single Source of Truth (SSOT) for the Python ecosystem, ensuring that the code running on your host machine behaves identically when deployed inside a container.

Orchestration of the Runtime (SSOT) to create a hermetic ambient. Separation of light dependencies from heavy environment-specific ones (as torch, models and others) to keep the clean host. Standardizes metadata defines the project name, version, author and compatibility and import project as a module. Tool centralization of all config files in one tool section of pyproject.toml. 

## *\[project\]*

## *name \= "eye"*

## *version \= "0.1.0"*

## *description \= "Enhanced Yardstick Engine (EYE): extração clínica semântica determinística com MCP \+ RAG."*

## *readme \= "README.md"*

## *requires-python \= "\>=3.11,\<3.13"*

## *authors \= \[{ name \= "Fausto Stangler" }\]*

## *license \= { text \= "Proprietary" }*

## 

## *\# Runtime (container)*

## *dependencies \= \[*

##   *\# API / serving*

##   *"fastapi\>=0.110",*

##   *"uvicorn\[standard\]\>=0.27",*

## 

##   *\# Config/HTTP*

##   *"python-dotenv\>=1.0",*

##   *"requests\>=2.31",*

##   *"httpx\>=0.27",*

## 

##   *\# Parsing / ingest*

##   *"beautifulsoup4\>=4.12",*

##   *"lxml\>=5.0",*

## 

##   *\# Schemas / extraction*

##   *"pydantic\>=2.6",*

##   *"instructor\>=1.6",*

## 

##   *\# RAG / orchestration*

##   *"langchain\>=0.2",*

##   *"langchain-community\>=0.2",*

##   *"langchain-text-splitters\>=0.2",*

##   *"langchain-chroma\>=0.1",*

##   *"langchain-openai\>=0.1",*

##   *"langchain-ollama\>=0.1",*

## 

##   *\# MCP (Dual-Role Host/Server)*

##   *"mcp\>=1.7",*

##   *"langchain-mcp-adapters\>=0.2.1",*

## *\]*

## 

## *\[project.optional-dependencies\]*

## *\# Uso local / notebooks (para uma imagem dev)*

## *notebook \= \[*

##   *"jupyterlab\>=4.0",*

##   *"ipykernel\>=6.29",*

##   *"matplotlib\>=3.8",*

##   *"pandas\>=2.2",*

##   *"numpy\>=1.26",*

## *\]*

## 

## *\# NLP tradicional (se realmente for usar spaCy no pipeline)*

## *nlp \= \[*

##   *"spacy\>=3.8",*

##   *"en-core-web-sm",*

## *\]*

## 

## *\# Inferência local fora do Ollama (somente se você decidir manter backend alternativo)*

## *local-cpp \= \[*

##   *"llama-cpp-python\>=0.3",*

##   *"gguf",*

##   *"tiktoken\>=0.6",*

## *\]*

## 

## *\# GPU (somente para dev/local; em prod você já está isolando inferência via Ollama container)*

## *gpu \= \[*

##   *"torch",*

## *\]*

## 

## *\# Qualidade/CI*

## *dev \= \[*

##   *"pytest\>=8.0",*

##   *"pytest-cov\>=5.0",*

##   *"ruff\>=0.6",*

##   *"mypy\>=1.10",*

##   *"debugpy\>=1.8",*

## *\]*

## 

## *\[build-system\]*

## *requires \= \["hatchling"\]*

## *build-backend \= "hatchling.build"*

## 

## *\[tool.hatch.build.targets.wheel\]*

## *packages \= \["eye\_engine"\]*

## 

## *\# uv: fonte declarativa para modelos spaCy (SSOT do artifact)*

## *\[tool.uv.sources\]*

## *en-core-web-sm \= { url \= "https://github.com/explosion/spacy-models/releases/download/en\_core\_web\_sm-3.8.0/en\_core\_web\_sm-3.8.0-py3-none-any.whl" }*

## 

## *\# (opcional) lint/typecheck defaults*

## *\[tool.ruff\]*

## *line-length \= 100*

## *target-version \= "py311"*

## 

## *\[tool.mypy\]*

## *python\_version \= "3.11"*

## *warn\_return\_any \= true*

## *warn\_unused\_ignores \= true*

## *no\_implicit\_optional \= true*

## *disallow\_untyped\_defs \= false*

### **5.1.2. uv.lock and Deterministic Resolution** {#5.1.2.-uv.lock-and-deterministic-resolution}

uv lock is the process by which the abstract dependency specification defined in pyproject.toml is resolved into a fully concrete, immutable dependency graph, stored in the uv.lock file.

## *cd "/mnt/gamer\_d/Fausto Stangler/Documentos/Python/EYE"*

## *docker run \--rm \\*

##   *\-v "$PWD:/app" \\*

##   *\-w /app \\*

##   *python:3.11-slim \\*

##   *bash \-lc '*

##     *set \-euo pipefail*

##     *apt-get update && apt-get install \-y \--no-install-recommends curl ca-certificates && rm \-rf /var/lib/apt/lists/\**

##     *curl \-LsSf https://astral.sh/uv/install.sh | sh*

##     *export PATH="$HOME/.local/bin:$PATH"*

##     *uv \--version*

##     *uv lock*

##   *'*

To a deep clean in docker now:

## *docker stop $(docker ps \-q) 2\>/dev/null*

## *docker rm \-f $(docker ps \-aq) 2\>/dev/null*

## *docker rmi \-f $(docker images \-aq) 2\>/dev/null*

## *docker volume rm $(docker volume ls \-q) 2\>/dev/null*

## *docker network rm $(docker network ls \-q | grep \-v "bridge\\|host\\|none") 2\>/dev/null*

## *docker builder prune \-a \-f*

## *docker system prune \-a \--volumes \-f*

## 5.2. Configuration & Secrets {#5.2.-configuration-&-secrets}

### **5.2.1. Secret Management & Environment Variables** {#5.2.1.-secret-management-&-environment-variables}

Layered configuration strategy to separate generic settings from sensitive credentials. Global architecture settings and local, sensitive machine-specific overrides

.verv

## *LLM\_PORT=11434*

## *LLM\_BASE\_URL="http://inference:11434/v1"*

## *LLM\_MODEL\_NAME="llama3.1:8b"*

## *CHROMA\_PERSIST\_DIR="/app/db/chroma\_db"*

.env.local

## *OPENAI\_API\_KEY="opan\_ai\_key"*

## *UNSTRUCTURED\_API\_KEY="chave\_api\_forte\_exemplo\_1234567890"*

## 5.3. Codebase and Project Scaffolding {#5.3.-codebase-and-project-scaffolding}

### **5.3.1. Repository Layout** {#5.3.1.-repository-layout}

The project implements a strict separation between source code (volatile) and model/container data (persistent/heavy). 

Source Code (Shared Host/Container): Located on the NTFS partition for cross-OS accessibility. 

## *cd "/mnt/gamer\_d/Fausto Stangler/Documentos/Python/EYE"*

Heavy Data & Runtimes (Linux Native): LLM weights, Docker layers, and Virtual Environments are hosted on the ext4 partition to ensure I/O performance, in their specific folders

## *cd "/mnt/linux\_d/docker"*

### **5.3.2. Source vs Persistent Data Separation** {#5.3.2.-source-vs-persistent-data-separation}

## 5.4. Container Image Specification {#5.4.-container-image-specification}

### **5.4.1. Dockerfile: Blueprint** {#5.4.1.-dockerfile:-blueprint}

The application environment is defined by a multi-stage-ready Python 3.11-slim image. It utilizes uv as the primary package manager to ensure deterministic builds via uv.lock.

## *\# syntax=docker/dockerfile:1.6*

## *FROM python:3.11-slim AS base*

## 

## *ENV PYTHONDONTWRITEBYTECODE=1 \\*

##     *PYTHONUNBUFFERED=1 \\*

##     *PIP\_NO\_CACHE\_DIR=1 \\*

##     *PIP\_DISABLE\_PIP\_VERSION\_CHECK=1 \\*

##     *UV\_PROJECT\_ENVIRONMENT=/venv \\*

##     *PYTHONPATH=/app*

## 

## *WORKDIR /app*

## 

## *\# APT robusto (menos falhas intermitentes)*

## *RUN set \-eux; \\*

##     *printf 'Acquire::Retries "5";\\nAcquire::http::Timeout "30";\\nAcquire::https::Timeout "30";\\n' \\*

##     *\> /etc/apt/apt.conf.d/80-retries*

## 

## *\# Dependências mínimas de build p/ libs C (bs4/lxml etc.)*

## *RUN set \-eux; \\*

##     *apt-get update; \\*

##     *apt-get install \-y \--no-install-recommends \\*

##     *ca-certificates curl git build-essential \\*

##     *libxml2-dev libxslt-dev \\*

##     *; \\*

##     *rm \-rf /var/lib/apt/lists/\**

## 

## *\# Usuário não-root*

## *RUN useradd \-m appuser && mkdir \-p /app /venv && chown \-R appuser:appuser /app /venv*

## *USER appuser*

## 

## *\# Preferível: pegar uv do container oficial (sem curl|sh)*

## *COPY \--from=ghcr.io/astral-sh/uv:latest /uv /home/appuser/.local/bin/uv*

## *ENV PATH="/venv/bin:/home/appuser/.local/bin:${PATH}"*

## 

## *\# Maximiza cache: só manifests primeiro*

## *COPY \--chown=appuser:appuser pyproject.toml uv.lock README.md ./*

## 

## 

## *\# \-------------------------*

## *\# DEV IMAGE (com extras)*

## *\# \-------------------------*

## *FROM base AS dev*

## *ARG INSTALL\_DEV=0*

## *RUN if \[ "$INSTALL\_DEV" \= "1" \]; then \\*

##     *uv sync \--frozen \--extra dev; \\*

##     *else \\*

##     *uv sync \--frozen \--no-dev; \\*

##     *fi*

## *COPY \--chown=appuser:appuser . .*

## *CMD \["bash"\]*

## 

## *\# \-------------------------*

## *\# RUNTIME IMAGE (lean)*

## *\# \-------------------------*

## *FROM base AS runtime*

## *RUN set \-eux; \\*

##     *uv sync \--frozen \--no-dev*

## *COPY \--chown=appuser:appuser . .*

## *EXPOSE 8000*

## *CMD \["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"\]*

## 

### **5.4.2. Runtime Orchestration (SSOT)** {#5.4.2.-runtime-orchestration-(ssot)}

### **5.4.3. Build-Time vs Runtime Concerns** {#5.4.3.-build-time-vs-runtime-concerns}

The system is decoupled into different services: the EYE Engine (Application logic) using the Dockerfile above, the Inference Server (Ollama), the Document Ingestion Server  (unstructured). 

### **5.4.4. docker-compose.yml (Base / Prod-like)** {#5.4.4.-docker-compose.yml-(base-/-prod-like)}

This is achieved using the base docker-compose.yaml for production use, and using the docker-compose.dev.yaml for development scenarios. 

## *services:*

##   *eye-api:*

##     *build:*

##       *context: .*

##       *args:*

##         *INSTALL\_DEV: "0"*

##     *\# Em prod-like, nada de bind-mount do código (imagem é o artefato)*

##     *env\_file:*

##       *\- .env*

##       *\- .env.local*

##     *environment:*

##       *\# A app fala com o serviço de inferência por rede interna*

##       *LLM\_BASE\_URL: ${LLM\_BASE\_URL:-http://inference:11434/v1}*

##       *LLM\_MODEL\_NAME: ${LLM\_MODEL\_NAME:-llama3.1:8b}*

##       *CHROMA\_PERSIST\_DIR: ${CHROMA\_PERSIST\_DIR:-/app/db/chroma}*

##     *depends\_on:*

##       *inference:*

##         *condition: service\_healthy*

##     *networks:*

##       *\- internal*

##     *\# Opcional (recomendado): persistir DB local do RAG (Chroma)*

##     *volumes:*

##       *\- chroma\_db:${CHROMA\_PERSIST\_DIR:-/app/db/chroma}*

##       *\- logs:/app/logs*

##     *\# Prod-like: por padrão não expõe porta no host (mais seguro).*

##     *\# Se quiser expor a API em prod, descomente:*

##     *\# ports:*

##     *\#   \- "8000:8000"*

## 

##   *inference:*

##     *image: ollama/ollama:latest*

##     *\# Recomendo mapear para o seu disco ext4 (como no seu manual):*

##     *\# \- /mnt/linux\_d/ollama:/root/.ollama*

##     *\# Se você preferir volume nomeado, troque pela linha abaixo:*

##     *\# \- ollama\_models:/root/.ollama*

##     *volumes:*

##       *\- /mnt/linux\_d/ollama:/root/.ollama*

##     *networks:*

##       *\- internal*

##     *healthcheck:*

##       *test: \[ "CMD-SHELL", "ollama list || exit 1" \]*

##       *interval: 10s*

##       *timeout: 3s*

##       *retries: 30*

##       *start\_period: 20s*

##     *deploy:*

##       *resources:*

##         *reservations:*

##           *devices:*

##             *\- driver: nvidia*

##               *count: 1*

##               *capabilities: \[ gpu \]*

## 

##   *\# Opcional: só ligue se realmente usar o Unstructured no pipeline.*

##   *\# Mantive como "profile" para não subir por padrão.*

##   *unstructured:*

##     *image: downloads.unstructured.io/unstructured-io/unstructured-api:latest*

## 

##     *environment:*

##       *\- UNSTRUCTURED\_API\_KEY=${UNSTRUCTURED\_API\_KEY:-}*

##     *networks:*

##       *\- internal*

##     *healthcheck:*

##       *test: \[ "CMD-SHELL", "curl \-fsS http://localhost:8000/healthcheck \> /dev/null || exit 1" \]*

##       *interval: 30s*

##       *timeout: 10s*

##       *retries: 5*

## 

## *volumes:*

##   *chroma\_db:*

##   *logs:*

##     *\# Se preferir volume nomeado para ollama ao invés de bind no /mnt/linux\_d:*

##     *\# ollama\_models:*

## 

## *networks:*

##   *internal:*

##     *driver: bridge*

##     *internal: false*

### **5.4.5. docker-compose.dev.yml (Development Override)** {#5.4.5.-docker-compose.dev.yml-(development-override)}

Special setup for dev

## *services:*

##   *eye-api:*

##     *build:*

##       *context: .*

##       *args:*

##         *INSTALL\_DEV: "1"*

##       *target: dev*

##     *image: eye-api:dev*

##     *\# Dev: bind-mount do código para live-edit*

##     *volumes:*

##       *\- .:/app*

##       *\# Cache do venv para acelerar rebuilds e evitar reinstalar tudo*

##       *\- venv:/venv*

##       *\# Persistência do Chroma também em dev (se quiser)*

##       *\- chroma\_db:${CHROMA\_PERSIST\_DIR:-/app/db/chroma}*

##       *\- ./logs:/app/logs \# \<= NOVO: persistência de logs no host*

##     *\# Dev: expõe API no host*

##     *ports:*

##       *\- "8000:8000"*

##       *\- "5678:5678"*

##     *environment:*

##       *\- PYDEVD\_DISABLE\_FILE\_VALIDATION=1*

##       *\- DEV\_MODE=1*

##       *\- LOG\_LEVEL=DEBUG*

##       *\- LOG\_FORMAT=pretty*

## 

##     *\# Dev: se você quiser manter um container “parado” para entrar e rodar comandos:*

##     *\# command: \["sleep", "infinity"\]*

##     *\# Ou rodar a API diretamente (recomendado se você já tem main:app):*

##     *command: \[ "/venv/bin/python", "-u", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" \]*

## 

## *volumes:*

##   *venv:*

##   *chroma\_db:*

### **5.4.6. IDE VSCode or Antigravity launch.json** {#5.4.6.-ide-vscode-or-antigravity-launch.json}

## *{*

##     *"version": "0.2.0",*

##     *"configurations": \[*

##         *{*

##             *"name": "Attach EYE (Docker)",*

##             *"type": "debugpy",*

##             *"request": "attach",*

##             *"connect": {*

##                 *"host": "localhost",*

##                 *"port": 5678*

##             *},*

##             *"pathMappings": \[*

##                 *{*

##                     *"localRoot": "${workspaceFolder}",*

##                     *"remoteRoot": "/app"*

##                 *}*

##             *\],*

##             *"justMyCode": true,*

##             *"subProcess": true*

##         *}*

##     *\]*

## *}*

# **Application** **Runtime & Operations**

# 6\. Application Entry Point and Lifecycle {#6.-application-entry-point-and-lifecycle}

## 6.1. Definition {#6.1.-definition}

Responsabilidade do entrypoint. O que pode / não pode acontecer no import. O que bloqueia o boot. O que acontece se algo falhar. 

## 6.2. Application Entry Point Contract {#6.2.-application-entry-point-contract}

main.py é o único entrypoint. imports devem ser side-effect free. inicializações pesadas (RAG, MCP, DB) devem ser lazy ou controladas. falhas críticas impedem startup. falhas não críticas degradam funcionalidades. 

### **6.2.1. Run containers** {#6.2.1.-run-containers}

## *cd "/mnt/gamer\_d/Fausto Stangler/Documentos/Python/EYE"*

## *docker compose \-f docker-compose.yml \-f docker-compose.dev.yml up \-d \--build*

Outras operações

**Ver status**

## *docker compose ps*

**Parar sem apagar nada**

## *docker compose stop*

**Voltar depois de parar sem apagar nada**

## *docker compose start*

**Desligar containers**

## *docker compose down*

**Reiniciar só o app**

## *docker compose restart eye-engine*

**Parar só o eye-engine**

## *docker compose stop eye-engine*

**Limpeza profunda**

## *docker compose down \--volumes \--remove-orphans \--rmi all*

### **6.2.2. Entry Point Responsibilities (main.py)** {#6.2.2.-entry-point-responsibilities-(main.py)}

The entry point is responsible for:

Initializing logging

Loading typed configuration

Creating the FastAPI application

Registering routes and middleware

Exposing health and readiness endpoints

Heavy operations (model loading, embeddings, ingestion) must not execute at import time.

### **6.2.3. main.py** {#6.2.3.-main.py}

Basic “hello world” API endpoint with logging. When debugging with json the inside methods breakpoints will stop the debugging. 

## *import logging*

## *from fastapi import FastAPI*

## 

## *logging.basicConfig(*

##     *level=logging.INFO,*

##     *format="%(asctime)s %(levelname)s %(name)s %(message)s",*

## *)*

## 

## *logger \= logging.getLogger("eye")*

## 

## *app \= FastAPI()*

## 

## *@app.get("/health")*

## *def health():*

##     *logger.info("Health check OK")*

##     *return {"status": "done"}*

### **URL Entry Point** 

## *http://localhost:8000/health*

### **Logging** {#logging}

Falta definir: Formato canônico (JSON vs pretty. Campos obrigatórios. O que é log vs metric vs event. O que nunca pode ir para log (PII clínica)

## 6.3. Startup sequence {#6.3.-startup-sequence}

### **6.3.1. Start Server (Via Terminal)** {#6.3.1.-start-server-(via-terminal)}

Assure the container is up and running. 

## *docker compose \-f docker-compose.yml \-f docker-compose.dev.yml up \-d \--build*

At this stage, the API url is already running at localhost:8000, but breakpoints are not working yet. 

### **6.3.2. Connect Debugger (via IDE (antigravity, vs code) or F5 or debug with launch.json)** {#6.3.2.-connect-debugger-(via-ide-(antigravity,-vs-code)-or-f5-or-debug-with-launch.json)}

Click in debug with launch.json or F5 to run “Attach EYE” or similar. This will create a connection between the IDE and docker container. Now the IDE can interrupt the code execution in docker at the breakpoints in the editor. 

### **6.3.3. Run code** {#6.3.3.-run-code}

The docker is listening (waiting) the call. When you call the endpoint via API in the browser (or any other way), python in the container will run the function, the IDe will interrupt the code  execution at the breakpoint. If no one calls the function, code will not execute, breakpoint will not be used. 

Open the browser in the URL:

## *http://localhost:8000/health*

## 6.4. Health semantics {#6.4.-health-semantics}

Qual endpoint é usado para: healthcheck do Docker; readiness do load balancer O que significa “READY” de verdade. Se o RAG falha depois do boot, o container morre ou degrada?

Precisa definir semântica de saúde, por exemplo:

## *status: ok | degraded | error*

## *versão da aplicação*

## *readiness vs liveness*

Exemplo de contrato esperado

## *{*

##   *"status": "ok",*

##   *"service": "eye-engine",*

##   *"version": "0.1.0",*

##   *"llm": "reachable",*

##   *"rag": "initialized",*

##   *"timestamp": "2025-01-01T12:00:00Z"*

## *}*

Implementar /health e /ready. 

## 6.5. Application Lifecycle Semantics {#6.5.-application-lifecycle-semantics}

The EYE application follows a deterministic and explicit lifecycle model to ensure reproducibility, auditability, and predictable failure modes.

## *START*

##   *↓*

## *Load Configuration*

##   *↓*

## *Initialize Application*

##   *↓*

## *Register MCP (optional)*

##   *↓*

## *Initialize RAG (lazy)*

##   *↓*

## *Expose API*

##   *↓*

## *READY*

### **6.5.1. Lifecycle States** {#6.5.1.-lifecycle-states}

The application operates under the following conceptual states:

## *BOOTSTRAP: Container process starts, configuration is loaded.*

## *INITIALIZING: Core services are registered (API, logging, MCP stubs).*

## *READY: Application is ready to accept requests.*

## *DEGRADED: Non-critical subsystems (e.g. RAG, external tools) are unavailable, but the API remains responsive.*

## *FAILED: Critical initialization error prevents startup.*

## *SHUTDOWN: Application received SIGTERM/SIGINT and is terminating gracefully.*

### **6.5.2. Startup Failure Policy** {#6.5.2.-startup-failure-policy}

Configuration errors are fatal and abort startup.

Missing optional services result in degraded mode.

All failures are logged with structured logs.

### **6.5.3. Graceful Shutdown** {#6.5.3.-graceful-shutdown}

The application must handle termination signals (SIGTERM, SIGINT) by: Stopping request intake, Flushing logs, Releasing resources, Exiting cleanly. 

The EYE application must behave correctly as a containerized process.

The process executed as PID 1 must handle UNIX termination signals explicitly.

| Signal | Meaning | Expected Behavior |
| ----- | ----- | ----- |
| SIGTERM | Indication for a controlled shutdown (Typically issued by Docker or an orchestrator) | Commence the designated shutdown sequence |
| SIGINT | Interruption initiated by a user (e.g., Ctrl+C) | Identical to the behavior for SIGTERM |
| SIGKILL | Mandated, immediate termination | No operational guarantees are provided |

Upon receiving SIGTERM or SIGINT, the application must: Stop accepting new requests, Allow in-flight requests to complete (best-effort), Flush logs, Close external connections (DB, MCP, HTTP clients), Exit with code 0 within a bounded timeout. 

Failure to exit within the grace period allows the orchestrator to issue SIGKILL.

## 6.6. Shutdown e sinais inexistentes {#6.6.-shutdown-e-sinais-inexistentes}

Quem recebe SIGTERM? Em quanto tempo o processo deve sair? O que acontece se não sair? O que é graceful shutdown no EYE?

Não há nenhuma menção a:

## *SIGTERM*

## 

## *SIGINT*

## 

## *encerramento gracioso*

## 

## *flush de logs*

## 

## *persistência de estado*

## 

Isso é obrigatório em containers.

# 7\. Clinical Data Flow and Validation {#7.-clinical-data-flow-and-validation}

Ingest → RAG → LLM → Instructor → JSON

Schemas

Failure modes

# 8\. Operations and Runbook {#8.-operations-and-runbook}

Start / Stop

Model provisioning

Logs

Cleanup

Safe reset

## 8.1. Debugging {#8.1.-debugging}

### **8.1.1. ECONNREFUSED error** {#8.1.1.-econnrefused-error}

The ECONNREFUSED error means no listener in the TCP connection at port 5678\. It could be the debugpy not running in the container, the 5678 port not  correctly exposed, the container not running or the processed finished before debugger call. 

To check these, start by checking chain of configuration, first at launch.json (type, attach, host and ports); then check docker-compose.dev.yaml (mapping 5678:5678); then startup command in compose (debugpy \--listen 0.0.0.0:5678 \--wait-for-client). 

Then check runtime environment. Run docker ps e docker ps-a to check for running containers. If no container running, no process, no listening, no socket, no connection. 

Also check dependencies. Check for debugpy in pyproject.toml and the uv sync in the build, because venv may be maskering fresh dependencies. 

