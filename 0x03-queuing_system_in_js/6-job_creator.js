const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: "1234567890",
    message: "This is the code to verify your account",
}

const notification = queue.create("push_notification_code", jobData).save(err => {
    if (!err) {
	console.log('Notification job created:', notification.id);
    }
});

queue.on('error', err => {
    console.error('Queue error:', err);
});

