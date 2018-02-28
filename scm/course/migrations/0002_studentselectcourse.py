# Generated by Django 2.0.2 on 2018-02-27 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSelectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentSelectCourse_score', models.CharField(max_length=10, verbose_name='成绩')),
                ('studentSelectCourseAddTime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('studentSelectCourse_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.SelectCourse', verbose_name='课程')),
                ('studentSelectCourse_stduent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.StudentUser', verbose_name='学生')),
            ],
            options={
                'verbose_name': '学生选课表',
                'verbose_name_plural': '学生选课表',
                'ordering': ['-studentSelectCourseAddTime'],
            },
        ),
    ]
