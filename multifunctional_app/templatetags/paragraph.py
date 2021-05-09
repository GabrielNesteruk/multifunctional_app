from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


def showText(text, text_details):
    data = {
        'text': text,
        'color': text_details['color'],
        'size': text_details['size'],
        'font': text_details['font'],
    }
    return data


paragraph_template = get_template('paragraph.html')
register.inclusion_tag(paragraph_template)(showText)


def bold(text):
    splited = text.split()
    return_text = ""
    for word in splited:
        start = word[:1]
        end = word[-1:]

        if start == '*' and end == '*' and word.count("*") == 2:
            word = word[1:-1]
            return_text += '<b>' + word + '</b> '
        else:
            return_text += word + ' '
    return mark_safe(return_text)


def italic(text):
    splited = text.split()
    return_text = ""
    for word in splited:
        start = word[:2]
        end = word[-2:]

        if start == '**' and end == '**' and word.count("*") == 4:
            word = word[2:-2]
            return_text += '<i>' + word + '</i> '
        else:
            return_text += word + ' '
    return mark_safe(return_text)


def strike(text):
    splited = text.split()
    return_text = ""
    for word in splited:
        start = word[:3]
        end = word[-3:]

        if start == '***' and end == '***' and word.count("*") == 6:
            word = word[3:-3]
            return_text += '<s>' + word + '</s> '
        else:
            return_text += word + ' '
    return mark_safe(return_text)


def new_line(text):
    return mark_safe(text.replace('&nl', '<br>'))


register.filter('bold', bold)
register.filter('new_line', new_line)
register.filter('italic', italic)
register.filter('strike', strike)
