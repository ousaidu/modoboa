# -*- coding: utf-8 -*-

"""
This module provides a simple way of managing events between MailNG
core application and additional components.

"""

events = ["CreateDomain",
          "DeleteDomain",
          "CreateMailbox",
          "DeleteMailbox",
          "ModifyMailbox",

          "UserMenuDisplay",
          "AdminMenuDisplay",

          "UserLogin"]

callbacks = {}

def register(event, callback):
    if not event in events:
        return 0
    if not event in callbacks.keys():
        callbacks[event] = []
    callbacks[event].append(callback)
    return 1

def unregister(event, callback):
    if not event in events:
        return False
    if not callbacks.has_key(event):
        return False
    callbacks[event].remove(callback)

def raiseEvent(event, **kwargs):
    if not event in events or not event in callbacks.keys():
        return 0
    for callback in callbacks[event]:
        callback(**kwargs)
    return 1

def raiseQueryEvent(event, **kwargs):
    result = []
    if not event in events or not event in callbacks.keys():
        return result
    for callback in callbacks[event]:
        result += callback(**kwargs)
    return result
