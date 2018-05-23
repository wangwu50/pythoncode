from kubernetes import client, config

config.load_kube_config()
v1 = client.AppsV1Api()
deployList = v1.list_namespaced_deployment('default')
for i in deployList.items:
    print(type(i))
    print(i.metadata.name)
