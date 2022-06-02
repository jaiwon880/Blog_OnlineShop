from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    use_from = models.DateTimeField() # 이 날 부터
    use_to = models.DateTimeField() # 언제까지
    amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)]) # 할일 시 총금액
    # Min~ MAx~ 최소 값과 최대값
    active = models.BooleanField() # True로 등록을해야 쿠폰을 사용할 수 있음

    def __str__(self):
        return self.code
