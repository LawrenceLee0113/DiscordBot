from openpyxl import Workbook,load_workbook
from os.path import join
import time
from datetime import datetime,timezone,timedelta


class it_is_not_a_class():
    def __init__(self):
        self.reason = "idk how to write class"
    def get_reason(self,print=False):
        if print:
            print(self.reason)
        return self.reason

class Classes:
    def __init__(self):
        #workbook初始化
        self.wb = load_workbook(join("classes.xlsx"))
        self.ws = self.wb.active
        #時區設定
        self.utf = datetime.utcnow().replace(tzinfo=timezone.utc)
        self.taiwan_tz = self.utf.astimezone(timezone(timedelta(hours=8)))

    def call(self):
        pass