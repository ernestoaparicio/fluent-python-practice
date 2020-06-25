# One of the best features of Python functions is the extremely flexible parameter handling mechanism, enhanced with keyword-only arguments in Python 3. Closely related are the use of * and ** to “explode” iterables and mappings into separate arguments when we call a function.


def tag(name, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    if attrs:
        attr_pairs = (f' {attr}="{value}"' for attr, value
                      in sorted(attrs.items()))
        attr_str = ''.join(attr_pairs)
    else:
        attr_str = ''
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
                    for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag(content='testing', name="img"))

# Prefixing the my_tag dict with ** passes all its items as separate arguments, which are then bound to the named parameters, with the remaining caught by **attrs. In this case we can have a 'class' key in the arguments dict, because it is a string, and does not clash with the class reserved word.
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'class': 'framed'}
print(tag(**my_tag))