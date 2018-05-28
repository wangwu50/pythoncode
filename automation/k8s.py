from kubernetes import client, config

config.load_kube_config()
betav1 = client.AppsV1beta1Api()
namespace = 'default'
deployList = betav1.list_namespaced_deployment(namespace)
for deploy in deployList.items:
    deploy.spec.selector.match_labels = {'app': deploy.metadata.name}
    dlabel = deploy.metadata.labels
    dlabel["service"] = deploy.metadata.name
    dlabel["log-realTime"] = "realTimeEnable"
    dlabel["log-hdfs"] = "hdfsEnable"
    dlabel["log-splunk"] = "splunkEnable"
    dlabel["log-fds"] = "fdsDisable"
    podlabel = deploy.spec.template.metadata.labels
    podlabel["service"] = deploy.metadata.name
    podlabel["log-realTime"] = "realTimeEnable"
    podlabel["log-hdfs"] = "hdfsEnable"
    podlabel["log-splunk"] = "splunkEnable"
    podlabel["log-fds"] = "fdsDisable"
    betav1.replace_namespaced_deployment(deploy.metadata.name, namespace, deploy)
stsList = betav1.list_namespaced_stateful_set(namespace)
for sts in stsList.items:
    sts.spec.selector.match_labels = {'app': sts.metadata.name}
    dlabel = sts.metadata.labels
    dlabel["service"] = sts.metadata.name
    dlabel["log-realTime"] = "realTimeEnable"
    dlabel["log-hdfs"] = "hdfsEnable"
    dlabel["log-splunk"] = "splunkEnable"
    dlabel["log-fds"] = "fdsDisable"
    podlabel = sts.spec.template.metadata.labels
    podlabel["service"] = sts.metadata.name
    podlabel["log-realTime"] = "realTimeEnable"
    podlabel["log-hdfs"] = "hdfsEnable"
    podlabel["log-splunk"] = "splunkEnable"
    podlabel["log-fds"] = "fdsDisable"
    sts.metadata.resource_version = ""
    data = betav1.delete_namespaced_stateful_set(sts.metadata.name, namespace, sts, propagation_policy='Orphan')
    print(data)
    betav1.create_namespaced_stateful_set(namespace, sts)
