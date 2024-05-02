import re

from ..schema_board import PATTERN_BOARD



def validate_board(board_to_check: str):
    """check if the board is valid"""
    
    return re.findall(
        PATTERN_BOARD,
        board_to_check
    )
