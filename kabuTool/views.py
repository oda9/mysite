import csv
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import kabuka

class IndexView(generic.TemplateView):
    template_name = 'kabuTool/index.html'


def store(request):

    data_store(csv_reader())

    return HttpResponseRedirect(reverse('polls:results'))

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
