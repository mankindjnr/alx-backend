const kue = require('kue');
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Tracking progress: 0 out of 100
  
  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    job.failed(errorMessage);
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100); // Tracking progress: 50 out of 100
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Job processing logic
queue.process('push_notification_code_2', 2, (job, done) => {
  const phoneNumber = job.data.phoneNumber;
  const message = job.data.message;
  
  sendNotification(phoneNumber, message, job, done);
});

// Handle queue errors
queue.on('error', err => {
  console.error('Queue error:', err);
});
