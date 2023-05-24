import { create } from 'domain';
import { createClient } from 'redis';
const kue = require('kue');
const util = require('util');
const express = require('express')

const port = 1245;
const redis_port = 6379;
const app = express()
const reservationEnabled = true;
const queue = kue.createQueue();


const client = createClient(redis_port);

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(err) {
    console.log(`Redis client not connected to the server ${err}`);
});


function reserveSeat(number, ) {
  client.set('available_seats', number);
}

const asyncGet = util.promisify(client.get).bind(client);
    
async function getCurrentAvailableSeats() {
  const seats = await asyncGet('available_seats');
  return seats;
}

app.get('/available_seats', (req, res) => {
    const availble = getCurrentAvailableSeats()
    res.json({"numberOfAvailableSeats": availble})
});

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.json({"status": "Reservation are blocked"});
        return;
      }
      const job = queue.create('reserve_seat', {'seat': 1}).save((error) => {
        if (error) {
          res.json({"status": "Reservation failed"});
          return;
        } else {
          res.json({"status": "Reservation in process"});
          job.on('complete', function () {
          console.log(`Seat reservation job ${job.id} completed`);
          });
          job.on('failed', function(error) {
            console.log(`Seat reservation job ${job.id} failed: ${error}`);
          });
        }
      });
    });

app.get('/process', (req,res) => {
    res.json({ "status": "Queue processing" });
    queue.process('reserve_seat', async function(job, done) {
        const available = Number(await getCurrentAvailableSeats());
        if (available === 0) {
            reservationEnabled = false;
            done(Error('Not enough seats available'));
        } else {
            reserveSeat(available - 1);
            done();
        }
    });
});

app.listen(port, () => {
    console.log(`Application listening on port ${port}`)
});

reserveSeat(100);