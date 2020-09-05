class MagicWSLNotFoundError(Exception):
    pass


class MagicRAMDiskError(Exception):
    pass


class MagicIOError(Exception):
    pass


class MagicPerformanceIssue(Warning):
    pass


class MagicSingleThreadCall(Warning):
    pass


class MagicKeyNotFound(Warning):
    pass


class MagicKeyAlreadyExists(Warning):
    pass


class MagicVersionConflict(Warning):
    pass

