#!/usr/bin/python3
"""
Command interpreter for the HBNB project
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        return True

    def help_quit(self):
        """Help for quit command"""
        print("Quit the command interpreter.")

    def help_EOF(self):
        """Help for EOF command"""
        print("Exit the command interpreter.")

    def emptyline(self):
        """Do nothing on empty input"""
        pass

    def do_help(self, arg):
        """Override the default help command to include custom commands"""
        super().do_help(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
