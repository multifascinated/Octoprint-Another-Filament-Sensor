# OctoPrint-AnotherFilamentSensor

Forked off of (https://github.com/kontakt/Octoprint-Filament-Reloaded)

The original version that I had made my changes on top of was also a fork off of this original
repository.

Once I found a filament sensor I liked I realized that the one issue it had was that it would
trigger the filament runout command multiple times in quick succession (ie. it would re-trigger
again right after I told octoprint to resume). This is annoying so I fixed it locally at one
point. Now I aim to bring the changes to a public repo. I intend this to be its own plugin; I
doubt it will ever get merged into the original plugin.

---
maybe I can just get the original working.. it looks like a different potential fix for that
same problem is included there... we'll see...
---

[OctoPrint](http://octoprint.org/) plugin that integrates with a filament sensor hooked up to a Raspberry Pi GPIO pin and allows the filament spool to be changed during a print if the filament runs out.

Future developments are planned to include multiple filament sensors and pop-ups.

Initial work based on the [Octoprint-Filament](https://github.com/MoonshineSG/Octoprint-Filament) plugin by MoonshineSG.

## Required sensor

Using this plugin requires a filament sensor. The code is set to use the Raspberry Pi's internal Pull-Up resistors, so the switch should be between your detection pin and a ground pin.

This plugin is using the GPIO.BOARD numbering scheme, the pin being used needs to be selected by the physical pin number.

## Features

* Configurable GPIO pin.
* Debounce noisy sensors.
* Support normally open and normally closed sensors.
* Execution of custom GCODE when out of filament detected.
* Optionally pause print when out of filament.

An API is available to check the filament sensor status via a GET method to `/plugin/filamentreload/status` which returns a JSON

- `{status: "-1"}` if the sensor is not setup
- `{status: "0"}` if the sensor is OFF (filament not present)
- `{status: "1"}` if the sensor is ON (filament present)

## Installation

* Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager).
* Manually using this URL: https://github.com/kontakt/Octoprint-Filament-Reloaded/archive/master.zip

## Configuration

After installation, configure the plugin via OctoPrint Settings interface.
