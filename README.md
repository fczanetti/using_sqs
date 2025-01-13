# SQS

Basic project to document the basics of using AWS SQS Service

## Create a simple Django project
This is a very simple project. It has only one view that register some data in the database when it receives http requests. To register these data, we have a task that is called in the view.

## Configure Celery
We also need Celery to be able to queue tasks to be executed asynchronously. The basic instructions from their docs are enough.

- https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps
- https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
- https://celery-safwan.readthedocs.io/en/latest/getting-started/brokers/sqs.html

## Create an AWS account
It'll be necessary to have an AWS account for you to create an SQS Queue and a IAM user. The IAM user is good because you can allow this user to access the SQS Queues and only the SQS Queues, making it more safe and restrict.

## Create an IAM user
When creating this user, insert on it a policy called "AmazonSQSFullAccess". For this user, you also need to create an AWS access key. The access key and the secret access key will be used to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

## Create an SQS Queue
Just create a simple SQS Queue on AWS. It's not necessary to set any policy allowing access on it. Of course it may be a good idea, but for this simple project we can leave it empty;

## Start database
This command has to be run from the root of the project, where `docker-compose.yml` is located.
```
docker compose up -d
```

## Start Django server
``` 
manage.py runserver
```

## Start Celery worker
```
celery -A sqs worker -Q using-sqs -l INFO
```

When you send an http request to the endpoint created on this project, you'll see Celery worker logging information about the task being executed.

These are the most basic configurations to have AWS SQS working for us.
