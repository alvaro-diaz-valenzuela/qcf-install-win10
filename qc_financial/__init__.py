import sys
if sys.version_info.major == 2: 
    from . QC_Financial import *
elif sys.version_info.minor == 7:
    from . QC_Financial_37 import *
elif sys.version_info.minor == 8:
    from . QC_Financial_38 import *
elif sys.version_info.minor == 9:
    from . QC_Financial_39 import *
else:
    from . QC_Financial_310 import *
