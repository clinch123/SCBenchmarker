import hashlib
from .constants import \
    OWN_REPLAY_TAG, \
    BENCH_REPLAY_TAG


def get_file_hash(filedata):
    return hashlib.md5(filedata).hexdigest()


def valid_names(request):
    """checks whether incoming data has correct names"""
    if OWN_REPLAY_TAG not in request.files:
        return False
    elif BENCH_REPLAY_TAG not in request.files:
        return False
    else:
        return True


def dual_data(func, in1, in2):
    return func(in1), func(in2)
