# Generated by Django 3.2.3 on 2021-05-16 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='RentSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=7, null=True, verbose_name='Аренда/Продажа')),
            ],
            options={
                'verbose_name': 'аренда/продажа',
                'verbose_name_plural': 'Аренда/Продажа',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nikname', models.CharField(max_length=255, verbose_name='Никнейм')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='reviews/', verbose_name='Фото')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='Видео')),
                ('date', models.DateField(verbose_name='Дата')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='TypeProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=7, null=True, verbose_name='тип недвижимости')),
            ],
            options={
                'verbose_name': 'тип недвижимости',
                'verbose_name_plural': 'Тип недвижимости',
            },
        ),
        migrations.CreateModel(
            name='PostRentSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dom/', verbose_name='Фото')),
                ('status', models.CharField(blank=True, choices=[('С ремонто', 'С ремонтом'), ('Без ремонта', 'Без ремонта ')], max_length=255, null=True, verbose_name='Состояние')),
                ('dom_type', models.CharField(blank=True, choices=[('Апартаменты', 'Апартаменты'), ('Хрущевка', 'Хрущевка'), ('Сталинка', 'Сталинка'), ('Новостройка', 'Новостройка'), ('Чешский проект', 'Чешский проект')], max_length=255, null=True, verbose_name='Тип дома')),
                ('material_type', models.CharField(blank=True, choices=[('Блочный', 'Блочный'), ('Кирпичный', 'Кирпичный')], max_length=255, null=True, verbose_name='Тип материала')),
                ('floors', models.CharField(blank=True, help_text='пример: 3 / 5', max_length=255, null=True, verbose_name='Этаж / этажность')),
                ('rooms', models.IntegerField(blank=True, null=True, verbose_name='Кол-во комнат')),
                ('areas', models.IntegerField(blank=True, null=True, verbose_name='Площадь м²')),
                ('height_ceiling', models.IntegerField(blank=True, null=True, verbose_name='Высота потолков м²')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена в рублях')),
                ('region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Район')),
                ('year_built', models.DateField(blank=True, null=True, verbose_name='Год постройки')),
                ('distance_sea', models.CharField(blank=True, max_length=255, null=True, verbose_name='Расстояние до море')),
                ('distance_track', models.CharField(blank=True, max_length=255, null=True, verbose_name='Расстояние до трассы')),
                ('ownership', models.CharField(blank=True, max_length=50, null=True, verbose_name='Право собственности')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('vip', models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], default=2, max_length=255, null=True, verbose_name='VIP')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='Город')),
                ('rent_sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.rentsale', verbose_name='Аренда/Продажа')),
                ('type_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.typeproperty', verbose_name='Тип недвижимости')),
            ],
            options={
                'verbose_name': 'Тип недвижимости',
                'verbose_name_plural': 'Тип недвижимости',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ImageShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_shots/', verbose_name='Изображение')),
                ('rs_objects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postrentsale', verbose_name='Объекты')),
            ],
            options={
                'verbose_name': 'фотка',
                'verbose_name_plural': 'Фотки',
            },
        ),
    ]
