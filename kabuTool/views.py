import csv
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.db.utils import IntegrityError

from .models import kabuka


def csv_reader():

    # CSVの読み込み
    csv_file = open("C:/pleiades/workspace/python/mysite/utils/files/csv/8267_1983.csv", "r", encoding="shift_jis", errors="", newline="" )

    # リスト形式
    return csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)


def data_store(list):

    for i, row in enumerate(list):
        if i == 0:
            code = row[0].split(' ')[0]

        if i >= 2:
            kjn_ymd = row[0].replace("-", "")

            try:
                kabuka.objects.update_or_create(
                    code        = code
                ,   kjn_ymd     = kjn_ymd
                ,   hzm_ne      = int(row[1])
                ,   tak_ne      = int(row[2])
                ,   yas_ne      = int(row[3])
                ,   owr_ne      = int(row[4])
                ,   dekidaka    = int(row[5])
                ,   chs_ne      = 0
                ,   del_flg     = "0"
                )
            except IntegrityError:
                print("データ登録でエラーが発生しました。code=$1,kjn_ymd=$2", code, kjn_ymd)


class IndexView(generic.TemplateView):

    data_store(csv_reader())

    template_name = 'kabuTool/index.html'


def store(request):

    data_store(csv_reader())

    return HttpResponseRedirect(reverse('kabuTool:results'))