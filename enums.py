from enum import IntEnum


class Algorithm_Category(IntEnum):
    BS = 0
    BP = 1
    BT = 2
    WG = 3


class WG_Message_Ids(IntEnum):
    MAWGN001 = 1
    MAWGN002 = 2
    MAWGN003 = 3
    MAWGN004 = 4
    MAWGN005 = 5


class BP_Scenario_Ids(IntEnum):
    SCBPN001 = 1
    SCBPN002 = 2
    SCBPN003 = 3
    SCBPN004 = 4
    SCBPN005 = 5
    SCBPN006 = 6
    SCBPN007 = 7
    SCBPN008 = 8
    SCBPN009 = 9
    SCBPN010 = 10
    SCBPN011 = 11
    MABPN001 = 12
    MABPN002 = 13
    MABPN003 = 14
    MABPN004 = 15
    MABPN005 = 16


class BS_Scenario_Ids(IntEnum):
    SCBSN000 = 0
    SCBSN001 = 1
    SCBSN002 = 2
    SCBSN003 = 3
    SCBSN004 = 4
    SCBSN005 = 5
    SCBSN006 = 6
    SCBSN007 = 7
    SCBSN008 = 8
    SCBSN009 = 9
    SCBSN010 = 10
    SCBSN011 = 11
    SCBSN012 = 12
    SCBSN013 = 13
    SCBSN014 = 14
    SCBSN015 = 15
    SCBSN016 = 16
    SCBSN017 = 17
    SCBSN018 = 18
    MABSN001 = 19
    MABSN002 = 20
    MABSN003 = 21
    MABSN004 = 22
    MABSN005 = 23


class BT_Scenario_Ids(IntEnum):
    SCT001 = 1
    SCT002 = 2
    SCT003 = 3
    SCT004 = 4
    SCT005 = 5
    SCT006 = 6
