const express = require('express')
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const app = express()

const shareFilePath = '/share/main.py'
var command = 204

app.listen(3000)

/*
    200 - OK
    202 - Accepted
    204 - No Content
    409 - Conflict
*/

function getInput()
{
    rl.question('Enter a command > ', (cmd) => {

        if      (cmd === 'send')
        {
            console.log('Sending code to the robot');
            command = 200
        }

        else if (cmd === 'sendRun')
        {
            console.log('Sending and running code to the robot');
            command = 202
        }
            
        else if (cmd === 'stop')
        {
            console.log('Stopping code execution');
            command = 409
        }

        else
            command = 204
            
        getInput()
    });

}


app.get('/', (req, res) => {

    res.status(command)
    res.download(__dirname + shareFilePath)

    if (command != 204)
        command = 204

});

getInput()

