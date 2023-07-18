from django import template
register=template.Library()

@register.filter()#swapping is the filter nama of function
def swap(data):
    return data.swapcase()


@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def map(data):
    k=data.split()
    r=''
    for i in range(len(k)):
        if i==0 or i==len(k)-1:
            r+=k[i]+' '
        else:
            r+=k[i].lower()+' '
    return r
@register.filter()
def count(data):
    r=0
    for i in range(len(data)):
        if data[i]=='i':
            r+=1
    return r

#register.filter('swap',swap)
#register.filter('remove',remove)