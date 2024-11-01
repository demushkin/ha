"""Tuya based touch switch."""
from zigpy.profiles import zgp, zha
from zigpy.zcl.clusters.general import Basic, GreenPowerProxy, Groups, Ota, Scenes, Time

from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)
from zhaquirks.tuya import NoManufacturerCluster, TuyaDimmerSwitch
from zhaquirks.tuya.mcu import (
    TuyaInWallLevelControl,
    TuyaLevelControlManufCluster,
    TuyaOnOff,
    TuyaOnOffNM,
)


class TuyaInWallLevelControlNM(NoManufacturerCluster, TuyaInWallLevelControl):
    """Tuya Level cluster for inwall dimmable device with NoManufacturerID."""


# --- DEVICE SUMMARY ---
# - Dimmer with Green Power Proxy: Endpoint=242 profile=41440 device_type=0x0061, output_clusters: 0x0021 -
# TuyaLerlinkFanSwitch: 0x00, 0x04, 0x05, 0xEF00; 0x000A, 0x0019


class TuyaLerlinkFanSwitch(TuyaDimmerSwitch):
    """Tuya touch switch device."""

    signature = {
        MODELS_INFO: [
            ("_TZE200_r32ctezx", "TS0601"),
        ],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=0x0100
            # device_version=1
            # input_clusters=[0, 4, 5, 61184]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.SMART_PLUG,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaLevelControlManufCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=242 profile=41440 device_type=97
            # input_clusters=[]
            # output_clusters=[33]
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    TuyaLevelControlManufCluster,
                    TuyaOnOffNM,
                    TuyaInWallLevelControlNM,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            242: {
                PROFILE_ID: zgp.PROFILE_ID,
                DEVICE_TYPE: zgp.DeviceType.PROXY_BASIC,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        }
    }

