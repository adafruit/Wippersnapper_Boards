---
name: add-board
description: >
  Adds a new WipperSnapper board definition to this repository.
---

## Perform research on the board (Mandatory before moving to the next steps)

Do not skip this step - it is crucial to perform research on the board you want to add to find the necessary information to create a hardware description model.

For adding a board with an ESP32 MCU, check the [arduino-esp32 repository's /variants/ folder](https://github.com/espressif/arduino-esp32/tree/master/variants) for the board's name and microcontroller information.
  * Each variant folder contains a `pins_arduino.h` file that lists the board's pins and their functions. This file is crucial for understanding the board's hardware capabilities and how to define its components in the hardware description model.

For adding a board with a RP2040 or RP2350 MCU, check the [arduino-pico repository's /variants/ folder](https://github.com/earlephilhower/arduino-pico/tree/master/variants) for the board's name and microcontroller information.
  * Each variant folder contains a `pins_arduino.h` file that lists the board's pins and their functions. This file is crucial for understanding the board's hardware capabilities and how to define its components in the hardware description model.

For adding a Single-Board-Computer such as a Raspberry Pi, we use the Adafruit Blinka project. Check the [Adafruit Blinka repository's src/board/ folder](https://github.com/adafruit/Adafruit_Blinka/tree/main/src/adafruit_blinka/board) for the board's name and microcontroller information.
  * Each folder within the `board` directory contains a Python file that lists the board's pins and their functions. This file is crucial for understanding the board's hardware capabilities and how to define its components in the hardware description model.

For adding a board which is not covered by the above cases, challenges may arise in finding the necessary information to create a hardware description model. In such cases, it is recommended to prompt the user to provide the necessary information.

## Read the [README.md]

Read this repository's [README.md] file to understand the structure of hardware description models and the necessary information required to create one. This will provide a clear understanding of how to define the board's properties and components in the hardware description model.

## Create a skeleton hardware description model

### Create a new folder
Create a new folder within the `boards` directory of this repository, named after the board you want to add. The folder name should follow the naming scheme outlined in the [README.md] file (Naming Scheme, boardName).

### Create a new JSON file
Within the newly created folder, create a new JSON file named `description.json`. This file will contain the hardware description model for the board you are adding.

## Define the hardware description model
Using the information gathered from your research and the structure outlined in the [README.md] file, define the hardware description model for the board in the `description.json` file. This includes filling in the required properties such as `boardName`, `mcuName`, `mcuRefVoltage`, `displayName`, `description`, `productURL`, and `documentationURL`. Additionally, define the components of the board in the `components` array, specifying their properties such as `name`, `displayName`, `dataType`, and `max_resolution` if applicable.

## If you are stuck, prompt the user for the necessary information
If you encounter any difficulties or have questions while creating the hardware description model, do not hesitate to prompt the user for the necessary information. This may include asking for specific details about the board's hardware capabilities, vendor name, URLs, pin configurations, or any other relevant information that is required to accurately define the hardware description model.

## Perform validation checks
After defining the hardware description model, validate the `definition.json` file against `boards/schema.json` to ensure that it adheres to the required structure and contains all necessary properties. This will help identify any errors or missing information in the hardware description model before it is added to the repository.