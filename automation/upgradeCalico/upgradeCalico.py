import subprocess
from kubernetes import client, config


def upgrade_calico():
    # upgrade_controllers
    upgrade_controllers()
    # upgrade_nodes
    upgrade_nodes()


def upgrade_controllers():
    print('upgrade_controllers start')
    subprocess.call('kubectl apply -f calico-controller.yaml')
    subprocess.call('kubectl apply -f rbac.yaml')


def upgrade_nodes():
    print('upgrade_nodes start')
    backup_calico_policy()
    ensure_update_strategy()
    upgrade_calico_node()


def upgrade_calico_node():
    # kubectl cordon
    # kubectl delete po
    # kubectl uncordon
    pass


def backup_calico_policy():
    subprocess.call('calicoctl get policy -o yaml > policys.yaml')


def ensure_update_strategy():
    config.load_kube_config()
    v1 = client.AppsV1Api()
    ds = v1.read_namespaced_daemon_set('calico-node', 'kube-system')
    if ds.spec.update_strategy.type != 'OnDelete':
        v1.patch_namespaced_daemon_set('calico-node', 'kube-system', {'spec': {'updateStrategy': {'type': 'OnDelete'}}})


if __name__ == '__main__':
    upgrade_calico()
