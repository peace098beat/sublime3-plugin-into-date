"""

## KEYMAP
[
    { "keys": ["super+;"], "command": "into_date" },
    { "keys": ["super+:"], "command": "into_time" },
    { "keys": ["super+shift+;"], "command": "into_date_time" },
]

"""
import sublime
import sublime_plugin

from datetime import datetime as dt


class IntoDateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			tdatetime = dt.now()
			tstr = tdatetime.strftime('%Y-%m-%d')
			self.view.insert(edit, region.a, tstr)




class IntoTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			tdatetime = dt.now()
			tstr = tdatetime.strftime('%H:%M:%S')
			self.view.insert(edit, region.a, tstr)


class IntoDateTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			tdatetime = dt.now()
			tstr = tdatetime.strftime('%Y-%m-%d %H:%M:%S')
			self.view.insert(edit, region.a, tstr)


