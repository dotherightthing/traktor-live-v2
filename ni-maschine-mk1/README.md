# NI Maschine Mk1: Ableton Resampler

Repurposing the MIDI mode of this old controller as a dedicated control surface for custom M4L Devices and Traktor DJing.

I'm also aiming to replace the functionality of the recently purchased MIDI Fighter Twisters. The Maschine Mk1 has screens which allows controls to be organised and labelled, even without the use of Python, and this is far more usable than printing overlays for controllers without screens. It's also a snap to change templates and I don't need to worry about the controller being in the wrong bank on startup as I do with the MFTs.

## M4L Devices

* <https://github.com/dotherightthing/m4l-helpers>

## Access MIDI mode

* `SHIFT + CONTROL`

## Controller Editor template

**Description:**

* Provides pages of MIDI controls
* Page and name display on controller
* Control name displays on controller (text entered into static name fields in template)
* Control values display as slider positions
* Unneeded controls can be visually disabled

**Files:**

* Ableton 11 template available from <https://support.native-instruments.com/hc/en-us/articles/4413367278097-How-to-Install-MASCHINE-Templates-for-Ableton-Live> - but this won't open in the Controller Editor for Maschine Mk1. There is an update available for the software but I'm afraid that this might negatively impact support for Maschine Mk1, so I haven't installed it yet
* Custom template - `ni-maschine-mk1/ni-controller-editor/Ableton_Resampler.ncm`

**Installation:**

1. Install Native Access
2. Install Controller Editor
3. File > Open Template

## User Remote Scripts

**Description:**

* Similar to MIDI Remote Scripts but less powerful as the only options are what's exposed in the text config file
* Works in conjunction with Controller Editor to split mappings across hardware navigable 'pages'

**Files:**

* `ni-maschine-mk1/user-remote-scripts/UserConfiguration.txt` (copied to the correct location by `npm run install`)

Note that in M4L Devices, device encoders 1-8, 9-13 etc are controlled in the `live.banks` object.

**Additional MIDI mapping:**

The following mappings are done directly in the Live template, but could be replaced by e.g. ClyphX Pro:

* 4 track XFade assign (button): `CC 50-53 / Channel 1`
* 4 track VU: Envelope L (encoder): `CC 14-17 / Channel 1`
* 4 track Pan (encoder): `CC 22-25 / Channel 1`

## MIDI Remote Scripts (TODO)

**Description:**

* Similar to User Remote Scripts but more powerful as they use Python scripting and can access the LOM, e.g. `show_messsage` which updates Live's status bar
* Adds usability to the static labels in the template by exposing the name of the selected device
* Some manufacturers' scripts may also be able to expose the parameter names - see Issue #1

**Files:**

* Maschine Mk1: <https://github.com/nuno-andre/maschine-mk1>

**Installation:**

1. Copy to `/Applications/Ableton\ Live\ 11\ Standard.app/Contents/App-Resources/MIDI\ Remote\ Scripts`

### Decompiling compiled Python scripts (`.pyc` files)

1. Install <https://pypi.org/project/uncompyle6/>
2. change to target directory
3. `find . -name '*.pyc' -exec bash -c 'uncompyle6 $1 > $1.py' _ {}\;`

## Ableton Live preferences

### MIDI

* Control Surface: `Name_of_User_or_MIDI_Remote_Script`
* Input: Maschine Controller Virtual Input
* Output: Maschine Controller Virtual Output

### MIDI Ports

* In: `Name_of_User_or_MIDI_Remote_Script Input`, Track: On, Remote: On
* Out: `Name_of_User_or_MIDI_Remote_Script Output`, Remote: On
