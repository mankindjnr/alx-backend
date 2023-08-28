const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message ${message}`);
}

queue.process('push_notification_code', (job, done) => {

    sendNotification(job.data.phoneNumber, job.data.message);
    setTimeout(() => {
        const isFailing = Math.random() < 0.2;

        if (isFailing) {
            console.log('Notification job failed');
            done(new Error('Job failed'));
        } else {
            done();
        }
    }, 1000);
});
