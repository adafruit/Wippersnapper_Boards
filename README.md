# WipperSnapper Boards - Hardware Description Models for Adafruit IO WipperSnapper

This repository contains Adafruit and user-submitted description models of hardware for use with Adafruit.io.

These hardware description models (HDMs) are similar in concept to IoT "digital twins", virtual representations of physical development boards. They contain everything Adafruit.io needs to know about the device connecting to it.

# Contributing
If you do not see the board you want to use with Adafruit IO on this repository, [follow this how-to guide on the Adafruit Learning System for full instructions about adding a board to this repository](https://learn.adafruit.com/how-to-add-a-new-board-to-wippersnapper).

https://learn.adafruit.com/how-to-add-a-new-board-to-wippersnapper/overview

# What is a hardware description model?
A hardware description model (HDM) describes the contents (information, properties, physical components) of a development board.

## Information
Information related to the hardware including the hardware's name, description and unique identifiers.

| Property    | Required | Data Type | description                                             |
|-------------|----------|-----------|---------------------------------------------------------|
| boardName   | Yes      | String    | Hardware name                                           |
| mcuName     | Yes      | String    | Microcontroller name                                    |
| mcuRefVoltage     | Yes      | Float    | Microcontroller's maximum voltage reference, in Volts.                                    |
| displayName | Yes      | String    | Adafruit IO Device name                                 |
| description  | No      | String    | Device description                                       |
| productURL | Yes      | String      | Link to board's homepage. |
| documentationURL | Yes      | String      | Link to board's documentation. |
| minVersion | No       | String      | Minimum WipperSnapper firmware version that supports this board (e.g. `1.0.0-beta.37`). |
| maxVersion | No       | String      | Maximum WipperSnapper firmware version that supports this board. |


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

# Automatic Configuration File - magic.json

`magic.json` is an Adafruit IO export of a board's built-in component configuration (for example onboard buttons, LEDs, displays, and sensors). It is validated by `/boards/magic_schema.json` in this repository.

For new or updated boards, **prefer configuring built-in components in Adafruit IO first, then exporting the generated `magic.json`**, instead of hand-authoring this file. This avoids schema drift and keeps component settings aligned with what Adafruit IO actually supports.

## magic.json schema summary

Top-level required fields:

| Property | Type | Description |
|----------|------|-------------|
| `exportVersion` | string | Version of the export format. |
| `exportedBy` | string | Exporting vendor. Must be `"Adafruit"`. |
| `exportedAt` | string | Timestamp when the file was exported (typically an ISO 8601 UTC timestamp from Adafruit IO, e.g. `2023-11-13T19:41:29.465Z`). |
| `exportedFromDevice` | object | Source board metadata for the export. |
| `components` | array | Exhaustive list of built-in components and their settings. |

`exportedFromDevice` requires:

| Property | Type | Description |
|----------|------|-------------|
| `board` | string | Board name the export came from. |
| `firmwareVersion` | string | WipperSnapper firmware version at export time. |

Each entry in `components` must include:

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Human-readable component name. |
| `type` | string | WipperSnapper component type identifier (for example `push_button`, `dimmable_led`, `neopixel`, or `lc709203f:voltage`). |

Component entries then include one specific configuration shape (for example pin, I2C, PWM, pixel, DS18X20, UART, servo, or display), as defined by the `oneOf` variants in `/boards/magic_schema.json`.

For concrete examples, see existing files such as:
- `/boards/feather-esp32s3/magic.json`
- `/boards/funhouse/magic.json`
- `/boards/pyportal-tinyusb/magic.json`

## Visualisations / UI Control Customisation

Similar to the components repos component definition schema, it is possible to specify the User Interface controls / visual options for each component by using the `visualization` property. 

This can allow icons and button labels to be better customised, as well as the choice of control type itself.

See the [Pin](https://github.com/adafruit/Wippersnapper_Components#pin-visualization-types) & [PWM](https://github.com/adafruit/Wippersnapper_Components#pwm-visualization-types) visualization types in the readme, or [the examples](https://github.com/search?q=repo%3Aadafruit%2FWippersnapper_Components%20visualization&type=code), in the components repo.

It is best to configure the component via the settings cog in the IO website, before exporting that configuration, rather than manually define the appropriate fields + values.
