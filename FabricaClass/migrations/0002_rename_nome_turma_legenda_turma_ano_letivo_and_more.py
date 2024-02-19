from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ("FabricaClass", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="turma",
            old_name="nome",
            new_name="legenda",
        ),
        migrations.AddField(
            model_name="turma",
            name="ano_letivo",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "1º Ano"), (2, "2º Ano"), (3, "3º Ano")],
                default=1,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="turma",
            name="semestre_letivo",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (4, "1º Semestre"),
                    (5, "2º Semestre"),
                    (6, "3º Semestre"),
                    (7, "4º Semestre"),
                    (8, "5º Semestre"),
                    (9, "6º Semestre"),
                    (10, "7º Semestre"),
                    (11, "8º Semestre"),
                    (12, "9º Semestre"),
                    (13, "10º Semestre"),
                ],
                default=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="curso",
            name="turno",
            field=models.IntegerField(
                choices=[
                    (1, "Matutino"),
                    (2, "Vespertino"),
                    (3, "Noturno"),
                    (4, "Integral"),
                ],
                default=4,
            ),
        ),
    ]
