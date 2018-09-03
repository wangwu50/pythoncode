from kubernetes import client, config

config.load_kube_config()
v1 = client.AppsV1Api()
v1.patch_namespaced_deployment('wang-nginx', 'default', {'spec': {'progressDeadlineSeconds': 601}})
