
# Facerec - Linux Face Unlock
Facerec is a face authentication system for Ubuntu Linux that works while logging in, running "sudo" commands, etc. with a user-friendly CLI to operate it.


## Installation

#### 1. Update Sources
```
sudo apt update
```
#### 2. add PPA to your machine
```
sudo add-apt-repository ppa:rushabh-v/facerec
```

#### 3. Install Facerec
```
sudo apt install facerec
```

#### 4. Source bashrc
```
source ~/.bashrc
```


## Command Line Interface

| Command | Description |
|---------|-------------|
| facerec new | Add a new root face |
| facerec enable | Enable facerec |
| facerec disable | Temporarily disable facerec |
| facerec remove | Completely remove the facerec |
| facerec --version | Display installed version of facerec |
| facerec --help | Get the CLI info |

Try using the tab compeletions. It is one of the trivial features I am extra proud of :joy:


## Contributions Welcome
* Bug reports, Feature requests and PRs will be highly appreciated.
* Dockerfile for the testing environment can be found here. (Will soon upload the image to docker hub)
* Currently, facerec is only supported on Ubuntu. Adding support for other distros is on the list of major future plans.

## Troubleshoot

* If you don't have root access. Go to recovery mode as root and run,

```
facerec remove
```
