const $ = require('jquery')
const zerorpc = require('zerorpc')

const port = 9105

var client = new zerorpc.Client()
client.connect('tcp://127.0.0.1:' + port)
console.log('Renderer: tcp connection to ' + port + ' success')

client.invoke('echo', 'server ready', (error, res) => {
  if (error || res !== 'server ready') {
    console.error(error)
  } else {
    console.log('server is ready')
  }
})

console.log('registering click')
$('#pingPython').click(function () {
  console.log('clicking button')

  client.invoke('ping', function (error, res, more) {
    if (error) {
      console.log(error.stack)
    } else {
      console.log('recieved result ' + res)
      $('#pingResponse').text(res)
    }
  })
})
