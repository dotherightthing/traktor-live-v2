"""
Class: MidiFighterTwister
_________________________________________________________________________________________

TESTING:

```sh
# note: the version string will change if Live auto-updates itself
tail -f '/Users/dan/Library/Preferences/Ableton/Live 10.1.43/Log.txt'
```

```py
self.canonical_parent.log_message('Hello world')
```
_________________________________________________________________________________________

"""

# Import UserActionsBase to extend it.
from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# import datetime

# Your class must extend UserActionsBase.
class MidiFighterTwister(UserActionsBase):
	# Your class must implement this method.
	def create_actions(self):
		# called by Macros.txt
		self.add_clip_action('reset_mapped_track_controls', self.reset_mapped_track_controls)
		self.add_clip_action('slice_track_clip_into_4', self.slice_track_clip_into_4)
		self.add_clip_action('merge_sliced_track_clip_from_4', self.merge_sliced_track_clip_from_4)

	# reset mapped controls on provided track name
	def reset_mapped_track_controls(self, action_def, args):
		track_name = args.upper()
		action_list = ''
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P1 127;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P2 63;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P3 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P4 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P5 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P6 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P7 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P8 63;'
		action_list += 'WAIT 1;'
		action_list += 'MSG "Reset ' + track_name + '";'
		action_list += 'PUSH MSG "Reset ' + track_name + '"'

		self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

	# slice selected clip on provided track name into 4 parts
	# https://www.youtube.com/watch?v=rjSTTO3f4_Y
	# TODD automate switching Push2 into Note mode to see slices and do sequencing
	# TODO check Gain amt - seems hotter than sample track when flattening
	# TODO put all the slices into the sequencer automatically
	def slice_track_clip_into_4(self, action_def, args):
		track_name = args.upper()
		action_list = ''

		# delete any existing slice tracks
		action_list += '"' + track_name + ' SLICED"/DEL;'

		# create a new MIDI Track with a Simpler device containing the Audio Clip
		# as well as any other Devices that were on the Clip's Track.
		action_list += '"' + track_name + '"/CLIP(SEL) TOSIMP;'
		action_list += 'WAIT 5;'

		# name the new track
		action_list += 'SEL/NAME "' + track_name + ' SLICED";'
		action_list += 'WAIT 5;'

		# use simpler's slice mode
		action_list += 'SEL/DEV SIMP PLAYMODE SLICE;'
		action_list += 'WAIT 1;'

		# set slice mode to beat
		action_list += 'SEL/DEV SIMP SMODE BEAT;'
		action_list += 'WAIT 1;'

		# set the beat division
		action_list += 'SEL/DEV SIMP MULT 8;'

		# convert to slices to a drum rack (of simplers) so that step sequencer mode can be activated
		action_list += '"' + track_name + ' SLICED"/DEV SIMP TODR;'
		action_list += 'WAIT 5;'

		# action_list += 'SEL/DEV SIMP GAIN 108;'

		# create a midi clip that is 1 bar long
		action_list += 'ADDCLIP SEL 1;'
		action_list += 'WAIT 1;'

		# select the slice track
		action_list += 'SEL "' + track_name + ' SLICED";'
		action_list += 'WAIT 1;'

		# name the midi clip
		action_list += 'SEL/CLIP NAME "SLICED";'
		action_list += 'WAIT 1;'

		# mute the slice track
		action_list += '"' + track_name + ' SLICED"/MUTE ON;'
		action_list += 'WAIT 1;'

		# cue the slice track, to prevent sequencing from being heard in the mix
		action_list += '"' + track_name + ' SLICED"/SOLO ON;'
		action_list += 'WAIT 1;'

		# play the midi clip
		action_list += 'SEL/PLAY;'
		action_list += 'WAIT 1;'

		# disable recording on the slice track
		action_list += '"' + track_name + ' SLICED"/ARM OFF;'
		action_list += 'WAIT 1;'

		# active step sequencer mode
		action_list += 'PUSH MODE DRUM;'
		action_list += 'WAIT 1;'

		# update user
		action_list += 'MSG "Sliced ' + track_name + '";'
		action_list += 'PUSH MSG "Sliced ' + track_name + '"'

		self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)

	# merging is essentially resampling from a specific track
	# NOTE: ARM OFF doesn't work if that track is selected
	def merge_sliced_track_clip_from_4(self, action_def, args):
		track_name = args.upper()
		action_list = ''

		# select the target track
		action_list += '"' + track_name + '"/SEL;'
		action_list += 'WAIT 1;'

		# monitor the source track
		action_list += '"' + track_name + '"/IN "' + track_name + ' SLICED";'
		action_list += 'WAIT 1;'

		# disarm all tracks
		action_list += 'ALL/ARM OFF;'
		action_list += 'WAIT 1;'

		# arm the target track
		action_list += '"' + track_name + '"/ARM ON;'
		action_list += 'WAIT 1;'

		# mute the target track
		action_list += '"' + track_name + '"/MUTE ON;'
		action_list += 'WAIT 1;'
		
		# record a new clip in the last slot of the target track
		action_list += 'SRECFIX 4 LAST;'
		action_list += 'WAIT 1;'
		
		# ensure the clip has finished recording
		action_list += 'WAITS 5B;'
		action_list += 'WAIT 1;'
		
		# rearm all tracks
		action_list += '"SAMPLE 1"/ARM ON;'
		action_list += '"SAMPLE 2"/ARM ON;'
		action_list += '"SAMPLE 3"/ARM ON;'
		action_list += '"SAMPLE 4"/ARM ON;'
		action_list += '"GLOBAL RESAMPLE"/ARM ON;'
		action_list += 'WAIT 1;'

		# name the recorded clip
		action_list += '"' + track_name + '"/CLIP NAME "SLICED";'
		action_list += 'WAIT 1;'

		# color the recorded clip purple to differentiate it from clips that haven't been sliced
		action_list += '"' + track_name + '"/CLIP COLOR 10;'
		action_list += 'WAIT 1;'

		# play the recorded clip
		action_list += '"' + track_name + '"/PLAY LAST;'
		action_list += 'WAIT 1;'

		# reset the target track
		action_list += '"' + track_name + '"/DEV(1) P1 127;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P2 63;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P3 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P4 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P5 107;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P6 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P7 0;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/DEV(1) P8 63;'
		action_list += 'WAIT 1;'
		action_list += '"' + track_name + '"/IN "DECK A";'
		action_list += 'WAIT 1;'

		# unmute the target track
		action_list += '"' + track_name + '"/MUTE OFF;'
		action_list += 'WAIT 1;'

		# mute the source track
		action_list += '"' + track_name + ' SLICED"/MUTE ON;'
		action_list += 'WAIT 1;'

		# put push in step sequencing mode
		action_list += 'PUSH MODE SESSION;'
		action_list += 'WAIT 1;'

		# update user
		action_list += 'MSG "Merged ' + track_name + ' SLICED";'
		action_list += 'PUSH MSG "Merged ' + track_name + ' SLICED"'

		self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)