 we can create the 3-tier arch using docker as well.

As the time does not allow me to write all the docker files, build it and orchestrate it with docker composer/swarm or k8s.

i will be listing the setps to achive that.

3 tier involved here would be frontend, backend and database.

Assuming we would have the docker files written for the these components, and we build the images with the following commands:

docker build –t <image name> <path>

and then push it to availble docker registry(private or public) or any external artifactory storage managment like jfrog artifactory or nexus

once the images are pushed to repository. we need to deploy it so that the underlying infra would be created.

For that i would choose eks service of aws, or aks for azure or gke for google cloud as per the cloud provider i will be selecing the respectoive service.

once the cluster will be created i will be creating below k8s resources/ojects.

1. k8s secret : to enable the cluster to fectch the images from external docker registry/

2. k8s namespace: where our backend, fronend and databases will reside as a pod.

3. k8s manifest file: for frontends will be creating deployment defenition files and for database if its production we can create any external db and expose

the endpoints as a service to be consumed by apps. if its dev/test we can create statefulsets for db storage.

4. Expose the services: create Cluster-IP service for internal services communication.

5. Ingress resources: Will create rule for ingress resources (considering ingress controller is alrready installed on our cluster) and expose the

frontends.

6. for further security end points we can enable RBAC and create service accounts with fine grained access and deploy the appliactions there.
