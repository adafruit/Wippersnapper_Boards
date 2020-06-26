# BlinkaConnect_Boards
Hardware descriptions for Adafruit IO Devices. 

This repository and its contents and specification is a ***work in progress and subject to change***.

# Introduction
TODO!

# Hardware Information
| Property    | Required | Data Type | Description             |
|-------------|----------|-----------|-------------------------|
| boardName   | Yes      | String    | Hardware name           |
| mcuName     | Yes      | String    | Microcontroller name    |
| VID         | Yes      | int16     | USB Vendor ID           |
| PID         | Yes      | int16     | USB Product ID          |
| displayName | Yes      | String    | Adafruit IO Device name |

TODO: Transport information needs to be added to the specification.

# Hardware Components

Hardware components are digital pins, ADC pins, sensors or outputs. These components are defined within a `components` array. Each component uses the following structure:

| Name         | Required | Data Type | Description                                                                       |
|--------------|----------|-----------|-----------------------------------------------------------------------------------|
| propertyName | yes      | String    | Property type                                                                     |
| displayName  | no       | String    | Human-readable display name for Adafruit IO                                       |
| name         | yes      | String    | Internal pin name                                                                 |
| type         | yes      | String    | Expected data type from component                                                 |
| unit         | no       | String    | Standardized SI unit                                                              |
| value        | no       | String    | Stores the sensor's value or state                                                |
| frequency    | no       | int32     | Stores the number of milliseconds between measurements as a signed 32-bit integer |


# Example

# Limitations
BlinkaConnect currently only supports WiFi, Cellular and Ethernet connectivity.

# Contributing
If you do not see the board you're using with BlinkaConnect

To add support for new hardware:
* Fork this repository and checkout a new branch.
* Make a new directory in `boards/YOUR_BOARD_NAME`
* Add your hardware description, `YOUR_BOARD_NAME.json`, to `boards/YOUR_BOARD_NAME`.
* Create a pull request on this repository
