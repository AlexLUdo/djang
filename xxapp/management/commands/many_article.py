from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from xxapp.models import Article
from userapp.models import XxUser




class Command(BaseCommand):

    def handle(self, *args, **options):
        
        Article.objects.all().delete()
        XxUser.objects.filter(is_superuser=False).delete()

        count = 100
        for i in range(count):
            p = (i/count)*100
            print(f'{i}) {p} %')
            mixer.blend(Article)

        print('end')
