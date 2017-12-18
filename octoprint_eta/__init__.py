# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from octoprint.util import RepeatedTimer
import time

class DisplayETAPlugin(octoprint.plugin.ProgressPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.EventHandlerPlugin):

    def __init__(self):
        self.activated = True
        self.timer = RepeatedTimer(5.0, DisplayETAPlugin.fromTimer, args=[self], run_first=False,)
        self.timer.start()
        self.currentFile=None
    def on_event(self,event, payload):
        if event == "FileSelected":
            self.currentFile=payload["file"]
            
    def fromTimer(self):
        self._logger.info("The Timer Has Fired")
        self._logger.info(self._printer.get_current_job())
        self._printer.select_file('/home/pablo/.octoprint/uploads/20mm_hollow_cube.gcode', False, printAfterSelect=True)

        self.timer.cancel()
        #self._plugin_manager.send_plugin_message(self._identifier, dict(eta_string=self.eta_string))
            
    def get_assets(self):
        return {
            "js": ["js/displayeta.js"]
        } 

__plugin_name__ = "Display ETA"
__plugin_identifier = "display-eta"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A quick \"Hello World\" example plugin for OctoPrint"
__plugin_implementation__ = DisplayETAPlugin()
