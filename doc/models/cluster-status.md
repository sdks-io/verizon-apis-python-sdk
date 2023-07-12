
# Cluster Status

## Structure

`ClusterStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `conditions` | [`List of ConditionItem`](../../doc/models/condition-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `token` | `string` | Optional | - |
| `published_blueprint` | `string` | Optional | - |
| `nodes` | [`List of NodeStatusItem`](../../doc/models/node-status-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `system_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `custom_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `auxiliary_task_count` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `projects` | [`List of StatusProjectItem`](../../doc/models/status-project-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `extra` | [`ClusterStatusExtra`](../../doc/models/cluster-status-extra.md) | Optional | - |

## Example (as JSON)

```json
{
  "conditions": [
    {
      "type": "type9",
      "status": "status7",
      "lastUpdated": "lastUpdated1",
      "reason": "reason3"
    },
    {
      "type": "type8",
      "status": "status6",
      "lastUpdated": "lastUpdated2",
      "reason": "reason2"
    },
    {
      "type": "type7",
      "status": "status5",
      "lastUpdated": "lastUpdated3",
      "reason": "reason1"
    }
  ],
  "token": "token6",
  "publishedBlueprint": "publishedBlueprint2",
  "nodes": [
    {
      "metadata": {
        "name": "name2",
        "displayName": "displayName0",
        "createdAt": "createdAt6",
        "modifiedAt": "modifiedAt4",
        "labels": {
          "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name0",
          "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id0",
          "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name8",
          "beta.kubernetes.io/arch": "beta.kubernetes.io/arch2",
          "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type2"
        }
      },
      "spec": {
        "additionalProperties": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "status": {
        "state": "state0",
        "conditions": [
          {
            "type": "type3",
            "status": "status1",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason7"
          }
        ],
        "nodeInfo": {
          "machineID": "machineID6",
          "systemUUID": "systemUUID6",
          "bootID": "bootID2",
          "kernelVersion": "kernelVersion6",
          "osImage": "osImage4"
        },
        "capacity": {
          "cpuCount": 40,
          "ephemeralStorageKB": 128,
          "memoryKB": 142
        },
        "allocatable": {
          "cpuCount": 8,
          "ephemeralStorageKB": 160,
          "memoryKB": 110
        }
      }
    },
    {
      "metadata": {
        "name": "name1",
        "displayName": "displayName1",
        "createdAt": "createdAt5",
        "modifiedAt": "modifiedAt5",
        "labels": {
          "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name9",
          "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id1",
          "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name7",
          "beta.kubernetes.io/arch": "beta.kubernetes.io/arch1",
          "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type1"
        }
      },
      "spec": {
        "additionalProperties": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "status": {
        "state": "state1",
        "conditions": [
          {
            "type": "type2",
            "status": "status0",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason6"
          },
          {
            "type": "type1",
            "status": "status9",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason5"
          }
        ],
        "nodeInfo": {
          "machineID": "machineID7",
          "systemUUID": "systemUUID7",
          "bootID": "bootID1",
          "kernelVersion": "kernelVersion5",
          "osImage": "osImage3"
        },
        "capacity": {
          "cpuCount": 41,
          "ephemeralStorageKB": 127,
          "memoryKB": 143
        },
        "allocatable": {
          "cpuCount": 7,
          "ephemeralStorageKB": 161,
          "memoryKB": 109
        }
      }
    },
    {
      "metadata": {
        "name": "name0",
        "displayName": "displayName2",
        "createdAt": "createdAt4",
        "modifiedAt": "modifiedAt6",
        "labels": {
          "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name8",
          "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id2",
          "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name6",
          "beta.kubernetes.io/arch": "beta.kubernetes.io/arch0",
          "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type0"
        }
      },
      "spec": {
        "additionalProperties": {
          "key1": "val1",
          "key2": "val2"
        }
      },
      "status": {
        "state": "state2",
        "conditions": [
          {
            "type": "type1",
            "status": "status9",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason5"
          },
          {
            "type": "type0",
            "status": "status8",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason4"
          },
          {
            "type": "type9",
            "status": "status7",
            "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
            "lastTransitionTime": "2016-03-13T12:52:32.123Z",
            "reason": "reason3"
          }
        ],
        "nodeInfo": {
          "machineID": "machineID8",
          "systemUUID": "systemUUID8",
          "bootID": "bootID0",
          "kernelVersion": "kernelVersion4",
          "osImage": "osImage2"
        },
        "capacity": {
          "cpuCount": 42,
          "ephemeralStorageKB": 126,
          "memoryKB": 144
        },
        "allocatable": {
          "cpuCount": 6,
          "ephemeralStorageKB": 162,
          "memoryKB": 108
        }
      }
    }
  ],
  "systemTaskCount": 18
}
```

