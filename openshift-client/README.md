# About
A dockerfile used to create image containing openshift origin client tool
installed and ready to use.

# Run
You can give openshift client commands directly when starting the container:
```
$ docker run <image> --help
$ docker run <image> login
$ docker run <image> status
```

You can also override the entrypoint which is the oc binary. This example
sets the entrypoint to bash shell. Which allows us to run many commands inside
the container:
```
$ docker run -it --entrypoint /bin/bash <image>
```