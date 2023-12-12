import itertools
import numpy as np
import io
from pydub import AudioSegment

def concatenate_audio_bytes(bytesa: bytes, bytesb: bytes) -> bytes:
    """
    Combines ` bytesa` and `bytesb` as audio files

    Arguments:
        bytesa (bytes): First item.
        bytesb (bytes): Second item.

    Returns:
        bytes: `{bytesa} {bytesb}`
    """
    return  np.hstack((bytesa, bytesb))

def mix_audio_files(bytesA, bytesB):
    """
    Mixes the audio represented by ` bytesa` and `bytesb` into a single AudioSegment
    by overlaying them (i.e. playing the two inputs simultaneously)

    Arguments:
        bytesa (bytes): First item.
        bytesb (bytes): Second item.

    Returns:
        bytes: the raw data of a single channel mix of bytesA and bytesB, the duration
               of which is equal to the duration of the longer input
    """
    asA = AudioSegment.from_file(io.BytesIO(bytesA))
    asB = AudioSegment.from_file(io.BytesIO(bytesB))
    maxDuration = max(len(asA), len(asB))
    asMerged = AudioSegment.silent(duration=maxDuration).overlay(asA).overlay(asB)
    return asMerged.raw_data

def concatenate_with_space(stringa: str, stringb: str) -> str:
    """
    Combines `stringa` and `stringb` with a space.

    Arguments:
        stringa (str): First item.
        stringb (str): Second item.

    Returns:
        str: `{stringa} {stringb}`
    """
    return stringa + " " + stringb


def aggregate_strings(stringa: str, stringb: str, by_character: bool = False) -> str:
    """
    Aggregates strings.

    (replaces agg_by_jag_char, agg_by_jag_word)

    Arguments:
        stringa (str): First item.
        stringb (str): Second item.
        by_character (bool): True if you want to join the combined string by character,
                             Else combines by word

    Returns:
        str: combination of stringa and stringb
    """

    stringa_list: list = stringa.split()
    stringb_list: list = stringb.split()

    zipped_lists: list = list(zip(stringa_list, stringb_list))
    out: list = list(itertools.chain(*zipped_lists))

    aggregated: str = ("" if by_character else " ").join(out)
    return aggregated
