
# Node Status Item

## Structure

`NodeStatusItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`Metadata`](../../doc/models/metadata.md) | Optional | - |
| `spec` | [`ServiceLaunchClusterAdditionalParams`](../../doc/models/service-launch-cluster-additional-params.md) | Optional | - |
| `status` | [`NodeStatus`](../../doc/models/node-status.md) | Optional | - |

## Example (as JSON)

```json
{
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
    "additionalProperties": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "status": {
    "state": "state4",
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
      "machineID": "machineID4",
      "systemUUID": "systemUUID4",
      "bootID": "bootID4",
      "kernelVersion": "kernelVersion8",
      "osImage": "osImage6"
    },
    "capacity": {
      "cpuCount": 78,
      "ephemeralStorageKB": 90,
      "memoryKB": 180
    },
    "allocatable": {
      "cpuCount": 102,
      "ephemeralStorageKB": 66,
      "memoryKB": 204
    }
  }
}
```

