import atheris
import sys
import os
from packagedcode.debian import DebianDebPackageHandler
from licensedcode.detection import is_correct_detection, calculate_query_coverage_coefficient

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    # Fuzz Debian package handler
    try:
        DebianDebPackageHandler.parse(fdp.ConsumeBytes(len(data)))
    except Exception:
        pass
    
    # Fuzz license detection functions
    try:
        license_matches = fdp.ConsumeUnicodeNoSurrogates(1000)
        is_correct_detection(license_matches)
        calculate_query_coverage_coefficient(license_matches)
    except Exception:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
