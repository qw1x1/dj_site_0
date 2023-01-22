from django.shortcuts import render, redirect
from django.views import View

# class ShopCart(View):

#     def add(self, slug):
#         if request.method == 'POST':
#             if not request.session.get('cart'):
#                 request.session['cart'] = list()
#             else:
#                 request.session['cart'] = list(request.session['cart'])

#             if slug not in request.session['cart']:
#                 request.session['cart'].append(slug)
#                 request.session.modified = True

#         return redirect(request.POST.get('url_form'))

#     def remove(self, slug):
#         if self.request.method == 'POST':
#             if slug in self.request.session['cart']:
#                 self.request.session['cart'].remove(slug)

#             self.request.session.modified = True
        # return redirect(self.request.POST.get('url_form'))



def add(request, slug):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

        if slug not in request.session['cart']:
            request.session['cart'].append(slug)
            request.session.modified = True
    print(request.session['cart'])
    return redirect(request.POST.get('url_form'))

def remove(request, slug):
    if request.method == 'POST':
        if slug in request.session['cart']:
            request.session['cart'].remove(slug)

        request.session.modified = True
    return redirect(request.POST.get('url_form'))

