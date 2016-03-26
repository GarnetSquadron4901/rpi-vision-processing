import Pyro4
import sys

ledService = Pyro4.Proxy('PYRONAME:ledService')
ledService.setErrorColor(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))