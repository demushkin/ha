const exposes = require('zigbee-herdsman-converters/lib/exposes');
const tuya = require('zigbee-herdsman-converters/lib/tuya');
const e = exposes.presets;
const ea = exposes.access;

const definition = {
    fingerprint: tuya.fingerprint('TS0601', ['_TZE204_uxllnywp']),
    model: 'RTC ZCZ03Z',
    vendor: 'TuYa',
    description: 'Human presence sensor 24Gv2 with presence patch',
    icon: 'https://www.zigbee2mqtt.io/images/devices/RT_ZCZ03Z.png',
    fromZigbee: [tuya.fz.datapoints],
    toZigbee: [tuya.tz.datapoints],
    exposes: [
        e.illuminance_lux(),
        e.presence(),
        e
            .numeric('detection_distance_max', ea.STATE_SET)
            .withValueMin(0)
            .withValueMax(840)
            .withValueStep(1)
            .withDescription('Max detection distance')
            .withUnit('cm'),
        e
            .numeric('detection_distance_min', ea.STATE_SET)
            .withValueMin(0)
            .withValueMax(840)
            .withValueStep(1)
            .withDescription('Min detection distance')
            .withUnit('cm'),
        e.numeric('target_distance', ea.STATE).withDescription('Distance to target').withUnit('cm'),
        e.numeric('fading_time', ea.STATE_SET).withValueMin(1).withValueMax(59).withValueStep(1).withDescription('Delay time').withUnit('s'),
        e.numeric('presence_sensitivity', ea.STATE_SET).withValueMin(1).withValueMax(10).withValueStep(1).withDescription('Presence sensitivity'),
        e.binary('indicator', ea.STATE_SET, 'ON', 'OFF').withDescription('LED Indicator'),
    ],
    meta: {
        tuyaDatapoints: [
            [1, 'presence', tuya.valueConverterBasic.trueFalse(4)],
            [101, 'target_distance', tuya.valueConverter.raw],
            [102, 'illuminance_lux', tuya.valueConverter.raw],
            [103, 'fading_time', tuya.valueConverter.raw],
            [104, 'indicator', tuya.valueConverter.onOff],
            [107, 'detection_distance_max', tuya.valueConverter.raw],
            [108, 'detection_distance_min', tuya.valueConverter.raw],
            [111, 'presence_sensitivity', tuya.valueConverter.raw],
        ],
    },
};

module.exports = definition;
