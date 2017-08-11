from charmhelpers.core.hookenv import (
    action_fail,
    action_set,
    config,
    log,
)

from charms.reactive import (
    when,
    remove_state as remove_flag,
)
import charms.sshproxy
import os.path
import yaml


@when('hooks.config-changed')
def config_changed_persistent():
    """Persist the configuration change for use by the collect-metrics hook."""
    # TODO: Verify if this is necessary. It *should* be called automatically,
    # but we might want to force it for our use.
    cfg = config()
    cfg.save()
    pass


@when('actions.reboot')
def reboot():
    """Reboot the VNF."""
    err = ''
    try:
        result, err = charms.sshproxy._run("reboot")
    except:
        action_fail('command failed:' + err)
    else:
        action_set({'outout': result})
    finally:
        remove_flag('actions.reboot')


# @when('hooks.collect-metrics')
# def metrics():
#     """Handle collect-metrics hook."""
#     err = ''
#     try:
#         # Read metrics.yaml
#         charm_dir = os.path.dirname(
#             os.path.abspath(
#                 os.path.join(__file__, "..")
#             )
#         )
#         metrics_yaml = os.path.join(charm_dir, "metrics.yaml")
#         with open(metrics_yaml) as f:
#             doc = yaml.load(f)
#             metrics = doc.get("metrics", {})
#             for metric, mdoc in metrics.items():
#                 # Find command: stanza
#                 cmd = mdoc.get("command")
#                 if cmd:
#                     log('Collecting metric `{}`'.format(metric))
#                     # Execute command via charms.proxy
#                     result, err = charms.sshproxy._run(cmd)
#
#                     # Add the returned metric
#                     charms.sshproxy.run_local(
#                         "add-metric {}={}".format(metric, result)
#                     )
#     except:
#         action_fail('command failed:' + err)
#     else:
#         action_set({'outout': result})
#     finally:
#         remove_flag('actions.reboot')

###############################################################################
# Below is an example implementation of the start/stop/restart actions.       #
# To use this, copy the below code into your layer and add the appropriate    #
# command(s) necessary to perform the action.                                 #
###############################################################################

# @when('actions.start')
# def start():
#     err = ''
#     try:
#         cmd = "service myname start"
#         result, err = charms.sshproxy._run(cmd)
#     except:
#         action_fail('command failed:' + err)
#     else:
#         action_set({'outout': result})
#     finally:
#         remove_flag('actions.start')
#
#
# @when('actions.stop')
# def stop():
#     err = ''
#     try:
#         # Enter the command to stop your service(s)
#         cmd = "service myname stop"
#         result, err = charms.sshproxy._run(cmd)
#     except:
#         action_fail('command failed:' + err)
#     else:
#         action_set({'outout': result})
#     finally:
#         remove_flag('actions.stop')
#
#
# @when('actions.restart')
# def restart():
#     err = ''
#     try:
#         # Enter the command to restart your service(s)
#         cmd = "service myname restart"
#         result, err = charms.sshproxy._run(cmd)
#     except:
#         action_fail('command failed:' + err)
#     else:
#         action_set({'outout': result})
#     finally:
#         remove_flag('actions.restart')
#
#
