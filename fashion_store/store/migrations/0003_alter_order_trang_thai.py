# Generated by Django 4.2 on 2025-03-17 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_trang_thai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='trang_thai',
            field=models.CharField(choices=[('dang_xu_ly', 'Đang xử lý'), ('da_xu_ly', 'Đã xử lý'), ('cho_giao_hang', 'Chờ giao hàng'), ('dang_giao_hang', 'Đang giao hàng'), ('da_giao_hang', 'Đã giao hàng'), ('da_huy', 'Đã hủy')], default='dang_xu_ly', max_length=20),
        ),
    ]
