"""EntryTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from luminus.views import course_view, prof_view, TA_view, student_view, forum_view, post_view, tut_view, auth_view

from luminus import views_helper

urlpatterns = [
    path('login/', auth_view.login),
    path('logout/', auth_view.logout),

    path('profs/code/<code>/', prof_view.get_profs_by_coursecode),
    path('prof/uname/<username>/', prof_view.get_prof_by_username),

    path('TAs/code/<code>/', TA_view.get_TAs_by_coursecode),
    path('TAs/<code>/<group_num>/', TA_view.get_TAs_by_coursecode_and_groupnum),
    path('TAs/notin/<code>/<group_num>/', TA_view.get_TAs_notincurtut_by_code_group_num),
    path('TAs/addtut/<uname>/<code>/<group_num>/', TA_view.add_TA_to_tut_by_uname_code_group_num),

    path('students/code/<code>/', student_view.get_students_by_coursecode),
    path('students/code/enroll/<code>/', student_view.add_enroll_request_by_uname_and_code),
    path('students/code/complete/<code>/<uname>/', student_view.mark_enroll_complete_by_uname_and_code),
    path('students/noattend/<code>/', student_view.get_students_noattend_by_coursecode),
    path('students/<code>/<group_num>/', student_view.get_students_by_coursecode_and_groupnum),
    path('students/uname/code/<uname>/<code>/', student_view.get_students_by_student_uname_and_coursecode),
    path('student/addtut/<uname>/<code>/<group_num>/', student_view.add_student_to_tut_by_uname_coursecode_groupnum),
    path('students/code/status/<code>/<status>/', student_view.get_students_by_coursecode_and_status),
    path('student/uname/code/grade/<uname>/<code>/<grade>/', student_view.update_testgrade_by_uname_and_code),
    path('students/calculate/<code>/<a>/<b>/<c>/<d>/<e>/<f>/', student_view.calculate_final_grade),

    path('courses/', course_view.get_courses),
    path('assists/', course_view.get_assists),
    path('course/code/<code>/', course_view.get_course_by_code),
    path('courses/puname/<puname>/', course_view.get_courses_by_puname),
    path('courses/tuname/<tuname>/', course_view.get_courses_by_tuname),
    path('courses/suname/<suname>/', course_view.get_courses_by_suname),
    path('courses/search/<keyword>/', course_view.search_courses),
    path('courses/all/', course_view.get_all_courses),

    path('forums/code/<code>/', forum_view.get_forum_by_code),
    path('forums/view/<code>/', forum_view.get_viewable_forum),
    path('forums/<code>/<group_num>/', forum_view.get_forum_by_code_and_group_num),
    path('forums/notin/<code>/<group_num>/', forum_view.get_forum_notintut_by_code_and_group_num),
    path('forums/addtut/<code>/<group_num>/<fid>/', forum_view.add_forum_to_tut_by_code_group_num_fid),
    path('forum/delete/<code>/<fid>/', forum_view.delete_forum),
    path('forum/add/', forum_view.add_forum),

    path('posts/<code>/<fid>/', post_view.get_posts_by_code_and_fid),
    path('posts/<code>/<fid>/<pid>/', post_view.get_posts_by_code_and_fid_and_pid),
    path('post/add/', post_view.add_post),
    path('post/delete/<code>/<fid>/<pid>/', post_view.delete_post),
    path('reply/add/', post_view.add_reply),

    path('tutorials/code/<code>/', tut_view.get_tutorials_by_coursecode),
    path('tutorials/uname/<username>/', tut_view.get_tutorials_by_student),
    path('tutorials/uname/code/<username>/<code>/', tut_view.get_tutorials_by_student_and_course),
    path('tutorials/ta/<code>/', tut_view.get_tutorials_by_tA_and_course),
    path('tutorials/<code>/<num>/', tut_view.get_tutorials_by_course_and_group),

    path('requests/code/<code>/', student_view.get_requests_by_coursecode),
    path('requests/approve/<uname>/<code>/', student_view.approve_requests),
    path('requests/reject/<uname>/<code>/', student_view.reject_requests),

    path('candidates/code/<code>/', student_view.get_ta_candidates_by_coursecode),
    path('candidates/add/<uname>/<code>/', student_view.add_ta_by_uname_coursecode_group),

    path('attendance/get/<uname>/<code>/<group_num>/', tut_view.retrieve_attendance_by_uname_code_group_num),
    path('attendance/add/<uname>/<code>/<group_num>/<attend_week>/', tut_view.add_stu_to_attendance_by_uname_code_group_num),

    url(r'', auth_view.default)

    # path('add/', views_helper.add_participator),
]
