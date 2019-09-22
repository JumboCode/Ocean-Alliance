# Ocean-Alliance
JumboCode 2019-2020 project for Ocean Alliance, led by Danielle Lan.

# Team Members
`Add yourself here by creating a new branch, make changes, then pull to practice git`

- Danielle Lan, PM, Should've gone to culinary school
- [Name], [Role], [Something about you]

# Environment setup
We will use Electron for this project, which is built upon Node.js.

If you are on Windows and love working in WSL (Windows Subsystem for Linux), you should just develop in Windows; trust me, I've tried to make it work.

If you need a editor recommendation, VS Code is what I (Danielle) am using, and it works fairly well with JavaScript.

Create a folder where you will work on the code. Initialize git there, and pull from this repo. If you are working on MacOS or Windows, you might want to try out sourcetree, a graphical git interface. Some PMs swear by it, and claimed that they never needed to learn git commands because of it.

Go through the [environment setup page for Electron](https://electronjs.org/docs/tutorial/development-environment), to set up Node.js and NPM.

If you are on Windows, run `npm install --global windows-build-tools` from an elevated terminal. This installs the build tools required for opencv. If you don't already have cmake, install that too; [binaries here](https://cmake.org/download/). If `npm install` complains not finding Visual Studio later, just reboot.

Install the packages used in this boilerplate (including Electron) by doing `npm install`. This downloads all packages listed in `package.json`.
Currently this includes:
1. Electron
2. Bootstrap
3. jQuery
4. Popper.js (a Bootstrap dependency)
5. opencv4nodejs

These are just some nice libraries I've been using when doing websites stuff. If you have preferred libraries that you want, we can talk about it; I'm a bit OOTL on what js frameworks that the cool kids are using these days.

This boilerplate code implements everything from the [Electron getting started tutorial](https://electronjs.org/docs/tutorial/first-app). To run it, do `npm start`. The OpenCV test code are snippets from https://www.npmjs.com/package/opencv4nodejs#quick-start.

# Coding Styles
`npm test` checks if the code passes the linters, and `npm fix` attempts to fix some javascript violations automatically.

This project tries to conform with the Standard JS style, with details [here](https://standardjs.com). [Install editor plugins to make your life easier](https://standardjs.com/#are-there-text-editor-plugins).

[HTMLHint](https://github.com/htmlhint/HTMLHint) is used as the linter for HTML. It also has plugins to editors (for VS Code at least).

# Other Links
- [Design Doc](https://docs.google.com/document/d/1I9zuQFTHVh6-9p7bcbBr22b-NnZ1on00LuRBD89p7x4/edit?usp=sharing)
- [Files](https://www.dropbox.com/sh/lo8qht7d1kfq35z/AABrX-oU-obZyjvL28C9L02Ea?dl=0)
