# banlam-input

Input methods for Taiwanese Hokkien on MacOS

... because creating a new input method is so easy now omg

## Installation

1. Clone or download this repo.
1. Install the desired input method(s):
   * Using Finder: navigate to the `dist` directory and double-click the desired input method.
   * Using command line: `open /path/to/dist/<method>.inputplugin`

MacOS has a built-in program called RegisterPluginIMApp.app that automatically recognizes files with the `.inputplugin` extension.

## Sources and Further Reading

### Data source

[moedict-data-twblg](https://github.com/g0v/moedict-data-twblg),
which was created from the Ministry of Education's website under terms of fair use.

### Creating custom input tables for MacOS:

See the official documentation for instructions and a reference file.
https://support.apple.com/guide/mac-help/create-and-use-your-own-input-source-on-mac-mchlp2866/mac

### Related work

* A project called [cin-tables](https://github.com/chinese-opendesktop/cin-tables/tree/fa1aa935199debbb394035def39b0d659d1fe7c0) includes a `.cin` file for POJ Holo input, based on *A Dictionary of the Amoy Vernacular Spoken Throughout the Prefectures of Chin-Chiu, Chiang-Chiu and Formosa* (1913) by William Campbell.
* The Ministry of Education has an input system for Tailo that has a lot more features ans supports Windows and Linux in addition to MacOS. The software was developed by a private company and appears to be quite old (like a decade). As of now, the download link is embedded in [a pdf file linked on the page](https://twblg.dict.edu.tw/holodict_new/download.jsp).
