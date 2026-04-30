from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Order, OrderService
from apps.services.models import Service


@login_required
def add_to_order(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    # 1. Найти или создать "активный" заказ
    order, created = Order.objects.get_or_create(
        user=request.user,
        status='cart',  # статус корзины
        defaults={'total_price': 0}
    )

    # 2. Проверяем, есть ли уже такая услуга
    order_service, created = OrderService.objects.get_or_create(
        order=order,
        service=service,
        defaults={
            'quantity': 1,
            'price_at_time': service.price
        }
    )

    # 3. Если уже есть → увеличиваем количество
    if not created:
        order_service.quantity += 1
        order_service.save()

    # 4. Пересчёт цены заказа
    total = 0
    for item in order.orderservice_set.all():
        total += item.price_at_time * item.quantity

    order.total_price = total
    order.save()

    return redirect('services_list')

@login_required
def cart_view(request):
    order = Order.objects.filter(user=request.user, status='cart').first()

    return render(request, 'orders/cart.html', {
        'order': order
    })