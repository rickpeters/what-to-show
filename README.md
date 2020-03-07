# what-to-show
Another fun project using Pimoroni Inky What and Pimoroni Button Shim to create a display to show several items. Main purpose is to have fun but also to have a demo project to get some experience on two subject:

* TDD : Test Driven Development (in this case using Python)
* Remote Development on Raspberry PI: since I think TDD is a bit of a challenge to do locally on the Raspberry PI I would like to use a IDE that enables me to develop on the Mac and deploy to the Raspberry Pi

First challenge will be to expand on what I want to achieve before I just start to code

## Target environment

A Rapsberry Pi 4 with 4 GB, A Pimoroni Inky What and a Pimoroni Button Shim. This combination should be able to:

* show several 'panels' with information
* use buttons to change what is displayed
* on bootit should have predictable behaviour and show a nice display

## TDD

What framework to use?
Also, it would be nice to be able to test functionality without having the Pi available. A smalle web-interface with the buttons and an image to show the result for the Inky What would be really cool. Challenge foor TDD will be to start really small :-) and where to start, with the browser variant or with the Inky What

## Remote development

Since I already use VSCode it seemed logical to try what was possible. I found this great article from Scott Hanselman on [Visual Studio Remote Development over SSH to Raspberry PI](https://www.hanselman.com/blog/VisualStudioCodeRemoteDevelopmentOverSSHToARaspberryPiIsButter.aspx). I already use the VSCode Remote Development extension so this was a breeze to setup and it worked without any glitch. I also installed a common Python Extension (ms-python.python) and Python Test Explorer (
littlefoxteam.vscode-python-test-adapter) to try this for doing TDD

## Showing panels

The Inky What has a nice library which essentially only allows you to show a PIL image at once. This image can be created using the PIL (or more moder pillow) library. What I would like is an additional abstraction layer that makes it possible to: * divide the What display in several 'panels' that together form te total diaplay area
* it should be possible to manipulate the separate panels
* combining panels into the total image should be transparant
* exporting image to png to be able to show in browser
* the library should have no knowledge of Inky What (the interface is the image)

## Resources

* (Pimoroni Buttonshim)[https://github.com/pimoroni/button-shim]
* (Pimoroni What)[https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-what]
* (Inky Python Library)[https://github.com/pimoroni/inky]
* PIL or pillow[https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html]

## Action Plan

Since I need something that works and something that 'moves' I will start easy.

[x] create a Github project
[x] basic README.md with goals
[x] switch to IDE with remote development
[ ] combine What example for displaying images and Buttonshim example and allow to change pictures using button press
[ ] start working on 'panel' interface with just one panel and show the image using TDD approach
[ ] repeat
[ ] web-interface

