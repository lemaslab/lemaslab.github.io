|title                               |description                                        |categories|
|------------------------------------|---------------------------------------------------|----------|
|RUMP Personal Computer Documentation|Steps outlining running RUMP on a personal computer|blog      |

Asciinema Tutorial for Running RUMP: https://asciinema.org/a/CqZ9KjtP42oqMoeAXYKAmMjv3

It may take around 8 hours to run. You can copy this command for step 14.

1. [Install Ubuntu desktop.](https://ubuntu.com/download/desktop)

2. [Install VirtualBox.](https://www.virtualbox.org/)

3. [Install Ubuntu inside the VirtualBox.](https://linuxhint.com/install_ubuntu_18-04_virtualbox/)
When selecting memory size, choose 7000 MB. When selecting file size, choose at least 40 GB.
Move into settings, select System, and then Processor. Allocate 4 CPUs. If your computer is running extremely slowly in the VirtualBox, change to 2 CPUs.
When you close the VirtualBox, always select "Power off the machine".

4. Start Ubuntu. Open terminal with ctrl + alt + T.

5. Clone RUMP repository.
```
$ git clone https://github.com/lemaslab/RUMP.git
```

6. Move into RUMP repository.
```
$ cd RUMP
```

7. Install curl command.
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install curl
```

8. Install git command.
```
$ sudo apt install git-all
```

9. [Install Docker.](https://docs.docker.com/engine/install/ubuntu/)

10. Install Java.
```
$ sudo apt-get update
$ sudo apt-get install default-jre
```

11. [Install Nextflow.](https://www.nextflow.io/)

12. Download MZmine-2.53 into the repository.
```
wget https://github.com/mzmine/mzmine2/releases/download/v2.53/MZmine-2.53-Linux.zip && unzip MZmine-2.53-Linux.zip && rm MZmine-2.53-Linux.zip
```

13. Access "nextflow.config". Hover over "7GB", type "r", and "4". This will change "7GB" to "4GB" for memory storage. Repeat for the other "7GB". Hit esc upon completion. Type ":wq" to save changes and exit the file.
```
vi nextflow.config
```

14. Test RUMP with sample data provided.
```
./nextflow main.nf --input_dir_pos functional_test/sample_data/POS/ --input_dir_neg functional_test/sample_data/NEG --POS_design_path functional_test/sample_data/pos_design.csv --NEG_design_path functional_test/sample_data/neg_design.csv -with-docker xinsongdu/lemaslab_rump:v0.0.0
```
