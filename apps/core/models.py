from django.db import models


class TimeStampedModel(models.Model):
    """
    Базовая модель для всех сущностей:
    created_at + updated_at
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    """
    Логическое удаление вместо физического
    """
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

class BaseModel(TimeStampedModel, SoftDeleteModel):
    """
    Общая база для всех моделей проекта
    """
    class Meta:
        abstract = True