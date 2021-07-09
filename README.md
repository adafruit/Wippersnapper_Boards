# Wippersnapper_Boards
Hardware definition models for Adafruit.io WipperSnapper.

# Introduction
This repository contains Adafruit and user-submitted description models of hardware for use with Adafruit.io WipperSnapper. These hardware description models are "pared-down" digital twins, virtual representations of physical development boards.

# Repository Contents
`description`: Contains hardware description models.
`boards.json`: Index of hardware within `descriptions/` containing hardware USB vendor ID (vid) and product ID (pid).

# Hardware description model
The hardware description model describes the contents (hardware information, properties, physical components) of a development board.

## Information
Information related to the hardware including the hardware's name, description and unique identifiers.

| Property    | Required | Data Type | description                                             |
|-------------|----------|-----------|---------------------------------------------------------|
| boardName   | Yes      | String    | Hardware name                                           |
| mcuName     | Yes      | String    | Microcontroller name                                    |
| mcuRefVoltage     | Yes      | Float    | Microcontroller's maximum voltage reference, in Volts.                                    |
| VID         | Yes      | int16     | USB Vendor ID                                           |
| PID         | Yes      | int16     | USB Product ID                                          |
| displayName | Yes      | String    | Adafruit IO Device name                                 |
| description  | Yes      | String    | Device description                                       |
| productPageURL | Yes      | String      | Link to board's homepage. |
| documentationURL | Yes      | String      | Link to board's documentation. |


### boardName Naming Scheme
A `boardName` MAY ONLY contain lower case ASCII letters, numbers, and the dash character (“-”).


## Components

Hardware components are digital pins, ADC pins, sensors, servos, or motors. These components are defined within the `components` array. 

\
Each hardware component is defined by adding the following to the `.json` description file:

| Property       | Required | Data Type | description                                                                            |
|----------------|----------|-----------|----------------------------------------------------------------------------------------|
| name           | yes      | string    | Component type. Components connected to hardware externally are prefixed by `external_`|
| displayName    | yes       | string    | Human-readable display name for Adafruit IO                                            |
| dataType       | yes      | string    | Expected data type from component                                                      |
| max_resolution | no       | int16     | Max resolution of an analog component, in bits                                         |


The following properties are set by the WipperSnapper web application. **You do not need to define these values**:

| Property       | Required | Data Type | description                                                                            |
|----------------|----------|-----------|----------------------------------------------------------------------------------------|
| mode  | no       | int16     | Component mode. See `mode` for type descriptions.                              |
| direction      | no       | bool      | Defines the direction of a component, either input (`0`) or output (`1`).              |
| pull           | no       | bool      | Defines the pull direction of a component, either up (`0`) or down (`1`).              |
| period         | no       | float     | Number of milliseconds between measurements.   |


### `period` Measurement Period

Number of seconds between measurements as a float. A period of `0` indicates the pin's value with be continuously polled for a state change. A period of `-1` stops all measurements.


### `mode` Component mode

Defines the component's mode. Currently can either be analog (`1`), or digital (`2`).
* [Associated protocol buffer message](https://github.com/adafruit/Wippersnapper_Protobuf/blob/master/proto/pin/v1/pin.proto#L28)


### Sensor Components

## I2C Sensors

Development boards may have I2C sensors connected to the I2C bus. The WipperSnapper hardware specification uses a list, `i2cSensors`, to define the information and capabilities of a sensor.

An example `i2cSensors` list describing hardware with an [AHT20 Temperature and Humidity sensor](https://www.adafruit.com/product/4566) connected to the i2c bus is below:

```
{
   "i2cSensors":[
      {
         "name":"AHT20",
         "displayName":"AHT20 Humidity and Temperature Sensor",
         "address":"0x38",
         "address2":null,
         "version:null,
         "sensor_id":null,
         "type":null,
         "max_value":null,
         "min_value":null,
         "resolution":null,
         "min_delay":null
      }
   ]
}
```

The individual fields are intended to be used as follows:
* `name` [REQUIRED]: The sensor name or ID, up to a maximum of twelve characters (ex. "MPL115A2")
* `displayName` [REQUIRED]: A descriptive sensor name which will be displayed on the WipperSnapper device interface.
* `address` [REQUIRED]: The i2c device's unique bus address. Must be between 0x00 and 0x7F.
* `address2` [optional]: An optional second i2c unique bus address. Must be between 0x00 and 0x7F.
* `version` [optional]: The version of the sensor HW and the driver to allow us to differentiate versions of the board or driver
* `sensor_id` [optional]: A unique sensor identifier that is used to differentiate this specific sensor instance from any others that are present on the system or in the sensor network
* `type` [optional]: The sensor type, based on [sensors_type_t in sensors.h](https://github.com/adafruit/Adafruit_Sensor/blob/master/Adafruit_Sensor.h).
* `max_value` [optional]: The maximum value that this sensor can return (in the appropriate SI unit)
* `min_value` [optional]: The minimum value that this sensor can return (in the appropriate SI unit)
* `resolution` [optional]: The smallest difference between two values that this sensor can report (in the appropriate SI unit)
* `min_delay` [optional]: The minimum delay in microseconds between two sensor events, or '0' if there is no constant sensor rate


# Examples

Example hardware descriptions can be found in the `descriptions/` directory.

# Limitations
* WipperSnapper currently only supports WiFi connectivity

# Contributing
If you do not see the board you want to use with WipperSnapper, adding support for a board is simple and we welcome all contributions:
* Fork this repository and checkout a new branch.
* Make a new directory in `descriptions/YOUR_BOARD_NAME`
* Add your hardware description, `YOUR_BOARD_NAME.json`, to `descriptions/YOUR_BOARD_NAME`.
* Add a new board to `index.json`. 
  * The `board` key value should match the name of the directory and description file you created.
  * This file is sorted by Vendor ID (VID) first.
    * If you are contributing hardware not designed by Adafruit - you will need to create a new Array and append an object containing the Product ID (`PID`) and `board`.
* Create a pull request on this repository
