from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Material
from .forms import MaterialForm

# Перевірка прав (адміни та модератори)
def is_staff_or_moderator(user):
    return user.is_authenticated and (user.is_staff or user.groups.filter(name='Moderators').exists())

# 1. Перегляд усіх матеріалів
def material_list(request):
    materials = Material.objects.all().order_by('-created_at')
    return render(request, 'materials/material_list.html', {'materials': materials})

# 2. Додавання матеріалу
@user_passes_test(is_staff_or_moderator)
def material_create(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.author = request.user
            material.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form})

# 3. Редагування матеріалу (функція, якої не вистачало)
@user_passes_test(is_staff_or_moderator)
def material_edit(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/material_form.html', {'form': form})

# 4. Видалення матеріалу
@user_passes_test(is_staff_or_moderator)
def material_delete(request, pk):
    material = get_object_or_404(Material, pk=pk)
    material.delete()
    return redirect('material_list')