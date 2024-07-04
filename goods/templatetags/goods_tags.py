# Create customs tags as static

from django import template

from goods.models import Categories

# Default used name is "register"
register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
