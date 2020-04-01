#!/usr/bin/env python
#
# This is an example of the command pattern.

import os

class CommandRenameFile(object):
    def __init__(self, from_name, to_name):
        # Set the private variables.
        self._from = from_name
        self._to = to_name

    # Rename the file extension.
    def action(self):
        os.rename(self._from, self._to)

    # Undo the renaming of the file extensions.
    def undo(self):
        os.rename(self._to, self._from)

class History(object):
    def __init__(self):
        self._commands = list()

    def action(self, command):
        self._commands.append(command)
        # Runs the renaming.
        command.action()

    def undo(self):
        self._commands.pop().undo()

if __name__ == '__main__':
    history = History()
    history.action(CommandRenameFile('./file1.txt', 'edit-file1.txt'))
    history.action(CommandRenameFile('./file2.txt', 'edit-file2.txt'))
    history.undo()
    history.undo()