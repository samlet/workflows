## start
⊕ [workshop/lab1a.md at master · openfaas/workshop](https://github.com/openfaas/workshop/blob/master/lab1a.md)

```sh
$ docker swarm init
$ git clone https://github.com/openfaas/faas
$ cd faas && \
  git checkout master

$ ./deploy_stack.sh
# Attempting to create credentials for gateway..
n1nc3e2q2i0xle1w9q126d36n
rntmzkexrn217f4zmq8jkmf94
[Credentials]
 username: admin 
 password: f8ac700f698f9d6323bb4c6fae8228d2f6ced62b2d91154732b4e06bee52628c
 echo -n f8ac700f698f9d6323bb4c6fae8228d2f6ced62b2d91154732b4e06bee52628c | faas-cli login --username=admin --password-stdin
# Enabling basic authentication for gateway..
# Your gateway URL is: http://127.0.0.1:8080

# This exports your password to and environment variable for use in the following commands
# export PASSWORD=<password-printed-in-console>
export PASSWORD=f8ac700f698f9d6323bb4c6fae8228d2f6ced62b2d91154732b4e06bee52628c

# This command sets the URL for the gateway, used by the faas-cli command
export OPENFAAS_URL=http://127.0.0.1:8080

# This command logs in and saves a file to ~/.openfaas/config.yml
echo -n $PASSWORD | faas-cli login --username admin --password-stdin
# Check if the services are up and showing 1/1 for each:
$ docker service ls
```

⊕ [workshop/lab2.md at master · openfaas/workshop](https://github.com/openfaas/workshop/blob/master/lab2.md)

+ deploy functions

```sh
# We can deploy some sample functions and then use them to test things out:
$ faas-cli deploy -f https://raw.githubusercontent.com/openfaas/faas/master/stack.yml
# 或者直接在ui上部署: You can deploy a function from the OpenFaaS store.

# show the functions, how many replicas you have and the invocation count.
$ faas-cli list
$ faas-cli list -v

# Pick one of the functions you saw appear on faas-cli list such as markdown:
$ faas-cli invoke markdown
# Reading from STDIN - hit (Control + D) to stop.
$ echo Hi | faas-cli invoke markdown
$ uname -a | faas-cli invoke markdown
$ cat lab2.md | faas-cli invoke markdown
```

+ monitoring dashboard

```sh
$ docker service create -d \
--name=grafana \
--publish=3000:3000 \
--network=func_functions \
stefanprodan/faas-grafana:4.6.3

$ open http://127.0.0.1:3000/dashboard/db/openfaas
# 用户名和密码均为admin
```

⊕ [workshop/lab3.md at master · openfaas/workshop](https://github.com/openfaas/workshop/blob/master/lab3.md)

```sh
$ faas-cli template pull
$ faas-cli new --list

# $ faas-cli new --lang python3 hello-openfaas --prefix="<your-docker-username-here>"
$ faas-cli new --lang python3 hello-openfaas --prefix="samlet"

# you can also override the default gateway URL of 127.0.0.1:8080 with an environmental variable: export OPENFAAS_URL=127.0.0.1:31112.

$ faas-cli up -f hello-openfaas.yml
# faas-cli up command combines build, push and deploy commands of faas-cli in a single command.

$ faas-cli invoke hello-openfaas
$ echo hi | faas-cli invoke hello-openfaas
# Functions can be invoked via a GET or POST method only.
$ curl http://127.0.0.1:8080/function/hello-openfaas
```

```sh
$ faas-cli new --lang python3 astronaut-finder --prefix="samlet"
# Edit ./astronaut-finder/requirements.txt
#   requests
# Update handler.py ...

$ faas-cli build -f ./astronaut-finder.yml
# $ faas-cli push -f ./astronaut-finder.yml
$ faas-cli deploy -f ./astronaut-finder.yml

# Invoke the function
$ echo | faas-cli invoke astronaut-finder
# Anton Shkaplerov is in space
$ echo | faas-cli invoke astronaut-finder
# Joe Acaba is in space

# Troubleshooting: find the container's logs
$ docker service logs -f astronaut-finder
```

* Troubleshooting: verbose output with write_debug
    * https://github.com/openfaas/workshop/blob/master/lab3.md#troubleshooting-verbose-output-with-write_debug

Edit your YAML file for the function and add an "environment" section.

```yaml
  astronaut-finder:
    lang: python3
    handler: ./astronaut-finder
    image: astronaut-finder
    environment:
      write_debug: true
```

Now deploy your function again with faas-cli deploy -f ./astronaut-finder.yml.
Invoke the function and then checkout the logs again to view the function responses:

```sh
$ faas-cli deploy -f ./astronaut-finder.yml
$ docker service logs -f astronaut-finder
# astronaut-finder.1.tp6k14i8kf6s   | 2019/04/25 18:28:36 Forking fprocess.
# astronaut-finder.1.tp6k14i8kf6s   | 2019/04/25 18:28:36 Query  
# astronaut-finder.1.tp6k14i8kf6s   | 2019/04/25 18:28:36 Path  /
# astronaut-finder.1.tp6k14i8kf6s   | 2019/04/25 18:28:37 Duration: 1.128897 seconds
# astronaut-finder.1.tp6k14i8kf6s   | Alexey Ovchinin is in space
```
