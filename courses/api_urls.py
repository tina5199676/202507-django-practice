from django.urls import path
from . import views

urlpatterns = [
    # 老師
    path('teachers/', views.TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),

    # 學生
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),

    # 課程
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),

    # 報名
    path('enrollments/', views.enroll_student, name='enroll-student'),
    path(
        'enrollments/<int:student_id>/<int:course_id>/',
        views.withdraw_student,
        name='withdraw-student',
    ),
]