import csv

from .models import kabuka


def csv_reader():

    # CSVの読み込み
    csv_file = open("C:/pleiades/workspace/python/mysite/utils/files/csv/8267_1983.csv", "r", encoding="shift_jis", errors="", newline="" )

    # リスト形式
    return csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)


def data_store(list):

    for i, row in enumerate(list):
        print(i, row)

        if i == 0:
            code = row[0].split(' ')[0]
            print(code)

        if i >= 2:
            kabuka.objects.update_or_create(
                code        = code
            ,   kjn_ymd     = ""
            ,   hzm_ne      = ""
            ,   tak_ne      = ""
            ,   yas_ne      = ""
            ,   owr_ne      = ""
            ,   dekidaka    = ""
            ,   chs_ne      = ""
            ,   del_flg     = ""
            )


if __name__ == '__main__':

    list = csv_reader()

    data_store(list)
