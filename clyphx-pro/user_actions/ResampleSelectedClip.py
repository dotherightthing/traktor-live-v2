"""
Class: ResampleSelectedClip
_________________________________________________________________________________________

TESTING:

```sh
# note: the version string will change if Live auto-updates itself
tail -f '/Users/dan/Library/Preferences/Ableton/Live 10.1.42/Log.txt'
```

```py
self.canonical_parent.log_message('Hello world')
```
_________________________________________________________________________________________

"""

# Import UserActionsBase to extend it.
from ClyphX_Pro.clyphx_pro.UserActionsBase import UserActionsBase

# Your class must extend UserActionsBase.
class ResampleSelectedClip(UserActionsBase):
    # Your class must implement this method.
    def create_actions(self):
        # called by Macros.txt
        self.add_clip_action('id_playing_clip', self.id_playing_clip)

    # def on_selected_track_changed(self):
    #     empty_dict = {}
    #     self.my_action(empty_dict, 'my_str')

    # when a button is pressed
    # get the name and length of the selected clip
    # there is no Button Binding for this, so a user action is required
    def id_playing_clip(self, action_def, args):
        # the current Live set object
        # see also https://docs.cycling74.com/max8/vignettes/live_object_model
        live_set = self.song()

        song_view = live_set.view
        selected_track = song_view.selected_track
        selected_track_name = selected_track.name

        # see https://docs.cycling74.com/max8/vignettes/live_object_model > playing_slot_index
        clip_stop_slot_fired_in_session_view = -2

        if (selected_track_name != 'DECK A') and (selected_track_name != 'DECK B'):
            tracks = list(live_set.tracks)
            selected_track_index = list(tracks).index(selected_track)
            track = list(tracks)[selected_track_index]
            msg = selected_track_name + ': '

            # self.canonical_parent.log_message('slot index = ' + track.playing_slot_index)

            # self.canonical_parent.clyphx_pro_component.trigger_action_list('MSG "slot index = ' + track.playing_slot_index + '"')

            if track.playing_slot_index > clip_stop_slot_fired_in_session_view:
                playing_slot = list(track.clip_slots)[track.playing_slot_index]
                playing_clip = playing_slot.clip

                # Clip name
                playing_clip_name = playing_clip.name

                playing_clip_length = playing_clip.length
                action_list = ''
                track_name = track.name

                if playing_clip and playing_clip.looping:
                    msg += playing_clip_name + ' (' + str(playing_clip_length/4) + ' bars)'
                else:
                    msg += playing_clip_name + '(' + str(playing_clip_length/4) + ' bars) is playing but not looping'

                # Insert an Audio Track to the right of the selected Track that will be armed and routed from the selected Track
                action_list += '; INSAUDIO'

                # By default track is named after source track
                # Rename after clip that we are intending to resample
                action_list += '; SEL/NAME "' + playing_clip_name + ' RS"'

                # Change the colour of the resample clip to a consistent PINK (27/70)
                # This colour is also used by the clip
                action_list += '; SEL/COLOR 27'

                # Unarm all tracks
                action_list += '; "SAMPLE 1"/ARM OFF'
                action_list += '; "SAMPLE 2"/ARM OFF'
                action_list += '; "SAMPLE 3"/ARM OFF'
                action_list += '; "SAMPLE 4"/ARM OFF'
                action_list += '; "RESAMPLE"/ARM OFF'

                # Trigger fixed-length Session Record on all armed Tracks where x is the length to record in Bars
                # New clip automatically plays after this
                action_list += '; SRECFIX ' + str(playing_clip_length/4)

                # Wait until the recording has finished
                action_list += '; WAITS ' + str(playing_clip_length/4) + 'B'

                action_list += '; WAIT 10'

                # Copy the Clip playing on the Track for use with the PASTECLIP Action
                action_list += '; SEL/COPYCLIP'

                # Paste the clip into the source track
                # TODO not working
                action_list += '; "' + track_name + '"/PASTECLIP EMPTY'

                # Reset devices on source track
                action_list += '; "' + track_name + '"/DEV(1) P1 127'
                action_list += '; "' + track_name + '"/DEV(1) P2 63'
                action_list += '; "' + track_name + '"/DEV(1) P3 107'
                action_list += '; "' + track_name + '"/DEV(1) P4 107'
                action_list += '; "' + track_name + '"/DEV(1) P5 107'
                action_list += '; "' + track_name + '"/DEV(1) P6 0'
                action_list += '; "' + track_name + '"/DEV(1) P7 0'
                action_list += '; "' + track_name + '"/DEV(1) P8 63'
                action_list += '; "' + track_name + '"/DEV(2) P1 0'
                action_list += '; "' + track_name + '"/DEV(2) P2 63'
                action_list += '; "' + track_name + '"/DEV(2) P3 63'
                action_list += '; "' + track_name + '"/DEV(2) P4 63'
                action_list += '; "' + track_name + '"/DEV(2) P5 63'
                action_list += '; "' + track_name + '"/DEV(2) P6 63'
                action_list += '; "' + track_name + '"/DEV(2) OFF'
                action_list += '; "' + track_name + '"/PAN 63'
                action_list += '; "' + track_name + '"/SEND A 0'
                action_list += '; "' + track_name + '"/SEND B 0'

                # Play the pasted clip
                #

                # Delete resample track
                #

                # Rearm tracks
                action_list += '; "SAMPLE 1"/ARM ON'
                action_list += '; "SAMPLE 2"/ARM ON'
                action_list += '; "SAMPLE 3"/ARM ON'
                action_list += '; "SAMPLE 4"/ARM ON'
                action_list += '; "RESAMPLE"/ARM ON'
            else:
                msg += 'no clip playing'

            action_list += '; PUSH MSG "' + msg + '"; MSG "' + msg + '"'

            # self.canonical_parent.log_message('loop_led: ' + action_list)
            self.canonical_parent.clyphx_pro_component.trigger_action_list(action_list)