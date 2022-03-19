from charms.reactive import hook, when, when_not, set_state, remove_state
from charmhelpers.core import hookenv

import charmhelpers.contrib.ansible


def run_install():
    charmhelpers.contrib.ansible.install_ansible_support()
    extra_vars = {
        "search_domains": hookenv.config('search_domains')
    }
    charmhelpers.contrib.ansible.apply_playbook(
        'playbooks/install.yml',
        extra_vars=extra_vars,
    )

    set_state('k8s-charm-static-ip.installed')
    hookenv.status_set('active', 'Done.')


@when_not('k8s-charm-static-ip.installed')
def install_k8s_charm_static_ip():
    run_install()


@hook('upgrade-charm')
def upgrade_charm():
    run_install()


@when('actions.rerun')
def rerun():
    run_install()
    remove_state('actions.rerun')
