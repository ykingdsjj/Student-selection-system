# Generated by Django 2.0.2 on 2018-02-27 04:42

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='课程编号')),
                ('courseName', models.CharField(max_length=30, verbose_name='课程名称')),
                ('courseCredit', models.CharField(max_length=3, verbose_name='课程学分')),
                ('CourseGrade', models.CharField(choices=[('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014')], default='2017', max_length=4, verbose_name='年级')),
                ('courseMajor', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='management.Major', verbose_name='所属专业')),
                ('coutseInstitute', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='management.Institute', verbose_name='所属学院')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='SelectCourse',
            fields=[
                ('selectCourseID', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='选课编号')),
                ('selectCourseAddTime', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('selectCourseClassTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ClassTime', verbose_name='上课时间')),
                ('selectCourseClassroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Classroom', verbose_name='上课教室')),
                ('selectCourseTeacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.TeacherUser', verbose_name='教师工号')),
                ('selectCourses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程编号')),
            ],
            options={
                'verbose_name': '可选课表',
                'verbose_name_plural': '可选课表',
                'ordering': ['-selectCourseAddTime'],
            },
        ),
    ]
