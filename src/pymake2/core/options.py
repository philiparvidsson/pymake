#---------------------------------------
# CLASSES
#---------------------------------------

class Options(object):
    #---------------------------------------
    # CONSTRUCTOR
    #---------------------------------------

    def __init__(self):
        self.conf     = None
        self.no_color = False
        self.no_exit  = False
        self.no_warn  = False

    #---------------------------------------
    # METHODS
    #---------------------------------------

    def parse(self, opt):
        value = None

        if opt.find('=') > 0:
            s     = opt.split('=', 1)
            opt   = s[0]
            value = s[1]

        if opt == '--conf' and value and not self.conf:
            self.conf = ast.literal_eval(value)

        if opt == '--no-color':
            self.no_color = True
            return True

        if opt == '--no-exit':
            self.no_exit = True
            return True

        if opt == '--no-warn':
            self.no_warn = True
            return True

        return False