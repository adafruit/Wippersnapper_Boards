---
name: add-board
description: "Use this skill to add a new board to the WipperSnapper repository. This involves researching the board's specifications, creating a hardware description model in JSON format, and ensuring it adheres to the required structure outlined in the README.md file. The skill will guide you through the necessary steps, including gathering information about the board's properties and components, and validating the final hardware description model against the provided schema."
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
Within the newly created folder, create a new JSON file named `definition.json`. This file will contain the hardware description model for the board you are adding.

## Define the hardware description model
Using the information gathered from your research and the structure outlined in the [README.md] file, define the hardware description model for the board in the `definition.json` file.


This includes filling in the required properties such as `boardName`, `mcuName`, `mcuRefVoltage`, `displayName`, `description`, `productURL`, and `documentationURL`. Additionally, define the components of the board in the `components` array, specifying their properties such as `name`, `displayName`, `dataType`, and `max_resolution` if applicable.

Do not attempt to prettify the JSON file. Focus on ensuring that all required properties are included and accurately defined based on your research.

## If you are stuck, prompt the user for the necessary information
If you encounter any difficulties or have questions while creating the hardware description model, do not hesitate to prompt the user for the necessary information. This may include asking for specific details about the board's hardware capabilities, vendor name, URLs, pin configurations, or any other relevant information that is required to accurately define the hardware description model.

## Add an image of the board

Next, you'll need to add an image of your board.

**IMPORTANT: Do NOT generate, create, or synthesize an image. You MUST download a real image from an external source (Fritzing Library, manufacturer website, or distributor). If you cannot find or download an image, ask the user to provide one. Never use AI-generated or hand-coded SVG/images.**

First, check the vendor's name (`vendor` property in the hardware description model) to determine who the manufacturer of the board is.

If the vendor is Adafruit, you should use an image from the [Adafruit Fritzing Library](https://github.com/adafruit/Fritzing-Library). This library provides vectorized illustrations of Adafruit boards, which are preferred for consistency and quality. Individual part files are `.fzpz` files located in the [`/parts` directory](https://github.com/adafruit/Fritzing-Library/tree/master/parts). Search that directory for the board you are adding.

Once you find the corresponding `.fzpz` file, download it and place it in the board's folder in this repository.

Then, run the extraction script. It opens the `.fzpz` file (a ZIP archive), finds the breadboard SVG (`svg.breadboard.*.svg`) inside it, saves it as `image.svg` in the same directory, and deletes the original `.fzpz` file:
```
python3 .github/skills/add-board/scripts/extract_svg_fzz.py boards/<board-name>/<image-file>.fzpz
```

If the vendor is not Adafruit, you should use an image from the manufacturer's website or from a reputable distributor such as Digi-Key or Mouser. The image should be a clear representation of the board, ideally showing a top-down view. Download the image and save it as `image` with the appropriate file extension (e.g., `image.jpg`, `image.png`) in the board's folder in this repository.


## Validate the image file
Next, make sure the image adheres to the following specifications: 

* The image file's extension can be any one of: JPG, JPEG, GIF, PNG, SVG
* The image file's size must be at least 3kb and must not exceed 100kb

## Validate the hardware description model

Run exactly this sequence of commands:

1) Before validating, install the `jsonschema` Python package. This is required because the validation script uses it to check the board definition against the JSON schema (the same schema used by CI). This is a setup step - the validation script will not work without this package installed.:

```
python3 -m pip install jsonschema
```

2) To validate the .json file you just created, run exactly this command:

```
python3 .github/skills/add-board/scripts/validate.py boards/<board-name>/definition.json
```

Replace `<board-name>` with the name of the board folder you created. Do not modify the command or add additional flags.

## Create a pull request
After you have created the hardware description model, added the image, and validated the files, you can create a pull request to merge your changes into the repository.
