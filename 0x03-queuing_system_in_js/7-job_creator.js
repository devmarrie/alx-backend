import { createQueue } from 'kue';
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

  const queue = createQueue();
  //jobs.forEach((i) => {})

  for (let job = 0; job < jobs.length; job++) {
    const list_job = queue.create('push_notification_code_2', 
                     job).save(function(err) {
                        if(!err) console.log(
                            `Notification job created: ${list_job.id}`
                        );
                     });
    list_job.on('complete', function() {
        console.log('Notification job JOB_ID completed');
    }).on('failed', function(errorMessge) {
        console.log(`Notification job ${list_job.id} failed: ${errorMessge}`);
    }).on ('progress', function(progress) {
        console.log(`Notification job ${list_job.id} ${progress} complete`);
    })
  }