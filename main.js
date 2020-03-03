const { ipcMain, dialog, app, BrowserWindow } = require('electron')
// var zerorpc = require('zerorpc')
const net = require('net')
const path = require('path')
const JobQueue = require('./global_scripts/jobqueue.js')
let jobQueue = new JobQueue()

global.appRoot = path.resolve(__dirname);

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

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
// function selectFiles (callbackfn) {
//   dialog.showOpenDialog(win, { properties: ['openFile', 
//                         'openDirectory', 'multiSelections'] }, (files) => {
//     if (typeof callbackfn === 'function' && callbackfn()) {
//       callbackfn(files)
//     }
//   })
// }


ipcMain.on('submit-job', (event, arg) => {

    console.log('received job')
    console.log(arg)

    // jobQueue.push(arg.in[0], arg.out[0]);
});

// nodeJS zeroRPC connection
// var client = new zerorpc.Client()
// client.connect('tcp://127.0.0.1:4242')

// Handle incoming python communications
const server = net.createServer((connection) => {
  console.log("Connection from Python client established.");

    connection.on('end', () => {
        console.log('Client disconnected.');
    });

    connection.on('data', (data) => {
      str_data = data.toString();
      // TODO : USE DATA HERE
    })
});

server.listen(5729, () => {
    console.log("Listening on port 5729.")
});
console.log("Started listening, past listen() call");

// Send outgoing communications to python
const client = net.createConnection({port: 5728}, () => {
    console.log("Connection to server established.");
});

// On incoming message
client.on('data', (data) => {
    console.log("Receiving data: ");
    console.log(data.toString());

    str_data = data.toString();

    // Message is a job status
    if str_data[0] == '1' {
    	console.log("Job status: " + str_data.slice(1));
    }
    // Message is a finished filename
    else if str_data[0] == '2' {
    	console.log("Finished job " + str_data.slice(1));
    }
});

// On connection end
client.on('end', () => {
    console.log('Disconnected from Python server.');
});

function startJob(filename) {
	client.write("0" + filename);
}

function requestStatus(filename) {
	client.write("1" + filename);
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
