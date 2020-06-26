# BlinkaConnect_Boards
Hardware specification and boards for BlinkaConnect.

This repository, its contents, and the BlinkaConnect hardware specification is a ***work in progress and subject to change***.

# Introduction
This README.md specifies the hardware description model for internet-of-things hardware compatible with BlinkaConnect. 

# Hardware Information
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
| period    | no       | int32     | Stores the number of milliseconds between measurements as a signed 32-bit integer |

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

Notes:
* Setting the `frequency` property to `-1` stops measurements and setting this property to `0` indicates 

# Example
TODO!

# Limitations
BlinkaConnect currently only supports WiFi, Cellular and Ethernet connectivity.

# Contributing
If you do not see the board you're using with BlinkaConnect

To add support for new hardware:
* Fork this repository and checkout a new branch.
* Make a new directory in `boards/YOUR_BOARD_NAME`
* Add your hardware description, `YOUR_BOARD_NAME.json`, to `boards/YOUR_BOARD_NAME`.
* Create a pull request on this repository
