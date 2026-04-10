---
name: add-board
description: "Use this agent to add a new board to the WipperSnapper repository. This involves researching the board's specifications, creating a hardware description model in JSON format, and ensuring it adheres to the required structure outlined in the README.md file. The agent will guide you through the necessary steps, including gathering information about the board's properties and components, and validating the final hardware description model against the provided schema."
argument-hint: "Provide the name of the board you want to add (e.g., 'esp32-c3-devkitm-1')."
---

## Perform research on the board (Mandatory before moving to the next steps)

Do not skip this step - it is crucial to perform research on the board you want to add to find the necessary information to create a hardware description model.

For adding a board with an ESP32 MCU, check the [arduino-esp32 repository's /variants/ folder](https://github.com/espressif/arduino-esp32/tree/master/variants) for the board's name and microcontroller information.
  * Each variant folder contains a `pins_arduino.h` file that lists the board's pins and their functions. This file is crucial for understanding the board's hardware capabilities and how to define its components in the hardware description model.

For adding a board with a RP2040 or RP2350 MCU, check the [arduino-pico repository's /variants/ folder](https://github.com/earlephilhower/arduino-pico/tree/master/variants) for the board's name and microcontroller information.
  * Each variant folder contains a `pins_arduino.h` file that lists the board's pins and their functions. This file is crucial for understanding the board's hardware capabilities and how to define its components in the hardware description model.

For adding a Single-Board-Computer such as a Raspberry Pi, we use the Adafruit Blinka project. First, navigate to the [Adafruit Blinka repository's src/board/ folder](https://github.com/adafruit/Adafruit_Blinka/tree/main/src/adafruit_blinka/board) to view a listing of the supported boards. If the board you want to add is listed, navigate its corresponding folder (and potentially into its subfolders) until you get to the corresponding Python file to access its pin definition. For example, if you want to add the Raspberry Pi 4B, navigate to `raspberrypi/` for the vendor and open the `raspi_4b.py` file within it to access the board's definitions and GPIO pin information. This information will be essential for defining the board's properties and components in the hardware description model.

For adding a board which is not covered by the above cases, challenges may arise in finding the necessary information to create a hardware description model. In such cases, it is recommended to prompt the user to provide the necessary information.

## Perform research on the board vendor
In addition to researching the board's specifications, it is also important to gather information about the board's vendor and product URLs. This information is required to fill in the `productURL`, `documentationURL`, and `vendor` properties in the hardware description model.

## Determine the installation method for the board's microcontroller
If not provided by the user, determine the installation method for the board's microcontroller, which is required to fill in the `installMethod` property within the hardware description model.

This may involve researching the board's microcontroller. If it is a single-board computer using the Adafruit Blinka project, the `installMethod` is likely to be `python`. Otherwise, if it is a microcontroller commonly used in the Arduino ecosystem, the `installMethod` is likely to be `web`. However, it is important to verify this information through research or by prompting the user to ensure accuracy in the hardware description model.

## Read the [README.md]

Read this repository's [README.md] file to understand the structure of hardware description models and the necessary information required to create one. This will provide a clear understanding of how to define the board's properties and components in the hardware description model.

## Create a skeleton hardware description model

### Create a new folder
Create a new folder within the `boards` directory of this repository, named after the board you want to add. The folder name should follow the naming scheme outlined in the [README.md] file (Naming Scheme, boardName).

### Create a new JSON file
Within the newly created folder, create a new JSON file named `description.json`. This file will contain the hardware description model for the board you are adding.

## Define the hardware description model
Using the information gathered from your research and the structure outlined in the [README.md] file, define the hardware description model for the board in the `description.json` file.


This includes filling in the required properties such as `boardName`, `mcuName`, `mcuRefVoltage`, `displayName`, `description`, `productURL`, and `documentationURL`. Additionally, define the components of the board in the `components` array, specifying their properties such as `name`, `displayName`, `dataType`, and `max_resolution` if applicable.

Do not attempt to prettify the JSON file. Focus on ensuring that all required properties are included and accurately defined based on your research.

## If you are stuck, prompt the user for the necessary information
If you encounter any difficulties or have questions while creating the hardware description model, do not hesitate to prompt the user for the necessary information. This may include asking for specific details about the board's hardware capabilities, vendor name, URLs, pin configurations, or any other relevant information that is required to accurately define the hardware description model.

## Validate the hardware description model

Run exactly this sequence of commands:

1) Before validating, install the `jsonschema` Python package. This is required because the validation script uses it to check the board definition against the JSON schema (the same schema used by CI). This is a setup step - the validation script will not work without this package installed.:

```
pip install jsonschema
```

2) To validate the .json file you just created, run exactly this command:

```
python3 scripts/validate.py boards/<board-name>/definition.json
```

Replace `<board-name>` with the name of the board folder you created. Do not modify the command or add additional flags.

