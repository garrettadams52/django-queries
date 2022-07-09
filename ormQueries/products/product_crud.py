from .models import Product 
from django.db.models import Q,Avg,Max
from django.db.models.functions import Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls,name):
        return Product.objects.get(model=name)

    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls,ratin):
        return Product.objects.filter(rating__exact=ratin)

    @classmethod
    def by_rating_range(cls,beg,end):
        return Product.objects.filter(rating__range=(beg,end))

    @classmethod
    def by_rating_and_color(cls,ratin,col):
        return Product.objects.filter(Q(rating=ratin)&Q(color=col))

    @classmethod
    def by_rating_or_color(cls,ratin,col):
        return Product.objects.filter(Q(rating=ratin)|Q(color=col))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()

    @classmethod
    def below_price_or_above_rating(cls,pri,ratin):
        return Product.objects.filter(Q(rating__gt=ratin)|Q(price_cents__lt=pri))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category','-price_cents')

    @classmethod
    def products_by_manufacturer_with_name_like(cls,like):
        return Product.objects.filter(manufacturer__contains=like)

    @classmethod
    def manufacturer_names_for_query(cls,like):
        dic = Product.objects.filter(manufacturer__contains=like).values('manufacturer')
        lst = [i['manufacturer'] for i in dic]
        return lst

    @classmethod
    def not_in_a_category(cls,like):
        return Product.objects.filter(~Q(category__contains=like))

    @classmethod
    def limited_not_in_a_category(cls,like,lim):
        return Product.objects.filter(~Q(category__contains=like))[:lim]

    @classmethod
    def category_manufacturers(cls,cate):
        dic = Product.objects.filter(category__contains=cate).values('manufacturer')
        lst = [i['manufacturer'] for i in dic]
        return lst

    @classmethod
    def average_category_rating(cls,like):
        return Product.objects.filter(category__contains=like).values('rating').aggregate(rating__avg=Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(price_cents__max=Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        ans = Product.objects.annotate(model_txt_length=Length('model')).aggregate(length_max=Max('model_txt_length'))
        ansd = Product.objects.annotate(model_txt_length=Length('model')).filter(model_txt_length=ans['length_max']).values('id')
        return list(ansd)[0]['id']

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.annotate(model_txt_length=Length('model')).order_by('model_txt_length').values('id')
       


    
        

       
      
    
       
        
       

        

    

        

        

    

        
