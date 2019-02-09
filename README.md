# serverless-django-boilerplate

## Inspiration

This boilerplate was created using content from [Serverless with Django](https://medium.com/@matias.forbord/starting-serverless-with-django-1b3dda1fb6a) and from [efi-mk/serverless-django-demo](https://github.com/efi-mk/serverless-django-demo).

## Steps

1. Install Serverless CLI in your machine: `npm install -g serverless`
2. Have AWS credentials in your local machine, best option is to use [AWS CLI](https://aws.amazon.com/pt/cli/) or to follow the instruction from [Serverless documentation](https://serverless.com/framework/docs/providers/aws/guide/credentials/)
3. Create your local env for testings your application locally. Use: `virtualenv env` and after activate your local environment, use: `pip install -r requirements.txt` and `python manage.py collectstatic`
4. Install all node packages using: `npm install`
5. Have Docker installed in your machine and run `docker-compose up --build` to have your local database running
6. You have to setup your local environment before, running Django migrations and creating a super user to have access to local admin. Use the command: `sls invoke local -f setup`
7. Check if your application is running locally with: `sls wsgi serve`

## Django Packages

- WhiteNoise: static files from Django
- Django REST Framework
- coreapi (1.32.0+) - Schema generation support
- Markdown (2.1.0+) - Markdown support for the browsable API
- django-filter (1.0.1+) - Filtering support
- django-guardian (1.1.1+) - Object level permissions support
