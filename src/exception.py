import os
import sys
from src.logger import logging


def get_error_detail(error,error_detail:sys):
    _,_,exec_tb=error_detail.exc_info()
    filename=exec_tb.tb_frame.f_code.co_filename
    lineNo=exec_tb.tb_lineno
    error_message=f"The error occured at [{filename}] along with the lineNumber [{lineNo}] and error message is [{str(error)}]"
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=get_error_detail(error=error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    




