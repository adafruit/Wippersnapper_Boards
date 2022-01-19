# WipperSnapper Boards - Hardware Description Models for Adafruit IO WipperSnapper Beta

This repository contains Adafruit and user-submitted description models of hardware for use with Adafruit.io WipperSnapper Beta.

These hardware description models (HDMs) are similar in concept to IoT "digital twins", virtual representations of physical development boards. They contain everything Adafruit.io WipperSnapper needs to know about the device connecting to it.

# What is a hardware description model?
A hardware description model (HDM) describes the contents (information, properties, physical components) of a development board.

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


### Naming Scheme, boardName
A `boardName` MAY ONLY contain lower case ASCII letters, numbers, and the dash character (“-”).


## Components

Components are ports such as digital pins or analog pins. These components are defined within the `components` array. 

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


### Sensor Components

## I2C Components

Hardware exposing the I2C bus may add an `i2cPorts` array to its HDM.

The following HDM snippet defines an I2C interface on port 0 with a `SDA` GPIO pin of `34` and a `SCL` GPIO pin of 33.

```
"i2cPorts": [
    {
        "i2cPortId": "0",
        "SDA": 34,
        "SCL": 33
    }
],
```


# Examples

Example hardware descriptions can be found in the `boards/` directory.

# Limitations
* WipperSnapper currently only supports hardware with WiFi connectivity.
* WipperSnapper currently supports the following microcontrollers: ESP8266, ESP32, ESP32-S2, SAMD51, SAMD21.

# Contributing
If you do not see the board you want to use with WipperSnapper, adding support for a board we already have support for (see above, _Limitations_) is simple and we welcome all contributions:
* Fork this repository and checkout a new branch.
* Make a new directory in `boards/YOUR_BOARD_NAME`
* Add the hardware description to this folder as `definition.json`
* Add an image of the hardware to this folder as `image.svg`
* Add a new board entry to `index.json`. 
  * The `board` key value should match the name of the directory and description file you created.
  * This file is sorted by Vendor ID (VID) first.
    * If you are contributing hardware not designed by Adafruit - you will need to create a new Array and append an object containing the Product ID (`PID`) and `board`.
* Create a pull request to this repository
