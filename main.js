const { app, BrowserWindow } = require('electron')
const path = require('path')
const JobQueue = require('./js/jobqueue.js')
const jobQueue = new JobQueue()
var zerorpc = require('zerorpc')

// Create zeroRPC client
var client = new zerorpc.Client()
client.connect('tcp://127.0.0.1:9105')

// Create zeroRPC server
var server = new zerorpc.Server({
  hello: function (name, reply) {
    reply(null, 'Hello, ' + name)
  },
  progress: function (progress, reply) {
    // Do something with progress
    console.log('Node.js zeroRPC: Progress: ' + progress)
    // Send the acknowledgement back to the client
    reply(null, 'Progress = ' + progress)
  },
  finished: function (reply) {
    // Do something now that we're finished
    console.log('Node.js zeroRPC: Processing finished.')
    // Send the acknowledgement back to the client
    reply(null, 'Finished.')
  }
})

server.bind('tcp://127.0.0.1:9106')

// global reference to the window object
let win
// global reference to forked python process and running port
let pyProc = null
let pyPort = null

function createWindow () {
  let win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  })

  win.loadFile('index.html')
  win.webContents.openDevTools()
  win.on('closed', () => {
    win = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (win === null) {
    createWindow()
  }
})

// Tell CV code to begin operating
function startWorking (job) {
  client.invoke('startWorking', job.input, job.output, function (error, res, more) {
    if (error) {
      console.log(error)
      return
    }
    console.log(res)
  })
}

/*************************************************************
 * py process, code extracted from
 * https://github.com/fyears/electron-python-example
 *************************************************************/
const PY_DIST_FOLDER = 'python_backenddist'
const PY_FOLDER = 'python_backend'
const PY_MODULE = 'api' // without .py suffix

const guessPackaged = () => {
  const fullPath = path.join(__dirname, PY_DIST_FOLDER)
  return require('fs').existsSync(fullPath)
}

const getScriptPath = () => {
  if (!guessPackaged()) {
    return path.join(__dirname, PY_FOLDER, PY_MODULE + '.py')
  }
  if (process.platform === 'win32') {
    return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE + '.exe')
  }
  return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE)
}

const selectPort = () => {
  pyPort = 9105
  return pyPort
}

const createPyProc = () => {
  console.log('creating python child process')
  const script = getScriptPath()
  const port = '' + selectPort()

  if (guessPackaged()) {
    pyProc = require('child_process').execFile(script, [port])
  } else {
    pyProc = require('child_process').spawn('python3', [script, port], { stdio: [process.stdin, process.stdout, process.stderr] })
  }

  if (pyProc != null) {
    console.log('child process success on port ' + port)
  }
}

const exitPyProc = () => {
  pyProc.kill()
  pyProc = null
  pyPort = null
}

app.on('ready', createPyProc)
app.on('will-quit', exitPyProc)

// TEST STUFF
jobQueue.push('hi', 'bye')
app.on('ready', () => { startWorking(jobQueue.pop()) })
