from django.db import models


class kabuka(models.Model):
    code        = models.CharField(max_length=4)
    kjn_ymd     = models.CharField(max_length=8)
    hzm_ne      = models.IntegerField()
    tak_ne      = models.IntegerField()
    yas_ne      = models.IntegerField()
    owr_ne      = models.IntegerField()
    dekidaka    = models.IntegerField()
    chs_ne      = models.IntegerField()
    del_flg     = models.CharField(max_length=1, default=0)

    # 複合PKは使用できないので、こちらで制御
    class Meta:
        unique_together = (
            ('code', 'kjn_ymd'),
        )
