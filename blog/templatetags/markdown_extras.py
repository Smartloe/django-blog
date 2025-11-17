from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()


@register.filter
def markdownify(value):
    """
    Render Markdown text to HTML.
    Supports fenced code blocks and tables.
    """
    if not value:
        return ""
    html = md.markdown(value, extensions=["fenced_code", "tables"])
    return mark_safe(html)
