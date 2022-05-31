from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

from app_coder.models import Sucursal, Vendedor, Producto
from app_coder.forms import SucursalForm, VendedorForm, ProductosForm


def index(request):
    return render(request, "app_coder/home.html")


def sucursal(request):
    sucursal = Sucursal.objects.all()

    context_dict = {
        'sucursal': sucursal
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/sucursal.html"
    )


def vendedores(request):
    vendedores = Vendedor.objects.all()

    context_dict = {
        'vendedores': vendedores
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/vendedor.html"
    )


def productos(request):
    productos = Producto.objects.all()

    context_dict = {
        'productos': productos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/productos.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        sucursal = Sucursal(name=request.POST['name'], code=request.POST['code'])
        sucursal.save()

        sucursal = Sucursal.objects.all()
        context_dict = {
            'sucursal': sucursal
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/sucursal.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def sucursal_forms_django(request):
    if request.method == 'POST':
        sucursal_form = SucursalForm(request.POST)
        if sucursal_form.is_valid():
            data = sucursal_form.cleaned_data
            sucursal = Sucursal(name=data['name'], code=data['code'])
            sucursal.save()

            sucursal = Sucursal.objects.all()
            context_dict = {
                'sucursal': sucursal
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/sucursal.html"
            )

    sucursal_form = SucursalForm(request.POST)
    context_dict = {
        'sucursal_form': sucursal_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/sucursal_django_forms.html'
    )


@login_required
def vendedor_forms_django(request):
    if request.method == 'POST':
        vendedor_form = VendedorForm(request.POST)
        if vendedor_form.is_valid():
            data = vendedor_form.cleaned_data
            vendedor = Vendedor(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                area=data['area'],
            )
            vendedor.save()

            vendedor = Vendedor.objects.all()
            context_dict = {
                'vendedor': vendedor
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/vendedor.html"
            )

    vendedor_form = VendedorForm(request.POST)
    context_dict = {
        'vendedor_form': vendedor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/vendedor_django_forms.html'
    )


@login_required
def update_vendedor(request, pk: int):
    vendedor = Vendedor.objects.get(pk=pk)

    if request.method == 'POST':
        vendedor_form = VendedorForm(request.POST)
        if vendedor_form.is_valid():
            data = vendedor_form.cleaned_data
            vendedor.name = data['name']
            vendedor.last_name = data['last_name']
            vendedor.email = data['email']
            vendedor.area = data['area']
            vendedor.save()

            vendedor = Vendedor.objects.all()
            context_dict = {
                'vendedor': vendedor
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/vendedor.html"
            )

    vendedor_form = VendedorForm(model_to_dict(vendedor))
    context_dict = {
        'vendedor': vendedor,
        'vendedor_form': vendedor_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/vendedor_form.html'
    )


@login_required
def delete_vendedor(request, pk: int):
    vendedor = Vendedor.objects.get(pk=pk)
    if request.method == 'POST':
        vendedor.delete()

        vendedor = Vendedor.objects.all()
        context_dict = {
            'vendedor': vendedor
        }
        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/vendedor.html"
        )

    context_dict = {
        'vendedor': vendedor,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/vendedor_confirm_delete.html'
    )


def productos_forms_django(request):
    if request.method == 'POST':
        productos_form = ProductosForm(request.POST)
        if productos_form.is_valid():
            data = productos_form.cleaned_data
            productos = Producto(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            productos.save()

            productos = Producto.objects.all()
            context_dict = {
                'productos': productos
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/productos.html"
            )

    productos_form = ProductosForm(request.POST)
    context_dict = {
        'productos_form': productos_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/productos_django_forms.html'
    )


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class SucursalListView(ListView):
    model = sucursal
    template_name = "app_coder/sucursal_list.html"


class SucursalDetailView(DetailView):
    model = sucursal
    template_name = "app_coder/course_detail.html"


class SucursalCreateView(LoginRequiredMixin, CreateView):
    model = sucursal
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:sucursal-list')
    fields = ['name', 'code']


class SucursalUpdateView(LoginRequiredMixin, UpdateView):
    model = sucursal
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class SucursalDeleteView(LoginRequiredMixin, DeleteView):
    model = sucursal
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')


from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from app_coder.forms import UserRegisterForm

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario Registrado satisfactoriamente."},
                template_name="app_coder/home.html",
            )
    else:
        form = UserCreationForm()
        # form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="app_coder/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "app_coder/home.html"
        else:
            template_name = "app_coder/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_coder/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("app_coder:Home")

def search(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        sucursales = Sucursal.objects.filter(query)
        context_dict = {
            'sucursales': sucursales
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )