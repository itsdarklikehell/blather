# This is part of Blather
# -- this code is licensed GPLv3
# Copyright 2013 Jezra (original)
# Ported to Python 3 / GStreamer 1.0

import os.path
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

GObject.type_register(Gst.Pipeline)


class Recognizer(GObject.GObject):
    __gsignals__ = {
        'finished': (GObject.SignalFlags.RUN_LAST, None, (str,))
    }

    def __init__(self, language_file, dictionary_file, src=None):
        GObject.GObject.__init__(self)
        self.commands = {}
        if src:
            audio_src = f'alsasrc device="hw:{src},0" ! audioconvert ! audioresample'
        else:
            audio_src = 'autoaudiosrc ! audioconvert ! audioresample'

        # VAD + pocketsphinx pipeline
        pipeline_str = (
            f'{audio_src} ! vader name=vad auto-threshold=true '
            f'! pocketsphinx name=asr lm={language_file} dict={dictionary_file} '
            f'! fakesink sync=false'
        )

        self.pipeline = Gst.parse_launch(pipeline_str)
        if not self.pipeline:
            raise RuntimeError("Failed to create GStreamer pipeline")

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect("message", self._on_bus_message)

        asr = self.pipeline.get_by_name('asr')
        if asr:
            asr.set_property('configured', True)

    def _on_bus_message(self, bus, message):
        if message.type == Gst.MessageType.ELEMENT:
            s = message.get_structure()
            if s and s.get_name() == 'pocketsphinx':
                text = s.get_string('hypothesis')
                if text and text.strip():
                    self.emit("finished", text.strip())

    def listen(self):
        self.pipeline.set_state(Gst.State.PLAYING)

    def pause(self):
        self.pipeline.set_state(Gst.State.PAUSED)

    def stop(self):
        self.pipeline.set_state(Gst.State.NULL)
