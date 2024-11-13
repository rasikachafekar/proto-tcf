# proto-tcf
proof of concept for Tree Conservation Foundation (WIP)

# steps

activate virtual environment
```
python -m venv venv
source venv/bin/activate
```

install packages
```
pip3 install flask requests python-dotenv psycopg2-binary
```

freeze dependencies
```
pip list
pip freeze > requirements.txt
```

## Build docker images

Eventually these need to be setup for pushing to a registry for usage

To build a new tcf app image(increment tag version):
```
cd app
docker build -t tcf:v0.9 .
```

To build a new tb image(increment tag version):
```
cd db
docker build -t pg:v0.4 .
```

## Kompose 
An example for getting k8s .yaml files from the  docker-compose file; a quickstart.

```
kompose convert --out kompose
```

review the files created in the `kompose` folders for the output of the above command.
I haven't yet tested deployment to see if this works, but it should.

## Helm charts

** Not yet being used. **

Under the directory kubernetes, I have created the `charts` subdirectory and `Charts.yaml` as part of setup 

Currently I am using `kubelet apply` to first add config-maps and secrets and then `deployment.yaml`

- Apply for db first and then app.
- Then access app over `localhost:30007`
