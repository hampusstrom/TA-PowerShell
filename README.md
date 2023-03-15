# Splunk TA for PowerShell
This app is still under development and thus, unstable. 
**Do not use in production!**
## Description
Splunk TA for PowerShell is an app for Splunk Enterprise that tries to be your one-stop-shop for everything PowerShell in Splunk.

## Features
* Inputs for Windows PowerShell Scriptblock event logs
* Automatic lookup for decoding -EncodedCommands in sysmon events.
* Inputs.conf local blacklisting of some common useless scriptblocks
* Tag and EventType for encoded commands (psencodedcommand) for easier filtering
* Automatically calculated SHA256 hash per unique scriptblock for easy whitelisting and IoC sharing.

## Planned
* Transcript logging
* Module logging if anyone actually cares about it
* PowerShell Core logging on Windows/*nix/MacOS
* Reports & Dashboards

## Depencencies
https://splunkbase.splunk.com/app/742

## How to use
Until this repo is stable, it won't be put on SplunkBase. 

Clone the repo 

``` git clone https://github.com/hampusstrom/TA-PowerShell.git ```

Customize the inputs.conf to your needs and push using your depoyer and/or deploymentserver depending on your needs.


## Contributing
All pull requests are welcome.
