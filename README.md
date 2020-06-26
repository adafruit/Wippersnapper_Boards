# BlinkaConnect_Boards
Hardware descriptions for Adafruit IO Devices. 

This repository and its contents and specification is a ***work in progress and subject to change***.

# Introduction
TODO!

# Hardware Information
| Property    | Required | Data Type | Description             |   |
|-------------|----------|-----------|-------------------------|---|
| boardName   | Yes      | String    | Hardware name           |   |
| mcuName     | Yes      | String    | Microcontroller name    |   |
| VID         | Yes      | int16     | USB Vendor ID           |   |
| PID         | Yes      | int16     | USB Product ID          |   |
| displayName | Yes      | String    | Adafruit IO Device name |   |

# Board sensors and pin

# Limitations
BlinkaConnect currently only supports WiFi, Cellular and Ethernet connectivity.

# Contributing
If you do not see the board you're using with BlinkaConnect

To add support for new hardware:
* Fork this repository and checkout a new branch.
* Make a new directory in `boards/YOUR_BOARD_NAME`
* Add your hardware description, `YOUR_BOARD_NAME.json`, to `boards/YOUR_BOARD_NAME`.
* Create a pull request on this repository
