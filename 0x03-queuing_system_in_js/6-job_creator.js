const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
    phoneNumber: "1234567890",
    message: "Whats up gee",
}

const notification = queue.create("push_notification_code", jobData).save(err => {
    if (!err) {
	console.log('Notification job created:', notification.id);
    }
});

queue.on('error', err => {
    console.error('Queue error:', err);
});

