const kue = require('kue');
const queue = kue.createQueue();

const job_data = {
    'phoneNumber': 45678909876,
    'message': 'Customer Notification',
}

const job = queue.create('push_notification_code', 
    job_data).save( function(err) {
        if(err) {
            console.log(err);
        } else {
            console.log(`Notification job created: ${job.id}`)
        }
 });

job.on('complete', function() {
    console.log('Notification job completed');
}).on('failed', function() {
    console.log('Notification job failed');
})