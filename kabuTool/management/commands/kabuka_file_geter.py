from django.core.management import BaseCommand
from utils import fileDownLoader


class Command(BaseCommand):
    help = 'ここにコマンドの説明を書けます。'
    def add_arguments(self, parser):
        #parser.add_argument('opt1', help='必須オプション')
        #parser.add_argument('--opt2', help='任意オプション')
        pass

    def handle(self, *args, **options):

        # ここに処理が書ける
        # fileDownLoader.main()
        pass