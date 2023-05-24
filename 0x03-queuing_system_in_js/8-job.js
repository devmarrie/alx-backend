function createPushNotificationsJobs(jobs, queue) {
  if(Array.isArray(jobs)) {
    jobs.forEach((i) => {
      const job = queue.create(
        'push_notification_code_3', i).save(function(err) {
           if(!err) console.log(
            `Notification job created: ${job.id}`
           );
        });

        job.on('complete', function() {
            console.log(`Notification job ${job.id} completed`)
        }).on('failed', function(err) {
            console.log(`Notification job ${job.id} failed: ${err}`)
        }).on('progress', function(progress) {
            console.log(`Notification job ${job.id} ${progress} complete`);
        });
    })
  } else {
    throw  Error('Jobs is not an array');
  }
}
module.exports = createPushNotificationsJobs()