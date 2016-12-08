from charmhelpers.core.hookenv import (
    action_fail,
    action_set,
)

from charms.reactive import (
    when,
    remove_flag,
)
import charms.sshproxy


@when('actions.start')
def start():
    err = ''
    try:
        # Enter the command to start your service(s)
        cmd = "service myname start"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.start')


@when('actions.stop')
def stop():
    err = ''
    try:
        # Enter the command to stop your service(s)
        cmd = "service myname stop"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.stop')


@when('actions.restart')
def restart():
    err = ''
    try:
        # Enter the command to restart your service(s)
        cmd = "service myname restart"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.restart')


@when('actions.reboot')
def reboot():
    err = ''
    try:
        # Enter the command to reboot the machine
        cmd = "reboot"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.reboot')
