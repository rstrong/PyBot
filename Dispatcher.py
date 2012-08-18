import importlib
import sys
import traceback

class Dispatcher(object):
    modules = []
    def __init__(self):
        try:
            self.modules.append(importlib.import_module('modules.weather', 'modules'))
            self.modules.append(importlib.import_module('modules.dns', 'modules'))
        except:
            e = sys.exc_info()[0]
            traceback.print_exc(file=sys.stdout)
            print e
            print "EXCEPTION: %s" % e
            print "Error loading module"

    def multiplex_msg(self, user, channel, msg):
        for module in self.modules:
            print module
            str = module.say(user, channel, msg)
            if str:
                return str
        

