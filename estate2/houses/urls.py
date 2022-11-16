from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('property/<int:id>', views.single,name="single"),
    #path('properties', views.propertiesView.as_view(),name="properties"),
    path('properties', views.list_properties,name="properties"),
    path('about', views.about,name="about"),

    path('add_house', views.add_house,name="add_house"),

    path('update_property/<int:pk>', views.update_property.as_view(),name="update_property"),

    path('delete_property/<int:pk>', views.delete_property.as_view(),name="delete_property"),

    path('userlogin', views.userlogin,name="userlogin"),
    path('userregister', views.userregister,name="userregister"),
    path('userlogout', views.userlogout,name="userlogout"),
    path('Profile', views.Profile,name="Profile"),
    path('messages', views.messages,name="messages"),


    path('search-for', views.search_for,name="search_for"),
    path('get-inquiry', views.get_inquiry,name="get_inquiry"),
    path('show-all-inquiry', views.show_all_inquiry,name="show_all_inquiry"),

    path('write-msg', views.write_msg,name="write_msg"),

    path('show-place/<str:place>', views.show_place,name="show_place"),
    path('show-type/<str:type_of_place>', views.show_type,name="show_type"),

    path('show_all_projects', views.show_all_projects,name="show_all_projects"),
    path('show_all_companies', views.show_all_companies,name="show_all_companies"),

    path('show_single_company/<int:id>', views.show_single_company,name="show_single_company"),
    path('show_single_project/<int:id>', views.show_single_project,name="show_single_project"),

    path('add_project', views.add_project,name="add_project"),
    path('add_company', views.add_company,name="add_company"),

    path('get_type_count', views.get_type_count,name="get_type_count"),
    path('get_type_only/<str:type>', views.get_type_only,name="get_type_only"),

    path('delete_msg/<int:id>', views.delete_msg,name="delete_msg"),
    path('delete_inquiry/<int:id>', views.delete_inquiry,name="delete_inquiry"),

    path('edit_footer/<int:pk>', views.edit_footer.as_view(),name="edit_footer"),
    path('edit_msg/<int:pk>', views.edit_msg.as_view(),name="edit_msg"),
    path('edit_inquiry/<int:pk>', views.edit_inquiry.as_view(),name="edit_inquiry"),
    path('edit_about/<int:pk>', views.edit_about.as_view(),name="edit_about"),
]