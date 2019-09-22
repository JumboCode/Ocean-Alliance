# Ocean-Alliance
JumboCode 2019-2020 project for Ocean Alliance, led by Danielle Lan.

# Environment setup
We will use Electron for this project, which is built upon Node.js.

If you are on Windows and love working in WSL (Windows Subsystem for Linux), you should just develop in Windows; trust me, I've tried to make it work.

If you need a editor recommendation, VS Code is what I (Danielle) am using, and it works fairly well with JavaScript.

<!-- # TODO: double check if opencv4nodejs already has opencv installed
Before everything else, install OpenCV 4. I promise this is the worst part of the setup process; it's only going to be easier after this. Look up installation instructions for OpenCV4 on your OS and follow along. You'd also want to get opencv_contrib, which contains additional stuff not included in stock opencv.
* Windows: 
  * https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html
  * Go to the part that says "Installation by Using git-bash and cmake"
* Linux:
  * If npm install opencv fails later, check out this github issue https://github.com/peterbraden/node-opencv/issues/325 -->

Create a folder where you will work on the code. Initialize git there, and pull from this repo. If you are working on MacOS or Windows, you might want to try out sourcetree, a graphical git interface. Some PMs swear by it, and claimed that they never needed to learn git commands because of it.

Go through the [environment setup page for Electron](https://electronjs.org/docs/tutorial/development-environment), to set up Node.js and NPM.

Install the packages used in this boilerplate (including Electron) by doing `npm install`. This downloads all packages listed in `package.json`.
Currently this includes:
1. Electron
2. Bootstrap
3. jQuery
4. Popper.js (a Bootstrap dependency)
5. opencv4nodejs

These are just some nice libraries I've been using when doing websites stuff. If you have preferred libraries that you want, we can talk about it; I'm a bit OOTL on what js frameworks that the cool kids are using these days.

This boilerplate code implements everything from the [Electron getting started tutorial](https://electronjs.org/docs/tutorial/first-app). To run it, do `npm start`. The OpenCV test code are snippets from https://www.npmjs.com/package/opencv4nodejs#quick-start.
