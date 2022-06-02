from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import AddCouponForm

# Create your views here.

@require_POST
def add_coupon(request): # post메소드만 받아서 처리하도록 함
    now = timezone.now()
    form = AddCouponForm(request.POST)
    if form.is_valid(): # 있는 쿠폰인지 조회함
        code = form.cleaned_data['code']

        try:
            coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now,
                                        use_to__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:detail')

