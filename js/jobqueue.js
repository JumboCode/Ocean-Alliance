const fs       = require('fs');
const electron = require('electron');
const path     = require('path');
const userPath = (electron.app || electron.remote.app).getPath('appData') + 
                 path.sep + 'jobqueue.json';

class JobQueue
{
    // constructor
    // Description: Construct a JobQueue object.
    //              NOTE: you should only use a single JobQueue object at once,
    //                    since all JobQueue objects sync to the same file.
    // Parameters:  n/a
    // Returns:     A JobQueue object.
    constructor()
    {
        if (fs.existsSync(userPath)) {
            this.data = this.readFromDisk();
        } else {
            this.data = []
            this.syncToDisk();
        }
    }

    // push
    // Description: Push an item onto the JobQueue.
    // Parameters:  inputPath - the path of the input for the job.
    //              outputPath - the path of the output for the job.
    // Returns:     n/a
    push(inputPath, outputPath)
    {
        this.data.unshift({input:  inputPath, 
                           output: outputPath});
        this.syncToDisk();
    }

    // pop
    // Description: Pop an item from the JobQueue.
    // Parameters:  n/a
    // Returns:     {input, output} - The input and output paths of the next
    //              job on the queue.
    pop()
    {
        var item = this.data.pop();
        this.syncToDisk();
        return item;
    }

    // length
    // Description: Returns the length of the JobQueue.
    // Parameters:  n/a
    // Returns:     The length of the JobQueue.
    length()
    {
        return this.data.length
    }

    // isEmpty
    // Description: Checks if the JobQueue is empty.
    // Parameters:  n/a
    // Returns:     True if the JobQueue is empty, false otherwise.
    isEmpty()
    {
        return this.data.length == 0;
    }

    // clear
    // Description: Empties the JobQueue.
    // Parameters:  n/a
    // Returns:     n/a
    clear()
    {
        this.data = []
        this.syncToDisk();
    }

    // "private" functions

    // Gets the current JobQueue stored on disk.
    readFromDisk()
    {
        return JSON.parse(fs.readFileSync(userPath));
    }

    // Writes the current JobQueue to disk.
    syncToDisk()
    {
        fs.writeFileSync(userPath, JSON.stringify(this.data));
    }
}

module.exports = JobQueue
