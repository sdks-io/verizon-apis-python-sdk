
# Cluster

## Structure

`Cluster`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_version` | `string` | Optional | - |
| `kind` | `string` | Optional | - |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |
| `spec` | [`ClusterSpec`](../../doc/models/cluster-spec.md) | Optional | - |
| `status` | [`ClusterStatus`](../../doc/models/cluster-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "apiVersion": "apiVersion4",
  "kind": "kind8",
  "metadata": {
    "name": "name6",
    "displayName": "displayName4",
    "createdAt": "createdAt0",
    "modifiedAt": "modifiedAt0",
    "labels": {
      "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name4",
      "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id4",
      "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name2",
      "beta.kubernetes.io/arch": "beta.kubernetes.io/arch6",
      "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type6"
    }
  },
  "spec": {
    "blueprintRef": "blueprintRef0",
    "overrideSelector": "overrideSelector2",
    "shareMode": "shareMode0"
  },
  "status": {
    "conditions": [
      {
        "type": "type3",
        "status": "status1",
        "lastUpdated": "lastUpdated7",
        "reason": "reason7"
      }
    ],
    "token": "token8",
    "publishedBlueprint": "publishedBlueprint6",
    "nodes": [
      {
        "metadata": {
          "name": "name4",
          "displayName": "displayName8",
          "createdAt": "createdAt8",
          "modifiedAt": "modifiedAt2",
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
            },
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
            "machineID": "machineID0",
            "systemUUID": "systemUUID0",
            "bootID": "bootID8",
            "kernelVersion": "kernelVersion2",
            "osImage": "osImage0"
          },
          "capacity": {
            "cpuCount": 56,
            "ephemeralStorageKB": 112,
            "memoryKB": 158
          },
          "allocatable": {
            "cpuCount": 248,
            "ephemeralStorageKB": 176,
            "memoryKB": 94
          }
        }
      },
      {
        "metadata": {
          "name": "name3",
          "displayName": "displayName9",
          "createdAt": "createdAt7",
          "modifiedAt": "modifiedAt3",
          "labels": {
            "alpha.rafay.io/cluster-name": "alpha.rafay.io/cluster-name9",
            "alpha.rafay.io/instance-id": "alpha.rafay.io/instance-id9",
            "alpha.rafay.io/nodegroup-name": "alpha.rafay.io/nodegroup-name9",
            "beta.kubernetes.io/arch": "beta.kubernetes.io/arch3",
            "beta.kubernetes.io/instance-type": "beta.kubernetes.io/instance-type3"
          }
        },
        "spec": {
          "additionalProperties": {
            "key1": "val1",
            "key2": "val2"
          }
        },
        "status": {
          "state": "state9",
          "conditions": [
            {
              "type": "type4",
              "status": "status2",
              "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
              "lastTransitionTime": "2016-03-13T12:52:32.123Z",
              "reason": "reason8"
            },
            {
              "type": "type3",
              "status": "status1",
              "lastHeartbeatTime": "2016-03-13T12:52:32.123Z",
              "lastTransitionTime": "2016-03-13T12:52:32.123Z",
              "reason": "reason7"
            }
          ],
          "nodeInfo": {
            "machineID": "machineID1",
            "systemUUID": "systemUUID1",
            "bootID": "bootID7",
            "kernelVersion": "kernelVersion1",
            "osImage": "osImage9"
          },
          "capacity": {
            "cpuCount": 55,
            "ephemeralStorageKB": 113,
            "memoryKB": 157
          },
          "allocatable": {
            "cpuCount": 249,
            "ephemeralStorageKB": 175,
            "memoryKB": 95
          }
        }
      }
    ],
    "systemTaskCount": 222
  }
}
```

