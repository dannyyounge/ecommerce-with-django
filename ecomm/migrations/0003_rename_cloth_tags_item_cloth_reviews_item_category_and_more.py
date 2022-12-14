# Generated by Django 4.0.5 on 2022-06-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0002_category_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='cloth_tags',
            new_name='cloth_reviews',
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomm.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='product_name',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_discount',
            field=models.BooleanField(max_length=2000, null=True),
        ),
    ]
