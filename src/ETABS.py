import sys
import comtypes.client

def start() -> None:

  helper = comtypes.client.CreateObject("ETABSv17.Helper")
  helper = helper.QueryInterface(comtypes.gen.ETABSv17.cHelper)

  try:
    ETABS = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject")
  except (OSError, comtypes.COMError):
    print("Cannot start a new instance of the program.")
    sys.exit(-1)

  ETABS.ApplicationStart()
  SAP = ETABS.SapModel
  SAP.InitializeNewModel()