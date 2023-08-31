const kue = require('kue');
const chai = require('chai');
const sinon = require('sinon');
const sinonChai = require('sinon-chai');

const expect = chai.expect;
chai.use(sinonChai);

describe('createPushNotificationsJobs', () => {
  let sandbox, queueStub;

  beforeEach(() => {
    sandbox = sinon.createSandbox();
    queueStub = {
      create: sandbox.stub().returnsThis(),
      on: sandbox.stub().returnsThis(),
      save: sandbox.stub()
    };
  });

  afterEach(() => {
    sandbox.restore();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidJobs = 'not an array';
    expect(() => createPushNotificationsJobs(invalidJobs, queueStub)).to.throw('Jobs is not an array');
  });

  it('should create and save jobs for each job data', () => {
    const validJobs = [{ id: 1 }, { id: 2 }];
    createPushNotificationsJobs(validJobs, queueStub);

    expect(queueStub.create).to.have.been.calledTwice;
    expect(queueStub.save).to.have.been.calledTwice;
  });

  it('should set up event listeners for each job', () => {
    const validJobs = [{ id: 1 }, { id: 2 }];
    createPushNotificationsJobs(validJobs, queueStub);

    expect(queueStub.on).to.have.been.calledWith('enqueue');
    expect(queueStub.on).to.have.been.calledWith('complete');
    expect(queueStub.on).to.have.been.calledWith('failed');
    expect(queueStub.on).to.have.been.calledWith('progress');
  });

  it('should log correct messages on event triggers', () => {
    const validJobs = [{ id: 1 }, { id: 2 }];
    createPushNotificationsJobs(validJobs, queueStub);

    const fakeJob = { id: 'fakeJobId' };
    queueStub.create.returns(fakeJob);

    queueStub.on.withArgs('enqueue').callArg(1);
    queueStub.on.withArgs('complete').callArg(1);
    queueStub.on.withArgs('failed').callArgWith(1, 'Fake Error');
    queueStub.on.withArgs('progress').callArgWith(1, 50);

    expect(console.log).to.have.been.calledWith(`Notification job created: ${fakeJob.id}`);
    expect(console.log).to.have.been.calledWith(`Notification job ${fakeJob.id} completed`);
    expect(console.log).to.have.been.calledWith(`Notification job ${fakeJob.id} failed: Fake Error`);
    expect(console.log).to.have.been.calledWith(`Notification job ${fakeJob.id} 50% complete`);
  });
});
