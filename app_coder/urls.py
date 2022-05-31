from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('sucursal', views.sucursal, name='sucursal'),
    path('vendedores', views.vendedores, name='vendedores'),
    path('productos', views.productos, name='productos'),
    path('formHTML', views.form_hmtl),
    path('sucursal-django-forms', views.sucursal_forms_django, name='SucursalDjangoForms'),
    path('vendedor/add', views.vendedor_forms_django, name='vendedor-add'),
    path('vendedor/<int:pk>/update', views.update_vendedor, name='vendedor-update'),
    path('vendedor/<int:pk>/delete', views.delete_vendedor, name='vendedor-delete'),
    path('producto/add', views.productos_forms_django, name='producto-add'),
    path('search', views.search, name='Search'),


    #D#ajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    
    #from django.urls import path
    #from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    #urlpatterns = [
     # ...
    #path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
     #]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.

    path('sucursal', views.SucursalListView.as_view(), name='sucursal_list'),
    path('sucursal/add/', views.SucursalCreateView.as_view(), name='sucursal-add'),
    path('sucursal/<int:pk>/detail', views.SucursalDetailView.as_view(), name='sucursal-detail'),
    path('sucursal/<int:pk>/update', views.SucursalUpdateView.as_view(), name='sucursal-update'),
    path('sucursal/<int:pk>/delete', views.SucursalDeleteView.as_view(), name='sucursal-delete'),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
]
