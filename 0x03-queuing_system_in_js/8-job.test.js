const createPushNotificationsJobs = require('./8-job');
const { expect } = require('chai');
const queue = require('kue').createQueue();

before( function() {
    queue.testMode.enter(true);
});

afterEach( function() {
    queue.testMode.clear();
});

after( function() {
    queue.testMode.exit();
});

describe('createPushNotificationsJobs', function() {
    it('should check the type of job value', function() {
      expect(() => createPushNotificationsJobs('jobs', queue)).to.throw( Error, 'Jobs is not an array');
    });

    it('should test weather the jobs are created successfully', function() {
        const jobs = [
            {
              phoneNumber: '4153518780',
              message: 'This is the code 1234 to verify your account'
            },
            {
              phoneNumber: '4153518781',
              message: 'This is the code 4562 to verify your account'
            },
          ];
        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);

        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.equal(jobs[0]);

        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.equal(jobs[1]);
    });
});

