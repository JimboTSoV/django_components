from django import template
from django.template.loader import get_template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def render_placeholder(context, page, placeholder_name):
    current_placeholder = page.placeholders.filter(placeholder_type__name=placeholder_name).first()
    components = current_placeholder.components.all()
    html = ""
    for component in components:
        html = html + component.render()

    html = mark_safe(html)

    if not context['edit_mode']:
        return html

    edit_template = get_template("pages/_base_placeholder_edit.html")
    return edit_template.render(context={'placeholder': current_placeholder, 'html': html})
