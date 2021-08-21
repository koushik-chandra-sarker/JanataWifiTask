import json

from django.core.management.base import BaseCommand

from crud.models import StockMarket


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        d = open('stock_market_data.json')
        data = json.load(d)
        for i in data:
            stockMarket = StockMarket(date=i['date'], trade_code=i['trade_code'], high=i['high'], low=i['low'],
                                      open=i['open'], close=i['close'], volume=i['volume'])
            stockMarket.save()
    # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
