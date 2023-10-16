# Schema Docs

- [1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > deviceSettings`](#deviceSettings)
  - [1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > deviceModel`](#deviceSettings_deviceModel)
  - [1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > firmwareVersion`](#deviceSettings_firmwareVersion)
  - [1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > hardwareVersion`](#deviceSettings_hardwareVersion)
  - [1.4. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > uId`](#deviceSettings_uId)
  - [1.5. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > deviceName`](#deviceSettings_deviceName)
  - [1.6. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > profileId`](#deviceSettings_profileId)

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

| Property                             | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [deviceSettings](#deviceSettings ) | No      | object | No         | -          | Device Settings   |

## <a name="deviceSettings"></a>1. ![Optional](https://img.shields.io/badge/Optional-yellow) Property `root > deviceSettings`

**Title:** Device Settings

|                           |                                                                                                          |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                                 |
| **Additional properties** | [![Not allowed](https://img.shields.io/badge/Not%20allowed-red)](# "Additional Properties not allowed.") |

**Description:** Device information which can be accessed via a CHCK command. READ ONLY

| Property                                              | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| + [deviceModel](#deviceSettings_deviceModel )         | No      | enum (of string) | No         | -          | Device Model      |
| + [firmwareVersion](#deviceSettings_firmwareVersion ) | No      | string           | No         | -          | Firmware Version  |
| + [hardwareVersion](#deviceSettings_hardwareVersion ) | No      | string           | No         | -          | Hardware Version  |
| + [uId](#deviceSettings_uId )                         | No      | integer          | No         | -          | UID               |
| + [deviceName](#deviceSettings_deviceName )           | No      | string           | No         | -          | Device Name       |
| + [profileId](#deviceSettings_profileId )             | No      | integer          | No         | -          | Profile ID        |

### <a name="deviceSettings_deviceModel"></a>1.1. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > deviceModel`

**Title:** Device Model

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

Must be one of:
* "Bridge4"
* "Bridge6"

### <a name="deviceSettings_firmwareVersion"></a>1.2. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > firmwareVersion`

**Title:** Firmware Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="deviceSettings_hardwareVersion"></a>1.3. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > hardwareVersion`

**Title:** Hardware Version

|          |          |
| -------- | -------- |
| **Type** | `string` |

### <a name="deviceSettings_uId"></a>1.4. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > uId`

**Title:** UID

|          |           |
| -------- | --------- |
| **Type** | `integer` |

**Description:** 96-bit unique identifing number for each device. Can be used to identify multiple devices with the same name

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

### <a name="deviceSettings_deviceName"></a>1.5. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > deviceName`

**Title:** Device Name

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** User assignable name for the device

| Restrictions   |    |
| -------------- | -- |
| **Max length** | 16 |

### <a name="deviceSettings_profileId"></a>1.6. ![Required](https://img.shields.io/badge/Required-blue) Property `root > deviceSettings > profileId`

**Title:** Profile ID

|             |           |
| ----------- | --------- |
| **Type**    | `integer` |
| **Default** | `0`       |

**Description:** Tracks changes to the device configuration across the editor and on-board. If a different value is retrieved compared to the previous stored value, it can be assumed that configuration changes were performed externally of the editor.

| Restrictions |                 |
| ------------ | --------------- |
| **Minimum**  | &ge; 0          |
| **Maximum**  | &le; 4294967295 |

----------------------------------------------------------------------------------------------------------------------------
