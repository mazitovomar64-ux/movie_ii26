from .models import Category, Movie, Country, MovieLanguages, Genre
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Movie)
class ProductTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description','slogan')



@register(Country)
class ProductTranslationOptions(TranslationOptions):
    fields = ('country_name', )



@register(MovieLanguages)
class ProductTranslationOptions(TranslationOptions):
    fields = ('Language', )



@register(Genre)
class ProductTranslationOptions(TranslationOptions):
    fields = ('genre_name', )


