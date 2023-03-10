# Splunk TA for PowerShell
This app is still under development and thus, unstable. 
Do not use in production!
## Description
The goal of this app is to handle all your PowerShell related needs in Splunk.

## Features
* Inputs for Windows PowerShell Scriptblock and Module logging
* Field extractions for scriptblock and module logs
* Automatic lookup for decoding -EncodedCommands
* Inputs.conf local blacklisting of some common useless scriptblocks
* Tag and EventType for encoded commands (psencodedcommand) for easier filtering
* Automatically calculated SHA256 hash per unique scriptblock for easy whitelisting and IoC sharing.


## Planned
* Transcript logging
* PowerShell Core logging on Windows/*nix
* Automatically calculated threat scores for scriptblocks from keywords. 
* Enterprise Security analytic stories
* Reports & Dashboards

## How to use
Until this repo is stable, it won't be put on SplunkBase. 

Clone the repo 

``` git clone https://github.com/hampusstrom/TA-PowerShell.git ```

Customize the inputs.conf to your needs and push using your depoyer and/or deploymentserver depending on your needs.


