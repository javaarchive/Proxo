

# Proxo - Remaking Reverse proxies
Github: [Releases](https://github.com/javaarchive/Proxo/releases)
Proxo is a Python flask project aiming to make reverse proxying better and easier. Proxo is currently a small project and isn't very stable. 
## Installation

[details="Deprecated steps"]
This will copy my developement version of proxo which I sometimes use to do other things
 1. Make a copy of this project on glitch: https://glitch.com/~epic-proxy(or download the code if you are running it locally)
[/details]

Current Steps(with github):
 1. Download a release from github and copy all the files in `Proxo-Someversion`  to your glitch directory
 2. Open `configuration.py` and find the line that defines the `origins` variable
 3. Find the line that has the `main` origin and set it to the url of your origin server. This can be a external server or a server on the same machine(use `localhost`  or `127.0.0.1` to maximize speed). 
 4. If you are in glitch the app will automatically restart and mirror your origin and you are done. If you are deploying locally proceed to step 5
 5. Find the line that starts with `"start":` and copy the command in the quotes and run it to start the server(optionally configure the port in `configuration.py`)
You're done! Your proxy is now setup. 
## Configuration
To be written
## Stability
The only possible ways of crashing are either the logging fails because there are so many workers or the app gets a request that isn't a `POST` or `GET`. 
For now the applicaton assumes all origin servers send the Content-Type header, so it will crash if your server is very minimal. 
## For future reference
In the future(by I mean very soon), I will start pointing everyone to a github release page to install Proxo instead of the glitch project because I will continue to use it for developement. I will provide everyone with a script that installs any Proxo you want from the release page. 
## For fun
See [releases](https://github.com/javaarchive/Proxo/releases)
I used proxo to make a mirror of github and glitch.com for fun. I just love to make web proxies!
## Install Script
It's work in progress
> Written with [StackEdit](https://stackedit.io/).
