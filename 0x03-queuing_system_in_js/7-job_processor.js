const kue = require('kue');
const queue = kue.createQueue();
const listed = ['4153518780', '4153518781'];


function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (listed.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed().error(new Error(errorMessage));
    console.log(errorMessage)
    done(new Error(errorMessage));
    return;
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

queue.process('push_notification_code_2', 2, function(job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});