from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recepts", "0002_recept_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recept",
            name="time",
            field=models.CharField(max_length=10),
        ),
    ]