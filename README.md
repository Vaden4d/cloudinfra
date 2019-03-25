# cloudinfra
Cloud infrastructure tasks at UCU (2019)

## 1. Dockerfile + service
Run application locally:

- clone repository: `git clone https://github.com/Vaden4d/cloudinfra.git`
- run `docker build -t hm-korshunov .`
- run `docker run -d -p 5000:5000 --rm --name cloud-infra hm-korshunov`

Then go to `localhost:5000` and read the internal content. 
To stop and remove container run:

`docker container stop $(docker container ls -f "name=cloud-infra" -q)` .