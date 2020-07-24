from django import template

register = template.Library()

@register.filter(name='find_element_at_index')
def find_element_at_index(value,arg):
    if value[arg]=="both":
        html_string = """<form class=\"upvote\" > <button type=\"submit\">Upvote</button></form>
                      <form class=\"downvote\" > <button type=\"submit\">Downvote</button></form> """
        return html_string
    else:
        return "you have "+(value[arg]).lower()+"d this answer"
