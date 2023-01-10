from django.urls import path
from .views import ListaPendiente, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Login, Registro
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', ListaPendiente.as_view(), name='tareas'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', Registro.as_view(), name='registro'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
    path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
    path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea'),
]
