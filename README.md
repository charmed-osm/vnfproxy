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

Some actions, such as `run` and `reboot`, do not require any additional configuration. `start`, `stop` and `restart`, however, will require you to specify the command(s) required to interact with your service.

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

Rename `README.ex` to `README.md` and describe your application and its usage.

-- fix this. there are cases where the config is useful -- Delete `config.yaml`, since the charm's configuration will be driven by the SO.

Create the `actions.yaml` file; this will describe the operations you would like to perform on or against your service.

```yaml

```
## Contact
