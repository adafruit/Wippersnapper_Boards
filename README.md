# BlinkaConnect_Boards
Hardware specification and boards for BlinkaConnect.

This repository, its contents, and the BlinkaConnect hardware specification is a ***work in progress and subject to change***.

# Introduction
This README.md specifies the hardware definition model for internet-of-things hardware compatible with BlinkaConnect. 

# Repository Contents

`definition`: Contains hardware definition models.
`boards.json`: Index of hardware within `definitions/` containing hardware USB vendor ID (vid) and product ID (pid).

# Hardware definition

The hardware definition describes the contents (hardware information, components) of a physical piece of hardware or project.

### Information

Information related to the hardware including the hardware's name, definition and unique identifiers.

| Property    | Required | Data Type | description             |
|-------------|----------|-----------|-------------------------|
| boardName   | Yes      | String    | Hardware name           |
| mcuName     | Yes      | String    | Microcontroller name    |
| VID         | Yes      | int16     | USB Vendor ID           |
| PID         | Yes      | int16     | USB Product ID          |
| displayName | Yes      | String    | Adafruit IO Device name |
| definition | Yes      | String    | Device definition      |
| lastUpdated | Yes      | Time    | Last time the board definition was updated, in ISO-8601      |


### Components

Hardware components are digital pins, ADC pins, sensors, servos, or motors. These components are defined within the `components` array. 

Each general component uses the following structure:

| Property      | Required | Data Type | description                                                                       |
|--------------|----------|-----------|-----------------------------------------------------------------------------------|
| name         | yes      | String    | Component type. Components connected to hardware externally are prefixed by `external_`|
| displayName  | no       | String    | Human-readable display name for Adafruit IO                                            |
| property     | yes      | String    | Property type                                                                          |
| dataType     | yes      | String    | Expected data type from component                                                      |
| value        | no       | String    | Stores the sensor's value or state                                                     |
| period       | no      | int32     | Number of milliseconds between measurements. Defaults to -1, no active measurements.   |
| writable     | yes      | boolean   | Whether the component is writable. Default is True, read/write.                        |

**Sensor Components**

Sensors are special component types which are defined by attaching a component to the device in user-code. These components should append the following properties onto the component structure above:

| Property     | Required | Data Type | description                                                                       |
|--------------|----------|-----------|-----------------------------------------------------------------------------------|
| sensorID     | Yes      |   int32   | Sensor instance number. Must be unique (no two conflicting sensorIDs per definition) |
| max_val      | No       |   float   |  Maximum value of this sensor's value in SI units.                                   |
| min_val      | No       |   float   |  Minimum value of this sensor's value in SI units.                                   |



#### Properties and Units
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

#### Measurement Period

Stores the number of milliseconds between measurements as a signed 32-bit int. Defining a value of `-1` stops a measurement. This field is **zero** by default.

# Example Hardware definition

The following hardware definition shows an [Adafruit PyPortal](https://www.adafruit.com/product/4116). 

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
* Make a new directory in `definitions/YOUR_BOARD_NAME`
* Add your hardware definition, `YOUR_BOARD_NAME.json`, to `definitions/YOUR_BOARD_NAME`.
* Add a new board to `index.json`. 
  * The `board` key value should match the name of the directory and definition file you created.
  * This file is sorted by Vendor ID (VID) first.
    * If you are contributing hardware not designed by Adafruit - you will need to create a new Array and append an object containing the Product ID (`PID`) and `board`.
* Create a pull request on this repository
