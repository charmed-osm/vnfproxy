# vnfproxy

## Overview

This charm layer is intended for use by vendors who wish to integrate with
OSM. The current release of OSM only supports a lightweight version of Juju
charms, which we will refer to as "proxy charms". Consider the diagram below:

```
+---------------------+    +---------------------+
|                     <----+                     |
|  Resource           |    |  Service            |
|  Orchestrator (RO)  +---->  Orchestrator (SO)  |
|                     |    |                     |
+------------------+--+    +-------+----^--------+
                   |               |    |
                   |               |    |
                   |               |    |
             +-----v-----+       +-v----+--+
             |           <-------+         |
             |  Virtual  |       |  Proxy  |
             |  Machine  |       |  Charm  |
             |           +------->         |
             +-----------+       +---------+
```

The Virtual Machine (VM) is created by the Resource Orchestrator (RO), at the
request of the Service Orchestrator (SO). Once the VM has been created, a
"proxy charm" is deployed in order to facilitate operations between the SO and
your service running within the VM.

As such, a proxy charm will expose a number of "actions" that are run via the
SO. By default, the following actions are exposed:

```bash
actions
├── reboot
├── restart
├── run
├── start
└── stop
```

Some actions, such as `run` and `reboot`, do not require any additional configuration. `start`, `stop` and `restart`, however, will require you to
implement the command(s) required to interact with your service.

## Usage

Create the framework for your proxy charm:

```bash
$ charm create pingpong
$ cd pingpong
```

Modify `layer.yaml` to the following:
```yaml
includes:
    - layer:basic
    - layer:vnfproxy
```

The `metadata.yaml` describes your service. It should look similar to the following:

```yaml
name: vnfproxy
summary: A layer for developing OSM "proxy" charms.
maintainer: Adam Israel <adam.israel@canonical.com>
description: |
  VNF "proxy" charms are a lightweight version of a charm that, rather than
  installing software on the same machine, execute commands over an ssh channel.
series:
  - trusty
  - xenial
tags:
  - osm
  - vnf
subordinate: false
```

Implement the default action(s) you wish to support by adding the following code to reactive/pingpong.py and fill in the cmd to be run:

```python
@when('actions.start')
def start():
    err = ''
    try:
        cmd = ""
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
```

Rename `README.ex` to `README.md` and describe your application and its usage.

-- fix this. there are cases where the config is useful -- Delete `config.yaml`, since the charm's configuration will be driven by the SO.

Create the `actions.yaml` file; this will describe the additional operations you would like to perform on or against your service.

```yaml
set-server:
    description: "Set the target IP address and port"
    params:
        server-ip:
            description: "IP on which the target service is listening."
            type: string
            default: ""
        server-port:
            description: "Port on which the target service is listening."
            type: integer
            default: 5555
    required:
        - server-ip
set-rate:
    description: "Set the rate of packet generation."
    params:
        rate:
            description: "Packet rate."
            type: integer
            default: 5
get-stats:
    description: "Get the stats."
get-state:
    description: "Get the admin state of the target service."
get-rate:
    description: "Get the rate set on the target service."
get-server:
    description: "Get the target server and IP set"
```


Once you've implemented your actions, you need to compile the various charm layers:
```bash
$ charm build

```

## Contact
