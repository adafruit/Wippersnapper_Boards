# BlinkaConnect_Boards
Hardware specification and boards for BlinkaConnect.

This repository, its contents, and the BlinkaConnect hardware specification is a ***work in progress and subject to change***.

# Introduction
This README.md specifies the hardware description model for internet-of-things hardware compatible with BlinkaConnect. 

# Hardware Description

TODO! Describe this information

| Property    | Required | Data Type | Description             |
|-------------|----------|-----------|-------------------------|
| boardName   | Yes      | String    | Hardware name           |
| mcuName     | Yes      | String    | Microcontroller name    |
| VID         | Yes      | int16     | USB Vendor ID           |
| PID         | Yes      | int16     | USB Product ID          |
| displayName | Yes      | String    | Adafruit IO Device name |



# Hardware Components

Hardware components are digital pins, ADC pins, sensors or outputs. These components are defined within the `components` array. 

Each component uses the following structure:

| Property         | Required | Data Type | Description                                                                       |
|--------------|----------|-----------|-----------------------------------------------------------------------------------|
| propertyName | yes      | String    | Property type                                                                     |
| displayName  | no       | String    | Human-readable display name for Adafruit IO                                       |
| name         | yes      | String    | Internal pin name                                                                 |
| type         | yes      | String    | Expected data type from component                                                 |
| unit         | no       | String    | Standardized SI unit                                                              |
| value        | no       | String    | Stores the sensor's value or state                                                |
| period    | no       | int32     | Number of milliseconds between measurements |

### Properties and Units
The component's `propertyName`, `type`, and `unit` describe component's the data type and SI unit. The table below mirrors the [Sensor Properties and Units defined in the CircuitPython API documentation.](https://circuitpython.readthedocs.io/en/latest/docs/design_guide.html#sensor-properties-and-units).

| Property name         | Python type           | Units                                                                   |
| --------------------- | --------------------- | ----------------------------------------------------------------------- |
| ``acceleration``      | (float, float, float) | x, y, z meter per second per second                                     |
| ``magnetic``          | (float, float, float) | x, y, z micro-Tesla (uT)                                                |
| ``orientation``       | (float, float, float) | x, y, z degrees                                                         |
| ``gyro``              | (float, float, float) | x, y, z radians per second                                              |
| ``temperature``       | float                 | degrees centigrade                                                      |
| ``eCO2``              | float                 | equivalent CO2 in ppm                                                   |
| ``TVOC``              | float                 | Total Volatile Organic Compounds in ppb                                 |
| ``distance``          | float                 | centimeters                                                             |
| ``light``             | float                 | non-unit-specific light levels (should be monotonic but is not lux)     |
| ``lux``               | float                 | SI lux                                                                  |
| ``pressure``          | float                 | hectopascal (hPa)                                                       |
| ``relative_humidity`` | float                 | percent                                                                 |
| ``current``           | float                 | milliamps (mA)                                                          |
| ``voltage``           | float                 | volts (V)                                                               |
| ``color``             | int                   | RGB, eight bits per channel (0xff0000 is red)                           |
| ``alarm``             | (time.struct, str)    | Sample alarm time and string to characterize frequency such as "hourly" |
| ``datetime``          | time.struct           | date and time                                                           |
| ``duty_cycle``        | int                   | 16-bit PWM duty cycle (regardless of output resolution)                 |
| ``frequency``         | int                   | Hertz                                                                   |
| ``value``             | bool                  | Digital logic                                                           |
| ``value``             | int                   | 16-bit Analog value, unit-less                                          |
| ``weight``            | float                 | grams (g)                                                               |

### Measurement Period

Stores the number of milliseconds between measurements as a signed 32-bit int. -1 stops a measurement and 0 indicates as fast as possible. Both readable and writable.

# Example Hardware Description

The following hardware description shows an [Adafruit PyPortal](https://www.adafruit.com/product/4116). 

```
{
    "boardName": "PyPortal",
    "mcuName": "samd51j20",
    "VID": "0x239A",
    "PID": "0x8036",
    "displayName": "",
    "components": [
        {
            "propertyName": "value",
            "displayName": "A1",
            "name": "A1",
            "type": "int16",
            "unit": "",
            "value": "",
            "period": "-1"
        },
        {
            "propertyName": "value",
            "displayName": "A4",
            "name": "A4",
            "type": "int16",
            "unit": "",
            "value": "",
            "period": "-1"
        },
        {
            "propertyName": "value",
            "displayName": "D3",
            "name": "D3",
            "type": "bool",
            "unit": "",
            "value": "",
            "period": "-1"
        },
        {
            "propertyName": "value",
            "displayName": "D4",
            "name": "D4",
            "type": "bool",
            "unit": "",
            "value": "",
            "period": "-1"
        },
        {
            "propertyName": "light",
            "displayName": "Light sensor",
            "name": "A2",
            "type": "float",
            "unit": "light level",
            "value": "",
            "period": "-1"
        },
        {
            "propertyName": "pixel",
            "displayName": "NeoPixel",
            "name": "NEOPIXEL",
            "type": "0",
            "value": ""
        },
        {
            "propertyName": "value",
            "displayName": "Built-in LED",
            "name": "D13",
            "type": "bool",
            "unit": "",
            "value": ""
        }
    ]
}
```

# Limitations
* BlinkaConnect currently only supports WiFi, Cellular and Ethernet connectivity.

# Contributing
If you do not see the board you're using with BlinkaConnect

To add support for new hardware:
* Fork this repository and checkout a new branch.
* Make a new directory in `boards/YOUR_BOARD_NAME`
* Add your hardware description, `YOUR_BOARD_NAME.json`, to `boards/YOUR_BOARD_NAME`.
* Create a pull request on this repository
