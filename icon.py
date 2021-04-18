#!/usr/bin/env python

fn = "/sys/block/sda/stat"
ro, wo = 0, 0
last = ""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
from gi.repository import Gtk
tray = Gtk.StatusIcon()
tray.set_visible(True)

def update():
	global ro, wo, last

	f = open(fn).read().split()
	r, w = f[0], f[4]
	rr, ww = "0", "0"
	if r != ro:
		rr = "1"
	if w != wo:
		ww = "1"
	ro, wo = r, w
	i = f"icon{rr}{ww}.png"
	if i != last:
		tray.set_from_file(i)
		tray.set_visible(True)
		last = i
	GObject.timeout_add(100, update)

GObject.timeout_add(100, update)
Gtk.main()

